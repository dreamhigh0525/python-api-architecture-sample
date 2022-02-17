#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, List
import re
import sqlite3


def parse_log(log_path: str) -> List[Any]:
    # '2020-11-10 18:44:54,038 [INFO] ::testid http://localhost/test_image.jpg 1       1.0'
    pattern = '.*\[INFO\] ::(.*)\t(.*)\t(.*)\t(.*)\t(.*)$'
    repattern = re.compile(pattern)
    with open(log_path, 'r') as f:
        lines = f.readlines()

    records = []
    for line in lines:
        result = repattern.match(line.rstrip('\n'))
        if result is not None:
            aid, category, url, label, confidence = result.groups()
            records.append((aid, category, url, int(label), float(confidence)))

    return records


def regist_data(db_path: str, records: List[Any]) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
    INSERT INTO inference(id, category, url, label, confidence)
    VALUES(?,?,?,?,?)
    '''
    cur.executemany(sql, records)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    log_path = 'logs/access.log'
    records = parse_log(log_path)
    regist_data('inference.db', records)
