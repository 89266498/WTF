import ibm_db

connStr = "DATABASE=HD_DPTST;HOSTNAME=10.76.65.49;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=instycjn;"
conn = None
try:
    # 连接数据库
    conn = ibm_db.connect(connStr, "", "")
    # 以插入语句为例,删除和更新只需要替换语句即可
    sql = "insert into tab_student values('%s', '%s')" % (1, "Jet")
    # 执行SQL语句
    stmt = ibm_db.exec_immediate(conn, sql)
    # 获取受影响的行数
    rows = ibm_db.num_rows(stmt)
except Exception as ex:
    print(ex)
finally:
    # 关闭数据库
    ibm_db.close(conn)
