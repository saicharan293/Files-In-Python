import datetime 

listing=[]

records=int(input("how many records "))

def save_dict(fname,lname,dob,salary,email,phone):  
    dict={'fname':fname,'lname':lname,'dob':dob,'salary':salary,"email":email,"phone":phone}
    listing.append(dict)

def add_employee():
    count=0
    for i in range(records):
        fname=input("enter fname: ")
        lname=input('enter lname: ')
        dob=input("Enter dob: ")
        salary=int(input("enter salary: "))
        email=input("Enter email: ")
        phone=int(input("Enter mobile number: "))
        count+=1
        print(f"---{count} insertion(s) completed---")
        save_dict(fname,lname,dob,salary,email,phone)

# print(type(list_employees))

def Display_employees(listing):
    for emp in listing:
        print(emp)


def Search_Employee(word):
    for outer in listing:
          for key,value in outer.items():
            if isinstance(value,str) and str(word) in value:
                print(outer)
                break
            elif isinstance(value,int) and value==word:
                print(outer)
                break

def sort_employees(option):
    
    sorted_list=sorted(listing,key=lambda x: x[option])
    for person in sorted_list:
      print(person)


def nth_salary(num_high):
    salary_spotted=sorted(listing,key=lambda x: x['salary'])
    count=1
    for i in salary_spotted:
        if count==num_high:
            print(i)
            break
        count+=1



def dob_in_employees(start,end):
    start_date=datetime.datetime.strptime(start,'%Y-%m-%d')
    end_date=datetime.datetime.strptime(end,'%Y-%m-%d')
    
    #list comprehension along with lambda function

    filetered_list=[employee for employee in listing if start_date<=datetime.datetime.strptime(employee['dob'],'%Y-%m-%d')<=end_date]

    sorted_employees=sorted(filetered_list,key=lambda x: x['dob'] )

    for employee in sorted_employees:
        print(employee)
    


# Search the function based on the inputs given by the user
# print fname, lname, email, phone, dob, salary
# sort_employees('salary')
# print('-'*10)
# nth_salary(3)

def main():
    Display_employees(listing)
    while listing:
        print('Choose the options to begin the search based on below options ')
        print('1.Search \n2.Sort \n3.dob \n4.nth highest salary \n5.end')
        enter=int(input())
        try:
            if enter == 1:
                user_input = input("Search based on: ?  ")
                Search_Employee(user_input)
            elif enter == 2:
                user_choice = input('Sort the values based on: ? ')
                sort_employees(user_choice)
            elif enter == 3:
                print("sort out the employees between given dates below")
                start = input("Enter the starting date in 'YYYY-mm-dd' format ")
                end = input("Enter the ending date in 'YYYY-mm-dd' format ")
                dob_in_employees(start, end)
            elif enter == 4:
                high = int(input("Enter the highest place of salary "))
                nth_salary(high)
            elif enter == 5:
                add_employee()
                Display_employees(listing)
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid choice")

main()

# listing_keys = listing[0].keys()
    # print(list(listing_keys))
    # user_input=input("your option is: ?  ")
    # Search_Employee(user_input)

    # print('Provide the user choice to sort the list from the below options ')
    # listing_keys = listing[0].keys()
    # print(list(listing_keys))
    
    # user_input=input("your option is: ?  ")
    # user_choice=input()

    # sort_employees(user_choice)
    # print('-'*10)
    # sort_employees('dob')
    # print("sort out the employees between given dates below")
    # start=input("Enter the starting date in 'YYYY-mm-dd' format ")
    # end=input("Enter the ending date in 'YYYY-mm-dd' format ")
    # dob_in_employees(start,end)

    # high=int(input("Enter the highest place of salary "))
    # nth_salary(high)
#    {"fname": "Emily", "lname": "Davis", "dob": "1993-11-10", "salary": 62000, "email": "emily@example.com", "phone": 9998887777},
#     {"fname": "William", "lname": "Miller", "dob": "1987-07-25", "salary": 72000, "email": "william@example.com", "phone": 2223334444},
#     {"fname": "Sophia", "lname": "Wilson", "dob": "1992-04-15", "salary": 58000, "email": "sophia@example.com", "phone": 7776665555},
#     {"fname": "James", "lname": "Taylor", "dob": "1984-09-05", "salary": 65000, "email": "james@example.com", "phone": 3335557777},
#     {"fname": "Olivia", "lname": "Martinez", "dob": "1989-12-30", "salary": 71000, "email": "olivia@example.com", "phone": 8887776666},
#     {"fname": "Benjamin", "lname": "Hernandez", "dob": "1991-06-18", "salary": 59000, "email": "benjamin@example.com", "phone": 4446668888},
#     {"fname": "Ethan", "lname": "Young", "dob": "1986-02-12", "salary": 68000, "email": "ethan@example.com", "phone": 6669993333},
#     {"fname": "Isabella", "lname": "Garcia", "dob": "1994-10-08", "salary": 73000, "email": "isabella@example.com", "phone": 3337779999},
#     {"fname": "Daniel", "lname": "Lopez", "dob": "1983-08-22", "salary": 60000, "email": "daniel@example.com", "phone": 7779991111}
# headings=['fname','lname','dob','salary','email','phone']
# data=[['sai','charan','2000-03-02',20000,'sai@co.com',1112223333],
#       ['emily','davis','1990-05-05',30000,'emily@co.com',2223334444],
#       ['Miller','David','1987-09-09',50000,'miller@co.com',3334445555]]


# global employees
    # page,_ ,offset=get_page_args(page_parameter="page",per_page_parameter="per_page")
    # total = len(employees)
    # per_page = 6  
    # if offset >= total:
    #     offset = total - (total % per_page)
    # total = len(employees)
    # print("total is ",total)

    # pagination_employees = get_users(offset=offset, per_page=per_page)

    # pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    # return render_template('index.html', employees=pagination_employees,
    #                        page=page, per_page=per_page, pagination=pagination)

# @app.route('/')
# def index():
#     page,per_page,offset=get_page_args(page_parameter='page',per_page_parameter='per_page')
   
#     total=8
#     pagination_users=get_users(offset=offset,per_page=6)
#     pagination=Pagination(page=page,per_page=6,total=total,css_framework='bootstrap4')
#     return render_template('index.html',
#                            employees=pagination_users,
#                            page=page,
#                            per_page=per_page,
#                            pagination=pagination)

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
# def get_users(offset=0, per_page=6):
#     return employees[offset: offset + per_page]
# <!-- <table>
#             <thead>
#               <tr>
#                 <th><a href="/sort?option=fname">First name</a></th>
#                 <th>Value</th>
#               </tr>
#             </thead>
#             <tbody>
#               {% for user in users %}
#               <tr>
#                 <td>
#                   {{loop.index + (page-1)* per_page}}
#                 </td>
#                 <td>
#                   {{user}}
#                 </td>
#               </tr>
#               {% endfor %}
#             </tbody>
#           </table> -->
employees = [
    {"fname": "Emily", "lname": "Davis", "dob": "1993-11-10", "salary": 62000, "email": "emily@example.com", "phone": 9998887777},
    {"fname": "William", "lname": "Miller", "dob": "1987-07-25", "salary": 72000, "email": "william@example.com", "phone": 2223334444},
    {"fname": "Olivia", "lname": "Brown", "dob": "1990-05-15", "salary": 58000, "email": "olivia@example.com", "phone": 3334445555},
    {"fname": "James", "lname": "Wilson", "dob": "1985-02-20", "salary": 65000, "email": "james@example.com", "phone": 4445556666},
    {"fname": "Sophia", "lname": "Taylor", "dob": "1995-08-30", "salary": 55000, "email": "sophia@example.com", "phone": 5556667777},
    {"fname": "Michael", "lname": "Anderson", "dob": "1988-04-05", "salary": 70000, "email": "michael@example.com", "phone": 6667778888},
    {"fname": "Emma", "lname": "Thomas", "dob": "1992-09-12", "salary": 60000, "email": "emma@example.com", "phone": 7778889999},
    {"fname": "Alexander", "lname": "Jackson", "dob": "1984-12-17", "salary": 68000, "email": "alexander@example.com", "phone": 8889990000},
    {"fname": "Isabella", "lname": "White", "dob": "1989-06-22", "salary": 54000, "email": "isabella@example.com", "phone": 9990001111},
    {"fname": "Ethan", "lname": "Harris", "dob": "1991-01-27", "salary": 63000, "email": "ethan@example.com", "phone": 1112223333},
    {"fname": "Mia", "lname": "Martin", "dob": "1986-03-03", "salary": 59000, "email": "mia@example.com", "phone": 2223334444},
    {"fname": "Daniel", "lname": "Thompson", "dob": "1994-07-08", "salary": 67000, "email": "daniel@example.com", "phone": 3334445555},
    {"fname": "Charlotte", "lname": "Garcia", "dob": "1983-10-13", "salary": 56000, "email": "charlotte@example.com", "phone": 4445556666},
    {"fname": "Liam", "lname": "Martinez", "dob": "1996-05-18", "salary": 64000, "email": "liam@example.com", "phone": 5556667777},
    {"fname": "Ava", "lname": "Robinson", "dob": "1981-11-23", "salary": 53000, "email": "ava@example.com", "phone": 6667778888},
    {"fname": "Matthew", "lname": "Clark", "dob": "1982-06-28", "salary": 69000, "email": "matthew@example.com", "phone": 7778889999},
    {"fname": "Amelia", "lname": "Rodriguez", "dob": "1997-02-02", "salary": 57000, "email": "amelia@example.com", "phone": 8889990000},
    {"fname": "Benjamin", "lname": "Lewis", "dob": "1980-08-07", "salary": 66000, "email": "benjamin@example.com", "phone": 9990001111},
    {"fname": "Harper", "lname": "Lee", "dob": "1985-04-12", "salary": 62000, "email": "harper@example.com", "phone": 1112223333},
    {"fname": "Elijah", "lname": "Walker", "dob": "1993-09-17", "salary": 71000, "email": "elijah@example.com", "phone": 2223334444},
    {"fname": "Elizabeth", "lname": "Perez", "dob": "1990-03-22", "salary": 57000, "email": "elizabeth@example.com", "phone": 3334445555},
    {"fname": "Lucas", "lname": "Hall", "dob": "1986-07-27", "salary": 70000, "email": "lucas@example.com", "phone": 4445556666},
    {"fname": "Avery", "lname": "Young", "dob": "1991-12-02", "salary": 53000, "email": "avery@example.com", "phone": 5556667777},
    {"fname": "Grace", "lname": "Scott", "dob": "1984-10-07", "salary": 67000, "email": "grace@example.com", "phone": 6667778888},
    {"fname": "Oliver", "lname": "Green", "dob": "1989-05-12", "salary": 68000, "email": "oliver@example.com", "phone": 7778889999},
    {"fname": "Chloe", "lname": "Adams", "dob": "1987-01-17", "salary": 56000, "email": "chloe@example.com", "phone": 8889990000},
    {"fname": "Sebastian", "lname": "Baker", "dob": "1992-06-22", "salary": 69000, "email": "sebastian@example.com", "phone": 9990001111},
    {"fname": "Lily", "lname": "Gonzalez", "dob": "1983-12-27", "salary": 59000, "email": "lily@example.com", "phone": 1112223333},
    {"fname": "Jackson", "lname": "Nelson", "dob": "1988-07-02", "salary": 71000, "email": "jackson@example.com", "phone": 2223334444},
    {"fname": "Penelope", "lname": "Carter", "dob": "1995-11-07", "salary": 54000, "email": "penelope@example.com", "phone": 3334445555},
    {"fname": "Gabriel", "lname": "Mitchell", "dob": "1982-04-12", "salary": 65000, "email": "gabriel@example.com", "phone": 4445556666},
    {"fname": "Madison", "lname": "Perez", "dob": "1994-09-17", "salary": 60000, "email": "madison@example.com", "phone": 5556667777},
    {"fname": "Logan", "lname": "Roberts", "dob": "1980-01-22", "salary": 72000, "email": "logan@example.com", "phone": 6667778888},
    {"fname": "Aria", "lname": "Cook", "dob": "1986-06-27", "salary": 55000, "email": "aria@example.com", "phone": 7778889999},
    {"fname": "Grayson", "lname": "Morgan", "dob": "1991-12-02", "salary": 67000, "email": "grayson@example.com", "phone": 8889990000},
    {"fname": "Sofia", "lname": "Flores", "dob": "1984-11-07", "salary": 58000, "email": "sofia@example.com", "phone": 9990001111},
    {"fname": "Riley", "lname": "Garcia", "dob": "1992-05-12", "salary": 66000, "email": "riley@example.com", "phone": 1112223333},
    {"fname": "David", "lname": "Reed", "dob": "1988-10-17", "salary": 69000, "email": "david@example.com", "phone": 2223334444},
    {"fname": "Zoe", "lname": "Sanchez", "dob": "1996-02-22", "salary": 57000, "email": "zoe@example.com", "phone": 3334445555},
    {"fname": "Carter", "lname": "Scott", "dob": "1981-08-27", "salary": 70000, "email": "carter@example.com", "phone": 4445556666},
    {"fname": "Hannah", "lname": "Lee", "dob": "1983-03-03", "salary": 59000, "email": "hannah@example.com", "phone": 5556667777},
    {"fname": "Luke", "lname": "Adams", "dob": "1994-07-08", "salary": 68000, "email": "luke@example.com", "phone": 6667778888},
    {"fname": "Aubrey", "lname": "Parker", "dob": "1990-10-13", "salary": 53000, "email": "aubrey@example.com", "phone": 7778889999},
    {"fname": "Daniel", "lname": "Wright", "dob": "1985-05-18", "salary": 71000, "email": "daniel@example.com", "phone": 8889990000},
    {"fname": "Penelope", "lname": "Carter", "dob": "1995-11-07", "salary": 54000, "email": "penelope@example.com", "phone": 3334445555},
    {"fname": "Gabriel", "lname": "Mitchell", "dob": "1982-04-12", "salary": 65000, "email": "gabriel@example.com", "phone": 4445556666},
    {"fname": "Madison", "lname": "Perez", "dob": "1994-09-17", "salary": 60000, "email": "madison@example.com", "phone": 5556667777},
    {"fname": "Logan", "lname": "Roberts", "dob": "1980-01-22", "salary": 72000, "email": "logan@example.com", "phone": 6667778888},
    {"fname": "Aria", "lname": "Cook", "dob": "1986-06-27", "salary": 55000, "email": "aria@example.com", "phone": 7778889999},
    {"fname": "Grayson", "lname": "Morgan", "dob": "1991-12-02", "salary": 67000, "email": "grayson@example.com", "phone": 8889990000},
    {"fname": "Sofia", "lname": "Flores", "dob": "1984-11-07", "salary": 58000, "email": "sofia@example.com", "phone": 9990001111},
    {"fname": "Riley", "lname": "Garcia", "dob": "1992-05-12", "salary": 66000, "email": "riley@example.com", "phone": 1112223333},
    {"fname": "David", "lname": "Reed", "dob": "1988-10-17", "salary": 69000, "email": "david@example.com", "phone": 2223334444},
    {"fname": "Zoe", "lname": "Sanchez", "dob": "1996-02-22", "salary": 57000, "email": "zoe@example.com", "phone": 3334445555},
    {"fname": "Carter", "lname": "Scott", "dob": "1981-08-27", "salary": 70000, "email": "carter@example.com", "phone": 4445556666},
    {"fname": "Hannah", "lname": "Lee", "dob": "1983-03-03", "salary": 59000, "email": "hannah@example.com", "phone": 5556667777},
    {"fname": "Luke", "lname": "Adams", "dob": "1994-07-08", "salary": 68000, "email": "luke@example.com", "phone": 6667778888},
    {"fname": "Aubrey", "lname": "Parker", "dob": "1990-10-13", "salary": 53000, "email": "aubrey@example.com", "phone": 7778889999},
    {"fname": "Daniel", "lname": "Wright", "dob": "1985-05-18", "salary": 71000, "email": "daniel@example.com", "phone": 8889990000}
]