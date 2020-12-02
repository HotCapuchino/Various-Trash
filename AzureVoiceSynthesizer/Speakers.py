import requests
from Auth_data import AuthData


class Speakers:

    __speakers = None

    def __init__(self):
        self.__lang = AuthData().getLangURL()

    def fetchLanguages(self, token):
        speakers_headers = {"Authorization": "Bearer " + token}
        self.__speakers = requests.get(self.__lang, headers=speakers_headers).json()

    def getLanguages(self):
        if self.__speakers:
            return self.__speakers
        else:
            print("First send the request for getting languages!")

