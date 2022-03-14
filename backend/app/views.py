import json
from app import app, db
from flask import request, jsonify, make_response
from flask_restful import Resource
from app.models import Todo, TodoSchema

class TodosAPIView(Resource):
  def get(self):
    keywords = request.args.get('keywords', None)
    if keywords:
      todos = Todo.query.filter(Todo.title.contains(keywords))
    else:
      todos = Todo.query.all()

    schema = TodoSchema()
    response = jsonify([schema.dumps(todo) for todo in todos])    
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    
    return make_response(response)

  def post(self):
    data = request.get_json()

    if data:
      if len(data.get('title').split(' ')) < 10:
        return make_response({
          "code": 400,
          "message": "Todo has to be at least 10 characters long."
        }, 400)

      if len(data.get('title').split(' ')) > 100:
        return make_response({
          "code": 400,
          "message": "Todo cannot be greater that 100 characters long."
        }, 400)
      
      todo = Todo(**data)
      db.session.add(todo)
      db.session.commit()

      
      todos = Todo.query.all()
      schema = TodoSchema()
      response = jsonify([schema.dumps(todo) for todo in todos])    
      response.status_code = 201
      response.headers['Content-Type'] = 'application/json'

      return make_response(response, 201)
    return make_response({
      "code": 400,
      "message": "Bad request"
    }, 400)


class TodoAPIView(Resource):
  def get(self, id):
    todo = Todo.query.filter_by(id=id).first()
    return make_response(todo.to_dict())

  def put(self, id):
    data = request.get_json()
    todo = Todo.query.filter_by(id=id).first()
    todo.title = data.get('title', todo.title)
    todo.status = data.get('status', todo.status)
    db.session.add(todo)
    db.session.commit()

    return todo.to_dict(), 200

