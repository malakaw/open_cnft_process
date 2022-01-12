#!/usr/bin/python2.7
#-*- coding: utf-8 -*-


import requests

def curl_(meth,url):
#    r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    r = requests.get('https://api.opencnft.io/1/rank')
    return r.json()

    
if __name__ == "__main__":
    rank_ = 'https://api.opencnft.io/1/rank'
    curl_("GET",rank_)
   
