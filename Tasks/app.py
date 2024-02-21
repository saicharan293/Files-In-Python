from flask import Flask, render_template, request
from flask_paginate import get_page_args,Pagination

app = Flask(__name__)
employees = [ ]
length=len(employees)
users=list(range(100))

# def add_employee(fname, lname, dob, salary, email, phone):
#     employees.append({'fname': fname, 'lname': lname, 'dob': dob, "salary": salary, 'email': email, 'phone': phone})

def get_users(offset=0, per_page=5):
    return employees[offset: offset + per_page]
@app.route('/',methods=['POST','GET'])
def index():
    global employees
    page,_ ,offset=get_page_args(page_parameter="page",per_page_parameter="per_page")
    total = len(employees)
    per_page = 6  # Change per_page as desire

        # Check if the total number of employees is divisible evenly by per_page
    if offset >= total:
        # If so, reset offset to the last page
        offset = total - (total % per_page)

    total = len(employees)
    print("total is ",total)
          # Update the total after adding the new employee

    pagination_employees = get_users(offset=offset, per_page=per_page)

    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('index.html', employees=pagination_employees,
                           page=page, per_page=per_page, pagination=pagination)


@app.route('/submit',methods=['POST'])
def submit():
    fname=request.form['fname']
    lname=request.form['lname']
    dob=request.form['dob']
    salary=int(request.form['salary'])
    email=request.form['email']
    phone=int(request.form['phone'])
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
    
    # return render_template('form.html', result=listing)


# @app.route('/highest-salary')
# def highest_salary():
#     num_high = int(request.args.get('num_high'))
#     result = nth_salary(num_high)
#     return render_template('form.html', result=listing)

# @app.route('/dob-range')
# def dob_range():
#     start = request.args.get('start')
#     end = request.args.get('end')
#     result = dob_in_employees(start, end)
#     return render_template('form.html', result=listing)

if __name__ == '__main__':
    app.run(debug=True)
