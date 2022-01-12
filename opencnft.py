#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import httpc as hc
import mysqlC as mc

rank_ = 'https://api.opencnft.io/1/rank'

rank_sql_insert_ = ''' INSERT INTO rank (name,volume,total_tx,total_assets,floor_price,volume_today,total_minted,total_owners) VALUES("%s",%s,%s,%s,%s,%s,%s,%s)
'''

rank_sql_delete_today = "delete from rank where  date(insert_date) = curdate()"


def process_json_rank(j_):
    for j in j_["ranking"]:
        str_sql = rank_sql_insert_ % (j["name"],j["volume"],j["total_tx"],j["total_assets"],j["floor_price"],j["volume_today"],j["total_minted"][0],j["total_owners"][0])
        print str_sql
        mc.exec_sql(str_sql)
        
        
def do_rank():
    jj = hc.curl_("GET",rank_)
    mc.exec_sql(rank_sql_delete_today)
    process_json_rank(jj)
    


if __name__ == "__main__":
    do_rank()
