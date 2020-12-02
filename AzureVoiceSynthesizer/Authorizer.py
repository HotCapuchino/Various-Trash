from Auth_data import AuthData
import requests


class Authorizer:

    __token = ""

    def __init__(self):
        self.__auth_data = AuthData()

    def auth(self):
        headers = {"Ocp-Apim-Subscription-Key": self.__auth_data.getKey()}
        response = requests.post(self.__auth_data.getAuthURL(), headers=headers)
        token = str(response.text)
        if not token:
            print("Oops! Something's gone wrong with authentication!")
            return Exception()
        else:
            self.__token = token

    def getToken(self):
        if self.__token:
            return self.__token
        else:
            print("First of all, you have to pass authentication!")