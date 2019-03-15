import requests
from requests.auth import HTTPDigestAuth


def changeLogTries(ip,port,login,password,mode):
    url = 'http://{}:{}/ISAPI/Security/illegalLoginLock'.format(ip, port)
    if mode == 1:
        payload = "<IllegalLoginLock><enabled>false</enabled></IllegalLoginLock>"
    if mode == 2:
        payload = "<IllegalLoginLock><enabled>true</enabled></IllegalLoginLock>"
    try:
        requests.put(url, auth=HTTPDigestAuth(login, password), data=payload)
        return "OK, changed"
    except:
        return "False, error with data "
