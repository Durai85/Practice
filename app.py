from flask import Flask, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def home():
    page = ""

    for i,t in enumerate(tasks):
        page += f"{t} <a href='/del/{i}'> X </a><br>"

    page += """
        <form method='POST' action='/add'>
            <input name='task'>
            <button>Add</button>
        </form>
    """

    return page

@app.route('/add', methods=['POST'])
def add():
    tasks.append(request.form['task'])
    return redirect('/')

@app.route('/del/<int:i>')
def delete(i):
    if i < len(tasks):
        tasks.pop(i)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
