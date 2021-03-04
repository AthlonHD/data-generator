# -*- coding = utf-8 -*-

import random
import time
import pymysql
from pymysql import connect


def datatosql():
    """
    将数据写入数据库
    """
    connect_mysql = pymysql.connect('10.24.67.188', user='root', password='z6S0PSWjdxxNM9bS', db='For_Test_CASE')
    print(connect_mysql)
    print(type(connect_mysql))
    cursor = connect_mysql.cursor()
    print(cursor)

    nrange = 50000

    for i in range(nrange):
        si = str(i)
        id = i
        gender = random.randint(0, 1)
        realname = 'jackma' + si
        phone = 18510000000 + i
        email = str(realname) + '@email.com'
        notes = '这是一段备注的内容'

        # print(realname)
        # print(type(realname))
        # print(email)
        # print(type(email))
        # print(notes)
        # print(type(notes))
        # create_time 和 update_time 由表自动生成

        # cursor.execute(sql)

        if i == 0:

            sql = "insert into 5k_data_table_00 (id, gender, realname, phone, email, notes) values (%s, %s, '%s', %s, '%s', '%s'),\n" \
                  % (id, gender, realname, phone, email, notes)
            print(sql)

        elif i == nrange - 1:

            sql = "(%s, %s, '%s', %s, '%s', '%s');\n" \
                  % (id, gender, realname, phone, email, notes)
            print(sql)

        else:

            sql = "(%s, %s, '%s', %s, '%s', '%s'),\n" \
                  % (id, gender, realname, phone, email, notes)
            print(sql)

        print('正在写入第%s遍\n' % (i + 1))
        with open('5kdata.txt', 'a') as f:
            f.write(sql)

    pass


if __name__ == '__main__':
    datatosql()
