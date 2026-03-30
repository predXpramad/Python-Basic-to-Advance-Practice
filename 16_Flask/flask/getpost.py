## Get Post
from flask import Flask, render_template, request

# render_template is used to render HTML Web Pages

app=Flask(__name__)

@app.route("/")   # , methods = [''] give us get/post option
def welcome():
    return render_template('index1.html')  


@app.route("/about",methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET']) ## We use action = url(form here) to connect html form with link
def form():
    return render_template('form.html')

@app.route('/submit',methods=['POST']) ## We use action = url(form here) to connect html form with link
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'


if __name__ == "__main__":
    app.run(debug = True)