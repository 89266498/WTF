from inhere import myproject
import re


info ={'Cid':'2018173106',
'Cname':'深圳坪山环保信息化平台项目',
'Ccompany':'华电国际电力股份有限公司深圳公司',
'Caddress':'深圳市坪山区坑梓街道青松路2号',
'Cperson':'张鑫',
'Cphone':'18126232023',
       }



path = r"C:\Users\gao\Desktop\环保\projects"
name = "2019173067广东华电韶关热电有限公司环保信息化平台合同"
filename = "深圳坪山"

a1 = myproject(path)
a1.makepro('深圳坪山')
a1.makefy(info)




id = re.match(r"\d*",name)
org = re.match(r"[^0-9]*",name)




