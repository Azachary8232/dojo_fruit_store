from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "skittles"  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['strawberry_count'] = request.form['strawberry']
    session['blackberry_count'] = request.form['blackberry']
    session['raspberry_count'] = request.form['raspberry']
    session['apple_count'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_zachary'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['count'] = int(session['strawberry_count']) + int(session['blackberry_count']) + int(session['raspberry_count']) + int(session['apple_count'])
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    