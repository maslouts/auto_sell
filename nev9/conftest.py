from nev9.hanshu import login
import requests
import  pytest

@pytest.fixture(scope="module")

def add():
    print("先登录")
    s = requests.session()
    login(s)
    return s
@pytest.fixture(scope="function")
def unloging():
    print("不登录")
    """自定义不登录"""
    s=requests.session()
    s.headers.update({"Api-Version":"v1","Device-Type":"tv", "Channel-Key":"d25cd4f36e2f98e3462cab3d92c0d776" })
    return s