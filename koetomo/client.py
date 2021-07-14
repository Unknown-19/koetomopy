from config import config
import random
import requests

class koetomo():
    def __init__(self):
        self.headers = {
            'User-Agent': config.VERSION
        }
        self.request = requests.Session()

    def CreateAccount(self):
        param = {
            "auth_token": "",
            "version": config.VERSION,
            "email": self.email,
            "password": self.GeneratePassword(),
            "name": "ao",
            "sex": "2",
            "birthday": "2006/01/02",
            "device_uid": "11c6fd8b0d528bd7"
        }
        r = self.request.post(
            config.HOST_URL + config.SIGNUP_ACCOUNT,
            headers=self.headers,
            params=param
        )
        print(r.json())
        self.authtoken = r.json()["data"]["auth_token"]
        print(self.authtoken)

    def LoginAccount(self):
        param = {
            "auth_token": self.authtoken,
            "version": config.VERSION,
            "email": self.email,
            "password": self.passwd,
            "device_uid": "11c6fd8b0d528bd7",
            "feature": "skwmeshroom,firebase"
        }
        r = self.request.post(
            config.HOST_URL + config.LOGIN_ACCOUNT,
            headers=self.headers,
            params=param
        )
        print(r.json())

    def RegisterEmail(self):
        param = {
            "auth_token": "",
            "version": config.VERSION,
            "email": self.CreateEmail()
        }
        r = self.request.post(
            config.HOST_URL + config.EMAIL_REGISTER,
            headers=self.headers,
            params=param
        )
        if r.status_code == 200:
            print("RegisterEmail: ok")
            print(r.json())
        else:
            print(r)
    def random_string(self, num):
        passwd = "abcdefghijklmnopqrstuvwxyz1234567890"
        return "".join([random.choice(passwd) for _ in range(num)])

    def CreateEmail(self):
        self.email = f"{self.random_string(7)}@{self.random_string(3)}.co.jp"
        return self.email

    def GeneratePassword(self):
        self.passwd = f"{self.random_string(5)}"
        return self.passwd

    def GenerateName(self):
        self.name = f"{self.random_string(5)}"
        return self.name

    def GenerateDeviceid(self):
        self.uid = f"{self.random_string(16)}"
        return self.uid

x = koetomo()
x.RegisterEmail()
x.CreateAccount()
x.LoginAccount()
