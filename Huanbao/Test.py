import ibm_db
import pandas as pd
import sqlalchemy
from sqlalchemy import *
import ibm_db_sa
import os
import getopt
import sys
import config
import re


def main(argv):
    try:
        options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])
    except getopt.GetoptError:
        sys.exit()

    for option, value in options:
        if option in ("-h", "--help"):
            print("help")
        if option in ("-i", "--ip"):
            print("ip is: {0}".format(value))
        if option in ("-p", "--port"):
            print("port is: {0}".format(value))

    print("error args: {0}".format(args))


def getallconfig(unit):
    if not os.path.exists(unit):
        os.makedirs(unit)
    for key, cmd in config.getsqlcmds(unit).items():
        getxlsxfordb(os.path.join(unit, key + '.csv'), cmd)


def columnsfilter(cols, filtercols=None):
    colstr = ""
    for col in cols:
        if filtercols is None or col not in filtercols:
            colstr += "{0},".format(col)
    colstr = colstr.rstrip(',')
    return colstr


def rowsfilter(row, filtercols=None):
    vals = ""
    for key, value in row.items():
        if filtercols is None or key not in filtercols:
            vals += "'{0}',".format(value)
    vals = vals.rstrip(',')
    return vals


def get_filePath_fileName_fileExt(fileUrl):
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension


def getsqlfromxlsx(filename, sqlfile, filtercols=None):
    df = pd.read_csv(filename, encoding='gbk')
    df = df.dropna(axis=1, how='any')
    ret = ""
    ph, tablename, ext = get_filePath_fileName_fileExt(filename)
    print(tablename)

    sqlc = r"INSERT INTO {0} ({1}) VALUES ({2});"
    colstr = columnsfilter(df.columns.values, filtercols)

    for index, row in df.iterrows():
        val = rowsfilter(row, filtercols)
        sqlt = sqlc.format(tablename, colstr, val)
        ret += sqlt + "\n"
    with open(sqlfile, 'w+') as fp:
        fp.write(ret)


# getsqlfromxlsx(r"123.csv","123.sql",['RQ','SJ'])

def getxlsxfordb(filename, sql):
    # sheetname = filename.split('.')[0]
    try:
        engine = sqlalchemy.create_engine("ibm_db_sa://db2inst2:db2inst2\
                                          @10.72.4.128:50001/JTHB?charset=utf8")
        data = pd.read_sql_query(sql, con=engine)
        if len(data) > 0:
            data.to_csv(filename, index=False)
    except Exception as ex:
        print(ex)
    finally:
        # 关闭数据库
        engine.dispose()


# pd.io.sql.to_sql(df,table_name,con=conn,schema='w_analysis',if_exists='append')
# getxlsxfordb(r'123.xlsx',r'select * from administrator.t_base_org')

def test():
    connStr = "DATABASE=JTHB;HOSTNAME=10.72.4.128;PORT=50001;PROTOCOL=TCPIP;UID=db2inst2;PWD=db2inst2;"
    conn = None
    try:
        # 连接数据库
        conn = ibm_db.connect(connStr, "", "")
        # 以插入语句为例,删除和更新只需要替换语句即可
        sql = "select * from administrator.t_base_org"
        # 执行SQL语句
        stmt = ibm_db.exec_immediate(conn, sql)
        dictionary = ibm_db.fetch_both(stmt)
        for key, value in dictionary.items():
            print('%s:%s' % (key, value))
        # 获取受影响的行数
    except Exception as ex:
        print(ex)
    finally:
        # 关闭数据库
        ibm_db.close(conn)


def getdcunit(unit):
    info = {'dc': re.match(r'[A-Z]*', unit).group(),
            'jz': re.findall(r'\d+', unit)[0],
            }
    print(info)
    return info


def repunit(source, dest):
    sourceinfo = getdcunit(source)
    destinfo = getdcunit(dest)

    filenames = []
    if os.path.exists(source):
        for root, dirs, files in os.walk(source):
            for file in files:
                filenames.append(os.path.join(root, file))
    if not os.path.exists(dest):
        os.makedirs(dest)
    print(filenames)
    for str in filenames:
        df = pd.read_csv(str)
        df.replace(source, dest, inplace=True, regex=True)
        df.replace('{0}:{1}'.format(sourceinfo['dc'], sourceinfo['jz']),
                   '{0}:{1}'.format(destinfo['dc'], destinfo['jz']), inplace=True, regex=True)
        df.to_csv(str.replace(source, dest), index=False)
        print(df)


# repunit('BRPC01', 'BRPC03')
getsqlfromxlsx(r"e:\T_BASE_STAT_PARA4.csv", r"e:\123.sql")

# if __name__ == '__main__':
#
#     cmd = sys.argv[1]
#     para = sys.argv[2]
#     print("{0},{1}".format(cmd, para))
#     if cmd == 'get':
#         print("{0},{1}".format(cmd, para))
#         getallconfig(para)
