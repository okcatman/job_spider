#!/usr/bin/env python
#coding:utf8

import sqlite3

def input(ip):
    conn = sqlite3.connect('ip.db')
    cursor = conn.cursor()
    sql = 'insert into ip(ip) values(?)'
    try:
        if cursor.execute(sql,(ip,)):
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except:
        return False



def output(ip):
    conn = sqlite3.connect('ip.db')
    cursor = conn.cursor()
    sql = 'delect * from ip where ip=?'
    try:
        if cursor.execute(sql,(ip,)):
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            return False
    except:
        return False