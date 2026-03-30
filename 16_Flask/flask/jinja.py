from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/") 
def welcome():
    """
    Renders the main input form.
    File: templates/index1.html
    """
    return render_template('index1.html')  

@app.route("/about", methods=['GET'])
def about():
    """Renders a simple about page."""
    return render_template('about.html')

@app.route('/success/<int:score>')
def success(score):
    """Simple Pass/Fail check based on an integer score."""
    res = "Passed" if score >= 50 else "Failed"
    return render_template('result.html', results=res)

@app.route('/test/<int:score>')
def test(score):
    """Pass/Fail check returning a dictionary object to the template."""
    res = "Passed" if score >= 50 else "Failed"
    exp = {'score': score, "res": res}
    return render_template('result1.html', results=exp)

@app.route('/checkif/<int:score>')
def checkif(score):
    """
    Displays the final calculated score.
    Note: The <int:score> rule requires a whole number.
    """
    return render_template('result2.html', scores=score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    """
    Processes form data from index1.html.
    1. Collects marks for 4 subjects.
    2. Calculates the average.
    3. Redirects to the 'checkif' route.
    """
    if request.method == 'POST':
        # Extract values from form 'name' attributes
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        
        # Calculate average and convert to INT to match the checkif route type
        total_score = int((science + maths + c + datascience) / 4)
    else:
        return render_template('getresults.html')
        
        # Dynamically build the URL for the 'checkif' function
    return redirect(url_for('checkif', score=total_score))
    
    # If accessed via GET (typing /submit in URL), redirect back to home form
    

if __name__ == "__main__":
    # debug=True allows for auto-reloading when code changes
    app.run(debug=True)
