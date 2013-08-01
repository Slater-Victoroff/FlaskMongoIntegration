from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "Mongo_Integration_Demo"}
app.config["SECRET_KEY"] = "InsecurePassword"

def register_blueprints(app):
    from MongoIntegration.views import clothes
    app.register_blueprint(clothes)

register_blueprints(app)
db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

