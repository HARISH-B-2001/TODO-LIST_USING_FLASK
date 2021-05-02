from flask import Flask, render_template,url_for,request,redirect
from db_functions import add_new_task,get_incomplete_task,get_complete_task,mark_task_complete, mark_task_undo,clear_task


app = Flask(__name__,
    template_folder='templates'
    )

@app.route('/')
def index():
    complete = get_complete_task()
    incomplete = get_incomplete_task()
    return render_template('index.html', complete=complete, incomplete=incomplete)

@app.route('/add', methods=["POST"])
def add():
    task = request.form["todoitem"]
    add_new_task(task)
    return redirect(url_for('index'))

@app.route('/complete/<task>')
def complete(task):
    mark_task_complete(task)
    return redirect(url_for('index'))

@app.route('/undo/<task>')
def undo(task):
    mark_task_undo(task)
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    clear_task()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
