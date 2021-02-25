

def test_01(add): #查看取消订单
    url2 = "https://dp.ssl.ysten.com/api/order/myOrder"
    s = add
    date = {
        "token": "OsDjljfyMTc2MDEyNTA4NjNfdHZfN18xNTc2MDUzMTU3",
        "status": "-1",
        "order_id": "-1"
      }
    r2 = s.get(url=url2, params=date, verify=False)
    print(r2.text)
    assert r2.json()["code"]==200
    assert r2.json()["msg"]=="Success!"

def test_02(unloging):
    s=unloging

    # 获取老师id
    url4 = "http://dp.ssl.ysten.com/api/schedule/teacherDetail"
    data = {
        "teacher_id": 5
    }
    r4 = s.get(url=url4, params=data, )
    print(r4.text)
    assert r4.json()["code"]==0
    assert r4.json()["msg"]=="教师信息异常！"

def test_03(unloging):
    # h获取三师直播课列表
    s=unloging
    url5 = "https://dp.ssl.ysten.com/api/schedule/mySanShiList"
    data = {
        "token": "OsDjljfyMTc2MDEyNTA4NjNfdHZfN18xNTc2MDUzMTU3",
        "schedule_type": 2
    }
    r5 = s.get(url=url5, params=data)
    print(r5.text)
    assert r5.json()["code"]==200
    assert r5.json()["msg"]=="Success!"






















