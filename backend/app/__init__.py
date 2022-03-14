from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


from app import views, models


api.add_resource(views.TodosAPIView, '/v1/todos')
api.add_resource(views.TodoAPIView, '/v1/todos/<id>')