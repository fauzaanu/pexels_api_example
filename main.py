import os

import requests


class Pexels:
    def __init__(self, api_key):
        self.headers = {
            "Authorization": f"{api_key}"
        }

    class Limits:
        def __init__(self):
            self.remaining = int()

    def update_rate_limit_info(self,response):
        self.Limits.remaining = response.headers["X-Ratelimit-Remaining"]

    def search(self,keyword):
        url = "https://api.pexels.com/v1/search"
        data = {
            "query":f"{keyword}"
        }
        response = requests.get(url, headers=self.headers, data=data)
        self.update_rate_limit_info(response)

        print("Remaining Limit",)
        # if response.headers["X-Ratelimit-Limit"]
        #print(response)
        return response

    def video_search(self,keyword):
        url = "https://api.pexels.com/videos/search"
        data = {
            "query":f"{keyword}"
        }
        response = requests.get(url, headers=self.headers, data=data)
        self.update_rate_limit_info(response)

        return response


if __name__ == "__main__":
    # print(os.environ.get('PEXELS_AK'))

    px_api_key = os.environ.get('PEXELS_AK')
    pexels_instance = Pexels(px_api_key)
    crow_search = pexels_instance.search("Crow")
    crow_video_search = pexels_instance.video_search("Crow Flying up")
    print(crow_search.json())
    print("================")
    print(crow_video_search.json())


