import unittest
import requests


class AddressSearcher:
    def search(self, postal_code):
        url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
        response = requests.get(url)
        response_dict = response.json()

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



class TestAddressSearcher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得(self):
        address_searcher = AddressSearcher()

        actual = address_searcher.search(postal_code="0287111")
        self.assertEqual("岩手県八幡平市大更", actual)

    def test_東京都練馬区豊玉南の地名を郵便番号から取得(self):
        address_searcher = AddressSearcher()

        actual = address_searcher.search(postal_code="1760014")
        self.assertEqual("東京都練馬区豊玉南", actual)


if __name__ == "__main__":
    unittest.main()
