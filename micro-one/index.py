from flask import Flask
from flask_restplus import Resource, Api, fields
from werkzeug.contrib.fixers import ProxyFix
from scraper import my_scraper


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='Our sample API',
          description='This is our sample API'
)

@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/hello_world2')
class HelloWorld(Resource):
    def get(self):
        return my_scraper()

if __name__ == '__main__':
    app.run(debug=True)