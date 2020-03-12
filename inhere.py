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

    def copycontract(self):
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfilename()
        filename = os.path.basename(file)
        shutil.copyfile(file, os.path.join(self.propath, filename))


def makeys(ret, name):
    fp = os.path.join(ret, '验收')
    if not os.path.exists(fp):
        os.makedirs(fp)

    os.chdir(fp)
    with open(name + '-验收报告.txt', 'a') as f:
        print(name + '-验收报告.txt')


def makefy(dst, hetongname):
    fp = os.path.join(dst, '发运')
    if not os.path.exists(fp):
        os.makedirs(fp)
    os.chdir(fp)
    with open(hetongname.split('.')[0] + '-项目发运.txt', 'a') as f:
        print(hetongname + '-项目发运.txt')


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


def copyfyd(info):
    dst = r'C:\Users\gao\Desktop\环保\projects\000000\temp1'
    if not os.path.exists(dst):
        shutil.copytree(r'C:\Users\gao\Desktop\环保\projects\000000\项目发运', dst)

    file = os.path.join(dst, 'word', 'document.xml')
    print(file)

    with open(file, 'r', encoding='utf-8') as f:
        xml = f.read()  # 打开并读取xml

    for k, v in info.items():
        xml = xml.replace(k, v)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(xml)

    zip_docx(dst, r'C:\Users\gao\Desktop\环保\projects\000000\1.docx')
    shutil.rmtree(dst)


def zip_docx(startdir, file_news):
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()
