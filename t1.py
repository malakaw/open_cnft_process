#!/usr/bin/python2.7
#-*- coding: utf-8 -*-


import requests

def do_():
#    r = requests.post('https://httpbin.org/post', data={'key': 'value'})
    r = requests.get('https://api.opencnft.io/1/rank')
    j_obj = r.json()
    print j_obj
    
if __name__ == "__main__":
    do_()
