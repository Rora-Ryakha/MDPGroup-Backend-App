import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from constraints import change_dict


def login_check(request):
    if "login" not in request.data:
        return False

    login = request.data["login"]
    if len(login) == 12 and login[0] == "+":
        for n in login[1:]:
            if not (n.isdigit()):
                return False
        return True
    else:
        if login.count("@") == 1:
            if len(login[:login.index('@')]) > 64 or len(login) > 254:
                return False
            if login[0] == '@' or login[-1] == '@' or login[0] == '.' or login[-1] == '.' or login.count(' ') > 0:
                return False
            return True
        else:
            return False


def inn_check(request):
    if "inn" not in request.data or "username" not in request.data:
        return False

    if request.data["username"][:3] in change_dict.keys():
        request.data["username"] = change_dict[request.data["username"][:3]] + request.data["username"][3:]
    elif request.data["username"][:4] in change_dict.keys():
        request.data["username"] = change_dict[request.data["username"][:4]] + request.data["username"][4:]

    options = Options()
    options.add_argument("--headless")
    browser = wd.Firefox(options=options)
    browser.get("https://egrul.nalog.ru/index.html")
    search = browser.find_element(by=By.ID, value="query")
    search.send_keys(str(request.data["inn"]))
    button = browser.find_element(by=By.ID, value="btnSearch")
    button.click()
    time.sleep(2)
    try:
        found = (browser.find_element(by=By.CLASS_NAME, value="res-caption")).text
        if found == request.data["username"]:
            return True
        return False
    except:
        return False
