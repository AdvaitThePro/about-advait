from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new index.html')

@app.route('/secser')
def secser():
    return render_template('secser.html')

@app.route('/accser')
def accser():
    return render_template('accser.html')

@app.route('/taxser')
def taxser():
    return render_template('taxser.html')

if __name__ == '__main__':
    app.run(debug=True)
