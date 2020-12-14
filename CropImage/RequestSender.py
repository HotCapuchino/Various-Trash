import requests


class Connector:
    __url = "https://fdfhsf.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false" \
        "&recognitionModel=recognition_03&returnRecognitionModel=false&detectionModel=detection_02"
    __key = "11953edd085047358fb48de93cac6dad"

    def __init__(self, binary_data):
        self.binary_data = binary_data

    def recieveFaceCoordinates(self):
        headers = {
            "Content-Type": "application/octet-stream",
            "Ocp-Apim-Subscription-Key": self.__key
        }
        body = self.binary_data
        request = requests.post(url=self.__url, headers=headers, data=body)
        if request.status_code != 200:
            print("Oops! Error occurred!")
            return request.json()
        return request.json()