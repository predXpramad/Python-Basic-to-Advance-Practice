from flask import Flask

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

# / -> Home page
@app.route("/")
def hi():
    return "I'm learning Flask Now...."

@app.route("/index")
def index():
    return "This Just an index page"

# In any python file the execution starts from here only.
if __name__=="__main__":
    app.run(debug=True) # debug = true allows me to restart code with maually stoping and then running code.