from app import db, ma
from flask import jsonify
from datetime import datetime

class Todo(db.Model):
  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  status = db.Column(db.Boolean)

  def __repr__(self):
        return '<TODO {}>'.format(self.title)


  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'status': self.status,
    }

class TodoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Todo

    id = ma.auto_field()
    title = ma.auto_field()
    status = ma.auto_field()