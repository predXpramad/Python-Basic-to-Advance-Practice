## Integrating HTML
from flask import Flask, render_template
# render_template is used to render HTML Web Pages

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index1.html')


@app.route("/about")
def about_us():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug = True)