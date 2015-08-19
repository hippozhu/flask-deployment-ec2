from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from ksdservice import application

if __name__ == "__main__":
	http_server = HTTPServer(WSGIContainer(application))
	http_server.listen(5000)
	IOLoop.instance().start()