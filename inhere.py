import os
import shutil
import re
import zipfile
import tkinter as tk
from tkinter import filedialog


class myproject:
    rootpath = ''
    proname = ''

    propath = ''
    cname = ''

    def __init__(self, rootpath, ):  # 构造函数
        """初始化属性name和age"""
        self.rootpath = rootpath

    def makepro(self, proname):
        self.proname = proname
        self.propath = os.path.join(self.rootpath, self.proname)
        if not os.path.exists(self.propath):
            os.makedirs(self.propath)
        self.copycontract()

    def loadpro(self, proname):
        self.proname = proname
        self.propath = os.path.join(self.rootpath, self.proname)
        if not os.path.exists(self.propath):
            print('NOT EXIST!')

    def copycontract(self):
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfilename()
        filename = os.path.basename(file)
        shutil.copyfile(file, os.path.join(self.propath, filename))

    def makefy(self,info):
        fp = os.path.join(self.propath, '发运')
        if not os.path.exists(fp):
            os.makedirs(fp)
        self.copyfyd(info)



    def zip_docx(self,startdir, file_news):
        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()

    def copyfyd(self,info):
        dst = os.path.join(self.rootpath,r'000000\temp1')
        sur = os.path.join(self.rootpath,r'000000\项目发运')
        if not os.path.exists(dst):
            shutil.copytree(sur, dst)
        file = os.path.join(dst, 'word', 'document.xml')

        with open(file, 'r', encoding='utf-8') as f:
            xml = f.read()  # 打开并读取xml

        for k, v in info.items():
            xml = xml.replace(k, v)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(xml)

        filename = os.path.join(self.rootpath,self.propath,"发运",info['Cid']+info['Cname']+".docx")
        print(filename)
        self.zip_docx(dst, filename)
        shutil.rmtree(dst)




def makeys(ret, name):
    fp = os.path.join(ret, '验收')
    if not os.path.exists(fp):
        os.makedirs(fp)

    os.chdir(fp)
    with open(name + '-验收报告.txt', 'a') as f:
        print(name + '-验收报告.txt')





# def makepro(path, filename):
#     root = tk.Tk()
#     root.withdraw()
#
#     hetong = filedialog.askopenfilename()
#
#     ret = os.path.join(path, filename)
#     if not os.path.exists(ret):
#         os.makedirs(ret)
#     os.chdir(ret)
#     hetongname = os.path.basename(hetong)
#     shutil.copyfile(hetong, hetongname)
#     return os.path.curdir



