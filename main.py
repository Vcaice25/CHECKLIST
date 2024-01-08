# Libreria para rel uso de Flask
from flask import Flask, render_template, request

# Librerias para el uso de la base de datos
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


app = Flask (__name__)

#Configuro parametro SQLALCHEMY_DATABASE_URI con la ubicacion de la bd
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.squite"

db = SQLAlchemy (app)

# Crear la Tabla
class Todo(db.Model):
    id:Mapped[int] = mapped_column(db.Integer, primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(db.String,nullable=False)
    state:Mapped[str] = mapped_column(db.Float,nullable=False,default= 'Incompleto')

#Crear la base y las tablas necesarias con el contexto de la aplicacion
with app. app_context():
    db. create_all()

#Rutas de la aplicacion
@app.route( "/", methods=['GET','POST'])
def home():
      if request.method == 'POST':
           return f' quieres agregar algo?'

@app.route("/insert")
def insert():
       return f'PRUEBA CKECK LIST'

@app.route("/update/<id>")
def update(id):
       return f'PRUEBA CKECK LIST MODIFICAR EL ID {id}'

@app.route("/delete/<id>")
def delete(id):
       return f'PRUEBA CKECK LIST ELIMINAR EL ID {id}'


  
if __name__ == '__main__':
      app.run(debug=True)
