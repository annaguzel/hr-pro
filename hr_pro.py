import datetime
class Employee:
    def __init__(self,name,age,salary,employment_year,**kwargs):
        self.name= name
        self.age=age
        self.salary=salary
        self.employment_year=employment_year

    def get_working_years(self):
        today=datetime.datetime.today()
        years=today.year-self.employment_year
        return years
    def __str__(self):
        years=str(self.get_working_years())
        return 'Name: '+self.name+', Age: '+self.age+', Salary: '+self.salary+', Working Years: '+years

   #Employee class here

class Manager(Employee):


    def __init__(self,name,age,salary,employment_year,bonus_percentage,**kwargs):
        self.name= name
        self.age=age
        self.salary=salary
        self.employment_year=employment_year
        self.bonus_percentage=bonus_percentage


    def get_bonus(self):
        salary=int(self.salary)
        return float(self.bonus_percentage) * salary
    def get_working_years(self):
        today=datetime.datetime.today()
        years=today.year-self.employment_year
        return years


    def __str__(self):
        years=str(self.get_working_years())
        bonus=str(self.get_bonus())
        return 'Name: '+self.name+', Age: '+self.age+', Salary: '+self.salary+',  Working Years: '+years+', Bonus: '+bonus





    #Manager class here
def main():
    man_list=[]
    emp_list=[]
    option=''
    while (option!='5'):
        print('Options:\n  1. Show Employees\n  2.Show Managers\n  3.Add an Employee\n  4.Add a Manager\n  5.Exit')
        option =input("What would you like to do?")
        if(option=='1'):
            print(emp_list)
        elif(option=='2'):
            print(man_list)
        elif(option=='3'):
            name=input('Name: ')
            age=input('Age: ')
            salary=input("Salary: ")
            employment_year=int(input('Employment year: '))
            new_emp=Employee(name,age,salary,employment_year)
            emp_list.append(new_emp.__str__())


        elif(option=='4'):
            name=input('Name: ')
            age=input('Age: ')
            salary=input("Salary: ")
            employment_year=int(input('Employment year: '))
            bonus_percentage=input('Bonus Percentage: ')
            new_man=Manager(name,age,salary,employment_year,bonus_percentage)
            man_list.append(new_man.__str__())

    exit()

if __name__ == '__main__':
	main()
