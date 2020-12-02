
class AuthData:

    __key = "1db01788ad86488d90d573a7fe502c11"
    __auth_url = "https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    __lang_url = "https://eastasia.tts.speech.microsoft.com/cognitiveservices/voices/list"
    __host = "https://eastasia.tts.speech.microsoft.com/cognitiveservices/v1"

    def getKey(self):
        return self.__key

    def getAuthURL(self):
        return self.__auth_url

    def getLangURL(self):
        return self.__lang_url

    def getHost(self):
        return self.__host
