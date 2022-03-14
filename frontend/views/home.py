import json
import deform
import requests
import colander
from deform import Form
from pyramid.view import view_config


class TodoForm(colander.MappingSchema):
  title = colander.SchemaNode(colander.String(), 
                              validator=colander.Range(10, 100))

class FilterTodoForm(colander.MappingSchema):
  keywords = colander.SchemaNode(colander.String())

class Todos(colander.SequenceSchema):
  todo = TodoForm()

class FilterTodos(colander.SequenceSchema):
  todo = FilterTodoForm()

class Schema(colander.MappingSchema):
  todos = Todos()

class FilterSchema(colander.MappingSchema):
  todos = FilterTodos()

schema = Schema()
filter_schema = FilterSchema()
  
todoForm = Form(schema, buttons=('submit',))
filter_form = Form(filter_schema)

class TodoView:
  def __init__(self, request):
    self.request = request

  @property
  def todo_form(self):
    schema = TodoForm()
    return deform.Form(schema, buttons=('submit', ))

  @property
  def filter_todo_form(self):
    schema = TodoForm()
    return deform.Form(schema, buttons=('submit', ))

  @property
  def reqts(self):
    return self.todo_form.get_widget_resources()

  @view_config(route_name='home', renderer='templates/home/index.jinja2')
  def add_todo(self):
    form = self.todo_form.render()
    keywords = self.request.params.get('keywords', None)
    
    if keywords:
      response = requests.get('http://backend:8000/v1/todos?keywords={}'.format(keywords))
      if response.status_code > 200:
        return dict(error=True)
    else:
      response = requests.get('http://backend:8000/v1/todos')
      if response.status_code > 200:
        return dict(error=True)

    todos_list = [json.loads(todo) for todo in response.json()] 

    if 'submit' in self.request.POST:
      response = requests.post('http://backend:8000/v1/todos', json={
        'title': self.request.POST.get('title')
      })

      if response.status_code == 400:
        return dict(todos=todos_list, form=form, errors=response.json())

      if response.status_code == 201:
        return dict(todos=todos_list, form=form, errors=None, success=True)

    return dict(todos=todos_list, form=form, error=None)
