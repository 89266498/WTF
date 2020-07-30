import requests, json
import datetime
import pandas  as pd


def qnm(sj):
    url = 'http://yx.chd.com.cn/marketing/unit/getOrganization.do?parent=%23'

    cookie = "wpsqing_autoLoginV1=1; wps_sid=6a51dc1006de0bc16e97cb61dc654893a2b93c4c0000004aba; csrf=s5zc7wC7QDz4bjFXCMpXTi5Ms3CFi5W2; JSESSIONID=0000DA9SwZHPAQzwHOnJJ7ogASl:1a6aicc23; LtpaToken2=0r4GEidfkODBphBqP0HmQ0iWV/JOcHYBqddOGvgU7PqL1QdCj+At3koDzPdkfpc63tlx6F1pTgZuVCdzzQMNVJ6a+bnPmicpDJS7wU88DcaZR26qMkJZNsl3ZorzQsmWJc+r5Gbu3cu/PAS1x4zqEliMx/b3gb2aF2gv7SpJJ1b5jkv5OyD5KF27ugk/a0cO80pT5RgbnkpZ4wW/z4NvqFjTimV7k5aoZ971EKsFY6pPh32h3CMWIpCcgDEvIqYKS3VptSRDzqmozr6yd3IcQnAGVVzfL1ZzEQqBvq+eqCMalGsPx3nj6+2D15Cww7QpwjTUQF+Bnj7Na/b2lX5YN36VIwPUbo6KBvA5ShJKlxrkKkVYOO3LjSkVaapKSbi9vLEC6TgJruGAG6FSzs2WhqEnAgPSeO5kWcDhQr+Ztq9Sl5bqOh2QEBTH/gvoFLKazbQfaT0R8sxKMrT5v+DXg/wO/h895ZBFAhEW97De4yVjUwDhjD6hZMYrXK0SJfvoHmCgz5//n095p1fkOFGaV98wzE3myVCLrIDqnjYgAz5kOVV7F0AqB9wtLrhjIGFulBzmDZWeHJorhKGKJc/SLvmCatsQY2yGbrjPKssRWGiftG4ISnxD2sEyK/Gl2QlEgNfsUR5be+pyDN2wrvTWVM+/aB0eXC96NsMZU5lIdxhFRtaVjV7Timrxxnno0MSB"
    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'yx.chd.com.cn',
        'Origin': 'http://yx.chd.com.cn/marketing/market/unitMaintain.sac',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }  # headers的例子，看你的post的headers

    data = {'parent': '#'}
    r = requests.get(url, headers=headers, data=data)
    print(r.json())

    with open(r'e:\123.txt', 'w+') as fb:
        fb.write(r.text)

    retall = []
    getallorg(r.text, retall)

    print('ret:')
    print(retall)

    with open(r'e:\orgs.txt', 'w+') as fp:
        fp.writelines(retall)


def getallorg(str, ret):
    jsn = json.loads(str)
    if not jsn.get('leaf'):
        ret.append(r"{0},{1},{2}\n".format(jsn.get('id'), jsn.get('text'), '0'))
        childs = jsn.get('children')
        for child in childs:
            getallorg(json.dumps(child), ret)
    else:
        ret.append(r"{0},{1},{2}\n".format(jsn.get('id'), jsn.get('text'), '1'))


qnm('')
