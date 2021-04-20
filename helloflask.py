from flask import Flask
import myroutes

app = Flask(__name__, static_url_path='/static')
#adding routes
app.add_url_rule('/', view_func = myroutes.home)
app.add_url_rule('/compile/', view_func = myroutes.compile, methods=['POST'] )

if __name__ == '__main__':
    app.run()


