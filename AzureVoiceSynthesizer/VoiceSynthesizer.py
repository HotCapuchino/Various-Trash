from Auth_data import AuthData
import requests


class Synthesizer:

    def __init__(self, user_data):
        self.__user_data = user_data
        self.__auth_data = AuthData()

    def getAudio(self, token):
        headers = {"X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
                   "Content-Type": "application/ssml+xml",
                   "User Agent": "My_app",
                   "Bearer": token}
        body = "<speak version='1.0' xml:lang='" + self.__user_data["lang"] + \
               '><voice xml:lang=' + self.__user_data["lang"] + \
               ' xml:gender=' + self.__user_data["gender"] + \
               ' name=' + self.__user_data["name"] + "\'>" + self.__user_data["text"] + "</voice></speak>"
        request = requests.post(self.__auth_data.getHost(), headers=headers, data=body.encode('utf-8'))
        response = request.status_code
        return response
