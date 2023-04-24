
class Recoginize:
    """
    token: string
    file: image file
    """
    def __init__(self, token, image):
        self.url = 'https://api.edenai.run/v2/image/object_detection'
        self.headers = {
            "Content-Type": "multipart/form-data",
            "Authorization": f"Bearer {token}"
        }
        self.image = image

    def objects_recognize(self):


        payload = {
            "providers": "api4ai",
            "file": self.image
        }

        # response = requests.post(self.url, data=payload, headers=self.headers)
        #
        # data = response.json()
        # print(data)