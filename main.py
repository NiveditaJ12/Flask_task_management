from flask import Flask, render_template, request, redirect, url_for,flash

from config import session, engine, Base
from models import ToDo

app= Flask(__name__)
app.secret_key = ['nivedita']
Base.metadata.bind = engine
Base.metadata.create_all(engine)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = ToDo(sr_no = request.form['sr_no'],task = request.form['new_task'], status=request.form['status'])
        print(new_todo)
        session.add(new_todo)
        session.commit()
    
    task = session.query(ToDo).all()
    return render_template('index.html', task=task)

@app.route('/delete/<id>')   
def delete(id):
    task = session.query(ToDo).filter(ToDo.id==id).first()
    session.delete(task)
    session.commit()
    all_todos = session.query(ToDo).all()
    for i,todo1 in enumerate(all_todos):
        todo1.sr_no = i+1
        session.add(todo1)
        session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<id>', methods = ['GET','POST'])   
def edit(id):
    task_update = session.query(ToDo).filter(ToDo.id==id).first()
    if task_update:
            task_update.task= request.form.get('updated_task') 
            task_update.status=request.form.get('updated_status')
            print(task_update.status)
            session.add(task_update)
            session.commit()
            return render_template('edit.html', id = task_update.id)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)