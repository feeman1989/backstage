# -*- coding: utf-8 -*-
__author__ = 'YW0463'
import xlrd
import MySQLdb
def conn_db():
    conn = MySQLdb.connect(user="root",db="backstage",passwd="root123ROOT",port=4769,host="localhost",charset="utf8")
    cursor = conn.cursor()
    sql = "insert into app_machine_info values(%s,%s,%s,%s,%s,%s)"
    for x,info in enumerate(get_info()):
        print x,info
        cursor.execute(sql,(x,info[0],info[1],info[2],info[3],info[4]))
def get_info():
    workbook = xlrd.open_workbook(u'C:\\Users\\yw0463\\Desktop\\openserver\\hero服务器密码_tx.xlsx')
    booksheet = workbook.sheets()[0]
    total_rows = int(booksheet.nrows)
    total_data = []
    for n in range(1,total_rows):
        total_data.append(booksheet.row_values(n))
    title_list = []
    zone_list = []
    world_id_list = []
    local_ip_list = []
    inter_ip_list = []
    for x in total_data:
        title_list.append(x[0])
        zone_list.append(x[-3])
        world_id_list.append(x[-2])
        local_ip_list.append(x[2])
        inter_ip_list.append(x[1])
    list = []
    for x,y in enumerate(zone_list):
        list.append([title_list[x],y,world_id_list[x],local_ip_list[x],inter_ip_list[x]])
    return list
conn_db()