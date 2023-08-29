from flask import Flask, request, make_response, render_template, redirect, url_for
from csv import writer

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        uniqname = request.form['uniqname']
        grade = request.form['grade']
        with open('signups.csv', 'a') as f:
            w_o = writer(f)
            w_o.writerow([first_name, last_name, uniqname, grade])
        return render_template('signup.html')
    else:
       return render_template('signup.html')

# @app.route('/add_user/', methods=["POST"])
# def add_user():
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     uniqname = request.form['uniqname']
#     grade = request.form['grade']
#     with open('signups.csv', 'a') as f:
#         w_o = writer(f)
#         w_o.writerow([first_name, last_name, uniqname, grade])
#     return redirect("/", code="200")