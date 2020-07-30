from inhere import myproject
import re


info = {'Cid': '2019171064',
        'Cname': '天津华电南疆热电环保信息化平台项目',
        'Ccompany': '天津华电南疆热电有限公司',
        'Caddress': '天津市塘沽区港塘路2657号 天津华电南疆热电有限公司 物资部',
        'Cperson': '曾春',
        'Cphone': '18874053395',
        }



path = r"C:\Users\gao\Desktop\环保\projects"
name = "2019173067广东华电韶关热电有限公司环保信息化平台合同"
filename = "深圳坪山"

a1 = myproject(path)
a1.makepro('天津南疆')
a1.makefy(info)




id = re.match(r"\d*",name)
org = re.match(r"[^0-9]*",name)




