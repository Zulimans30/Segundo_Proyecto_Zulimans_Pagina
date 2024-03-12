"""Run server config"""
from flask import Flask
from app import index_routes

app = Flask(__name__)
app.register_blueprint(index_routes.index)



if __name__ == '__main__':
    app.run(debug=True)
