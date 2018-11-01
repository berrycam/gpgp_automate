# -*- coding: utf-8 -*-
'''
Created on 2018.10.19

@author: chenaimei
'''

import csv


def get_data_cvs(filename):
    users = []
    with open(filename, 'r', encoding='ISO-8859-15') as f:
        rows = csv.reader((line.replace('\0','') for line in f))
        # 第1行是标题，直接跳过
        next(rows)
        for row in rows:
            users.append(row)
    return users
    