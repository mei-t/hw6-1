#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import jinja2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainPage(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(u'好きな言葉を2つ入力してください！') #「好きな言葉を2つ入力してください」と表示
        self.render('main.html') #その下にmain.htmlの内容を表示

    def post(self):
        word1 = self.request.get('word1')
        word2 = self.request.get('word2')
        if word1 is None or word2 is None:
            self.redict('/')

        pata = ""      #パタトクカシー作成
        for i in range(min(len(word1), len(word2))):
            pata = pata + word1[i] + word2[i]
        if len(word1) < len(word2):
            pata += word2[len(word1):]
        elif len(word1) > len(word2):
            pata += word1[len(word2):]

        self.response.write(word1 +u' + ' + word2 + u' =  ' + pata) #結果表示
        
        self.response.write(u'<br>もう一度、好きな言葉を2つ入力してください！') #「もう一度、好きな言葉を2つ入力してください」と表示

        self.render('main.html')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
