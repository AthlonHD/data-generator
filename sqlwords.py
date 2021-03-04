# -*- coding=utf-8 -*-

for i in range(100):
    text = "('{0}', '{1}'),".format(str(i), '这是第' + str(i) + '行')
    sql = 'insert into "For_Test_Table_00"(id, "CONTENT") VALUES ' + text
    print(sql)
    with open('data.txt', 'a') as f:
        f.write(text)
