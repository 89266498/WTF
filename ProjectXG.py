from inhere import myproject
import re


info ={'Cid':'2019173067',
'Cname':'广东华电韶关热电环保',
'Ccompany':'广东华电韶关热电有限公司',
'Caddress':'广东省韶关南雄市珠玑工业园',
'Cperson':'潘贵民',
'Cphone':'15733228728',
       }



path = r"C:\Users\gao\Desktop\环保\projects"
name = "2019173067广东华电韶关热电有限公司环保信息化平台合同"
filename = "韶关热电"

a1 = myproject(path)
a1.makepro('闵行能源')




id = re.match(r"\d*",name)
org = re.match(r"[^0-9]*",name)




