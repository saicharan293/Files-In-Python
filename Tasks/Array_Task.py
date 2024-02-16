import datetime 

listing=[]

records=int(input("how many records "))

def save_dict(fname,lname,dob,salary,email,phone):  
    dict={'fname':fname,'lname':lname,'dob':dob,'salary':salary,"email":email,"phone":phone}
    listing.append(dict)

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


def Searh_Employees(word):
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
    
    #list comprehension

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
    while listing:
        print('Choose the options to begin the search based on below options ')
        print('1.Search \n2.Sort \n3.dob \n4.nth highest salary \n5.end')
        enter=int(input())
        try:
            match(enter):
                case 1:
                    user_input=input("Search based on: ?  ")
                    Searh_Employees(user_input)
                case 2:
                    user_choice=input('Sort the values based on: ? ')
                    sort_employees(user_choice)
                case 3:
                    print("sort out the employees between given dates below")
                    start=input("Enter the starting date in 'YYYY-mm-dd' format ")
                    end=input("Enter the ending date in 'YYYY-mm-dd' format ")
                    dob_in_employees(start,end)
                case 4:
                    high=int(input("Enter the highest place of salary "))
                    nth_salary(high)
                case 5:
                    break
        except:
            raise print("Invalid choice")

main()

# listing_keys = listing[0].keys()
    # print(list(listing_keys))
    # user_input=input("your option is: ?  ")
    # Searh_Employees(user_input)

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
