import requests
from requests.auth import HTTPDigestAuth


def changeLogTries(ip,port,login,password):
    url = 'http://{}:{}/ISAPI/Security/illegalLoginLock'.format(ip, port)
    payload = "<IllegalLoginLock><enabled>false</enabled></IllegalLoginLock>"
    try:
        r = requests.put(url, auth=HTTPDigestAuth(login, password), data=payload)
        return "OK, changed"
    except:
        return "False, error with data "
