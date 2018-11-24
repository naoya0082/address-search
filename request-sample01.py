import requests

# 岩手県八幡平大更の情報をrequestsモジュールを使って取得
response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=3730845")
print(response)
