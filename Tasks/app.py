from flask import Flask, render_template, request
from flask_paginate import get_page_args,Pagination

# employees=[
#     {"fname": "Emily", "lname": "Davis", "dob": "1993-11-10", "salary": 62000, "email": "emily@example.com", "phone": 9998887777},
#     {"fname": "William", "lname": "Miller", "dob": "1987-07-25", "salary": 72000, "email": "william@example.com", "phone": 2223334444},
#     {"fname": "Sophia", "lname": "Wilson", "dob": "1992-04-15", "salary": 58000, "email": "sophia@example.com", "phone": 7776665555},
#     {"fname": "James", "lname": "Taylor", "dob": "1984-09-05", "salary": 65000, "email": "james@example.com", "phone": 3335557777},
#     {"fname": "Olivia", "lname": "Martinez", "dob": "1989-12-30", "salary": 71000, "email": "olivia@example.com", "phone": 8887776666},
#     {"fname": "Benjamin", "lname": "Hernandez", "dob": "1991-06-18", "salary": 59000, "email": "benjamin@example.com", "phone": 4446668888},
#     {"fname": "Ethan", "lname": "Young", "dob": "1986-02-12", "salary": 68000, "email": "ethan@example.com", "phone": 6669993333},
#     {"fname": "Isabella", "lname": "Garcia", "dob": "1994-10-08", "salary": 73000, "email": "isabella@example.com", "phone": 3337779999},
#     {"fname": "Daniel", "lname": "Lopez", "dob": "1983-08-22", "salary": 60000, "email": "daniel@example.com", "phone": 7779991111}
# ]
employees=[]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',employees=employees)






@app.route('/submit',methods=['POST'])
def submit():
    fname=request.form['fname']
    lname=request.form['lname']
    dob=request.form['dob']
    salary=request.form['salary']
    email=request.form['email']
    phone=request.form['phone']
    employees.append({'fname':fname,'lname':lname,'dob':dob,"salary":salary,'email':email,'phone':phone})
    return render_template('index.html',employees=employees)


@app.route('/search',methods=['POST'])
def search():
    search_field = request.form['search_field']
    search_term = request.form['search_term'].lower()
    search_results = []
    for employee in employees:
        if  search_term in str(employee.get(search_field).lower()):
            search_results.append(employee)
    return render_template('index.html', employees=search_results)

@app.route('/sort')
def sorting():
    option = request.args.get('option')
    if option:
        sorted_list= sorted(employees, key=lambda x: x[option])
    else:
        sorted_list= employees
    return render_template('index.html', employees=sorted_list)

@app.route('/reset')
def reset():
    return render_template('index.html',employees=employees)
    


if __name__ == '__main__':
    app.run(debug=True)
