import urllib3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def login(s):
    # s = requests.session()
    url = "https://dp.ssl.ysten.com/api/student/loginForMobile"

    headers= {
        "Api-Version":"v1",
        "Device-Type":"tv",
        "Channel-Key":"d25cd4f36e2f98e3462cab3d92c0d776"  #d25cd4f36e2f98e3462cab3d92c0d776
        }
    boy = {
        "phone_no":"17601250863",
        "code":"9526"
        }
    r =s.post(url,headers=headers,data=boy,verify=False)
    print(r.text)
    s.headers.update(headers)
    token=r.json()["data"]["token"]

    print(token)
    return token


if __name__=='__main__':
    s=requests.session()
    login(s)




#获取订单已取消的
def din(login):
    url2 = "https://dp.ssl.ysten.com/api/order/myOrder"

    date = {
        "token": "token",
        "status": "-1",
        "order_id": "-1"
    }
    r2 = s.get(url=url2, params=date, verify=False)
    print(r2.text)
