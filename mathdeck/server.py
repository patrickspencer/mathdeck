# -*- coding: utf-8 -*-

"""
mathdeck.server
~~~~~~~~~~~~~~~

An http server to communicate with mathdeck. This is to faciliate the
use of mathdeck with non-python programs.

:copyright: (c) 2014-2016 by Patrick Spencer.
:license: Apache 2.0, see LICENSE for more details.
"""

import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class GetProblemRequest(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        print('Got JSON data:', data)
        self.write({ 'got' : 'your data' })

def make_app():
    return tornado.web.Application([
        (r"/problem/", GetProblemRequest),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
