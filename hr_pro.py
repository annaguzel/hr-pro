import datetime
class Employee:
    def __init__(self,name,age,salary,employment_year):
        self.name= name
        self.age=age
        self.salary=salary
        self.employment_year=employment_year

    def get_working_years(self):
        today=datetime.datetime.today()

        return today.year-self.employment_year

class Manager(Employee):


    def __init__(self,name,age,salary,employment_year,bonus_percentage):

        self.bonus_percentage=bonus_percentage
        Employee.__init__(self, name, age, salary, employment_year)


    def get_bonus(self):
        return self.bonus_percentage * self.salary
    
def main():
    man_list=[]
    emp_list=[]
    bool=True
    print("Welcome to HR Pro2019")
    while bool:
        print('Options:\n  1. Show Employees\n  2.Show Managers\n  3.Add an Employee\n  4.Add a Manager\n  5.Exit')
        option =int(input("What would you like to do?"))
        if(option==1):
            if(len(emp_list)==0):
                print("Add Employees!")
            else:
                print("Employees:  ")
                for i in range(0, len(emp_list)):
                    print("Name: "+ emp_list[i].name+", Age: "+str(emp_list[i].age)+", Salary: "+ str(emp_list[i].salary)+", working Years: "+str(emp_list[i].get_working_years()))
                print("------------")
        elif(option==2):
            if (len(man_list)==0):
                print("Add Managers!")
            else:
                print("Managers  ")
                for i in range(0, len(man_list)):
                    print("Name: "+ man_list[i].name+", Age: "+str(man_list[i].age)+", Salary: "+ str(man_list[i].salary)+", working Years: "+str(man_list[i].get_working_years())+", Bonus: "+str(man_list[i].get_bonus()))
                print("------------")
        elif(option==3):
            name=input('Name: ')
            age=int(input('Age: '))
            salary=int(input("Salary: "))
            employment_year=int(input('Employment year: '))
            new_emp=Employee(name,age,salary,employment_year)
            emp_list.append(new_emp)


        elif(option==4):
            name=input('Name: ')
            age=input('Age: ')
            salary=int(input("Salary: "))
            employment_year=int(input('Employment year: '))
            bonus_percentage=float(input('Bonus Percentage: '))
            new_man=Manager(name,age,salary,employment_year,bonus_percentage)
            man_list.append(new_man)
        else:
            bool=False


if __name__ == '__main__':
	main()
