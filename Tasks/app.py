from flask import Flask, redirect, render_template, request

app = Flask(__name__)
employee_list=[]

@app.route('/')
def index():
    return render_template('index.html',employee_list=employee_list)


@app.route('/submit',methods=['POST'])
def submit():
    fname=request.form['fname']
    lname=request.form['lname']
    dob=request.form['dob']
    salary=int(request.form['salary'])
    email=request.form['email']
    phone=int(request.form['phone'])
    employee_list.append({'fname':fname,'lname':lname,'dob':dob,"salary":salary,'email':email,'phone':phone})
    return redirect('/#enrolled')


@app.route('/search', methods=['POST'])
def search():
    # search_field = request.form['search_field']
    search_term = request.form['search_term']
    search_results = []
    for employee in employee_list:
        if any(search_term in str(value).lower() for value in employee.values()):
            search_results.append(employee)
    return render_template('index.html', employee_list=search_results)
    
@app.route('/sort')
def sorting():
    option = request.args.get('option')
    if option:
        sorted_list= sorted(employee_list, key=lambda x: x[option])
    else:
        sorted_list= employee_list
    # sorted_list=sort_employees(option)
    return render_template('index.html', employee_list=sorted_list)

@app.route('/reset')
def reset():
    return render_template('index.html',employee_list=employee_list)

# @app.route('/')
    
    # return render_template('form.html', result=employee_list)


# @app.route('/highest-salary')
# def highest_salary():
#     num_high = int(request.args.get('num_high'))
#     result = nth_salary(num_high)
#     return render_template('form.html', result=employee_list)

# @app.route('/dob-range')
# def dob_range():
#     start = request.args.get('start')
#     end = request.args.get('end')
#     result = dob_in_employees(start, end)
#     return render_template('form.html', result=employee_list)

if __name__ == '__main__':
    app.run(debug=True)
