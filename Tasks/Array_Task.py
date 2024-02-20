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