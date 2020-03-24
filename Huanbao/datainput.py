import requests, json
import datetime

import  pandas  as pd

def qnm(sj):
    url = 'http://env.chd.com.cn:81/AddMessage.aspx'

    cookie = "Isover=no; 63f54585-1b20-426a-b1f3-9b81eed2511fAnswer_radio=c06df71c-3ca1-4ec9-8c83-ccf25a020a42#A$c9bcf830-c93d-459b-8a94-f23baa7af46f#A$; 63f54585-1b20-426a-b1f3-9b81eed2511fsubmit=yes; PaperID=29638e3f-b34a-4ced-a79b-64cfe20f5f2b; PlanID=4f4418e7-a0c7-4f39-886f-fc67a1f9401c; orgName=org=G001; BIGipServer~Chd-app~POOL_HBRTMS_81=973359114.20736.0000; LtpaToken2=iIxbr3jp2ic3KNz+iAoKNdrSrFf6zxJaCjlobyvJ6kScBkjuFeEN392Gm+G4HeEuNO+pTP4T9zxL0oMCQHFMERFyBMXFriUYixjlCQzkHLQHyy07dD2mirUm5uOmECFTZnC2+5EOgpyikGVY1SZzLi8evcmbVP0zZ0P76Teh65A4gzJSLGBe9P3PRwohd5qrTmqFHgBxesV1vHoeD7hHE/iFkj3gXJHILpU6mJi2W9nLQg/tlx6t8ZdtOqH12Mgv03gXNkl61Y7OFIBOYKTaI/NgRyc1dGsWVyPKWqX81zvUY9HJl06+VBeznhruoFTRSLlf17HuUWgyqOQtn+wQzkmXVMLkXNG584iwXxX09HN646SzjBGrXiDE2Qj9qJlHstOIXpfFI2GS3jeZqhC3W3Y/nOx7cek2t/vpEnuD+J6SzVRH1p2EQ3npzr/9juqqq04Q84x4P/7rbYfpKW2VH1o/W1ir8/sS3oSY8pZR3SSbrybVOBGbqK6GS45yTjJkzTUoMADxCKrmzg8fACvqni38b6JUBQhfBAg3TgqNHHlpHEP9x0de+EWIUjhT3cFfXsU0ws9dmBaRSbgWeuZi+3tRTPVa940MHzPTf7JD1Db7Fdu+w4wLKX31j/JEyyBp3I1iAxwlbMOQzi3tgy6MmAQZtg3CxDISc1I9Px0ZiIk=; ASP.NET_SessionId=cgcgmpfgh40jsf4wx4edxy0c; ID_KEY=zhongxj; T_USERID=zhongxj; JSESSIONID=0000ZBRGg2BxUJ77xFlCVsnatpI:19hsofm6s; __session:frm:=http:"
    headers = {
        'Accept': 'application/json, text/javascript, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'env.chd.com.cn:81',
        'Origin': 'http://env.chd.com.cn:81',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }  # headers的例子，看你的post的headers

    data = {'param': 'addxls', 'jzid': 'PSTP05', 'xls': sj, 'fjids': '7846'}
    print(data)
    r = requests.post(url, headers=headers, data=data)
    print(r)
    print(r.text)


def all():
    rq = '2020-01-31'
    df=pd.read_excel(r'123.xls')#可以通过sheet_name来指定读取的表单
    data = df[df['RQ']==rq]
    #data['RQ1'] = rq
    print(data)
    # data.to_excel(r"e:\%s.xls"%rq,index=False,sheet_name='补录记录')
    i=0
    ret=''
    for index, row in data.iterrows():
        t = "%s %02d:00:00" %(rq,i)
        for str in df.columns.values:
            if str not in('RQ','SJ'):
                r = '%s,%s,%s@'%(str,t,row[str])
                print(r)
                ret=ret+r
        i=i+1
        print(i)
    ret=ret[:-1]
    print(ret)
    qnm(ret)

st = datetime.datetime.strptime('2020-01-01','%Y-%m-%d')
et = datetime.datetime.strptime('2020-02-01','%Y-%m-%d')
t=st
while t<et:
    print(t.strftime('%Y%m%d'))
    t = t+datetime.timedelta(days=1)

print(datetime.datetime.now().strftime("%Y%m%d"))
