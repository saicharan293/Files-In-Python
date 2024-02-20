from flask import Flask, redirect, render_template, Request, request

app = Flask(__name__)
employees = [
    {"fname": "John", "lname": "Doe", "dob": "1990-01-01", "salary": 50000, "email": "john@example.com", "phone": 1234567890},
    {"fname": "Jane", "lname": "Smith", "dob": "1995-05-05", "salary": 60000, "email": "jane@example.com", "phone": 9876543210},
    {"fname": "Alice", "lname": "Johnson", "dob": "1985-08-15", "salary": 70000, "email": "alice@example.com", "phone": 1112223333}
]

@app.route('/')
def index():
    return render_template('index.html')


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
