from flask import Flask, render_template


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/dataAnalyst')
def dataAnalyst():
    return render_template('dataAnalyst.html')

@app.route('/projectManager')
def projectManager():
    return render_template('projectManager.html')

if __name__=='__main__':
    app.run(debug=True)