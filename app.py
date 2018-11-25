import requests


class AddressSearcher:
    def __init__(self):
        self.base_url = f"http://zipcloud.ibsnet.co.jp/api/search"

    def search(self, postal_code):
        url = f"{self.base_url}?zipcode={postal_code}"
        response = requests.get(url)
        response_dict = response.json()

        if response_dict["results"] == None:
            return "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"

        都道府県 = response_dict["results"][0]["address1"]
        市区町村 = response_dict["results"][0]["address2"]
        町域 = response_dict["results"][0]["address3"]
        return f"{都道府県}{市区町村}{町域}"

    # def search2(self, postal_code):
    #     url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=1760014"
    #     response = requests.get(url)
    #     response_dict = response.json()
    #
    #     都道府県 = response_dict["results"][0]["address1"]
    #     市区町村 = response_dict["results"][0]["address2"]
    #     町域 = response_dict["results"][0]["address3"]
    #     return f"{都道府県}{市区町村}{町域}"