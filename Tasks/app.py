from flask import Flask, redirect, render_template, Request, request

app = Flask(__name__)
listing=[]

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
    listing.append({'fname':fname,'lname':lname,'dob':dob,"salary":salary,'email':email,'phone':phone})
    return redirect('/display')

@app.route('/display')
def display_employees():
    # Assuming 'listing' contains enrolled employee details
    # Fetch or define 'listing' variable containing employee details
    return render_template('display.html', listing=listing)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_field = request.form['search_field']
        search_term = request.form['search_term']
    else:  # If method is GET
        search_field = request.args.get('search_field')
        search_term = request.args.get('search_term')
    search_results = []
    for employee in listing:
        if str(employee.get(search_field)) == search_term:
            search_results.append(employee)
    return render_template('search.html', search=search_results)
    
@app.route('/sort')
def sorting():
    option = request.args.get('option')
    if option:
        sorted_list= sorted(listing, key=lambda x: x[option])
    else:
        sorted_list= listing
    # sorted_list=sort_employees(option)
    return render_template('display.html', listing=sorted_list)

@app.route('/reset')
def reset():
    return render_template('display.html',listing=listing)
    
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
