from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False, default='Incompleto')


with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nueva_tarea_nombre = request.form.get('name')
        nueva_tarea = Todo(name=nueva_tarea_nombre)
        db.session.add(nueva_tarea)
        db.session.commit()

    lista_tareas = Todo.query.all()

    return render_template('select.html', lista_tareas=lista_tareas)

@app.route("/update/<id>")
def update(id):
    tarea = Todo.query.get(id)
    if tarea:
        tarea.state = 'Completo' if tarea.state == 'Incompleto' else 'Incompleto'
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/delete/<id>")
def delete(id):
    tarea = Todo.query.get(id)
    if tarea:
        db.session.delete(tarea)
        db.session.commit()
    return redirect(url_for('home'))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True)
