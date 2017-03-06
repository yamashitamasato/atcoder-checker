# -*- coding:utf-8 -*-
#Copyright © 2017 山下正人. All rights reserved.

import os
import websc
from bottle import route, run,template
from bottle import get, post,request
import requests
from bottle import static_file
import asy

@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./views/static/js')


@route('/fonts/<filename>')
def fonts_static(filename):
    return static_file(filename, root='./views/static/fonts')


@route('/css/<filename>')
def css_static(filename):
    return static_file(filename, root='./views/static/css')
@route('/', method='GET')
def input():
    input_txt = request.query.get('user')
    #GETで何も渡されていない時はinput_txtに何も入れない
    input_txt = "" if input_txt is None else input_txt
    return template('html',input_txt=input_txt)

@route('/', method='POST')
def do_echo():
    input_txt = request.forms.get('input_txt')
    scoreB,scoreG,scoreR,scoreT=asy.start(input_txt)
    return template('table',scoreB=scoreB,scoreG=scoreG,scoreR=scoreR,scoreT=scoreT,input_txt=input_txt)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)),debug=True)
