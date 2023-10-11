#Company Structure Class

import string
from uuid import uuid4


class Employee:
    """ Company Structure
    
    Employee:
       - Engineer
       - Projec Manager
    """
    message = None
    company_division = 'Engineer'  #class variable [owned by the clas an not the instance]

    def __init__(self, firstName, lastName) -> None:
        self.firstName= firstName
        self.lastName = lastName
        self.employee_id = str(uuid4())
        self.team = None
        self.position = None

    def getEmployeeFullName(self)-> string:
        """ Get employee fullname.
            
        Return:
              Employee name (string)
        """

        return self.firstName + " " + self.lastName
    
    def setEmployeeTeam(self, team = {})-> None:
        """ Set new employee team 
        
        Args:
            team(dict): Employee team
        """
        self.team = team

    def setTeamAndPosiitonInfo(self, team, position):
        """ Set team and Position info
        
        Args:
           team(str):     Team name
           position(str): Position name
        """
        self.team = team
        self.position = position
   
    @classmethod
    def failed(self):    #class method [Does not require instantion in order to be used.]
        print('Invalid class constructor ...')
   
    @classmethod
    def construct_with_one_string(this, first_last):
        """ Will construct an employee class with a single string
        
        Args:
            first_last(str): Employee name
                ex. Morel Sami
        """
        this.message = 'Failed'
        full_name_arr = first_last.split()
        if(len(full_name_arr) >= 2):
            #this.message = 'Passed'
            return(this(full_name_arr[0], full_name_arr[1]))
        
        this.failed()


class Engineer(Employee):
    def __init__(self, firstName, lastName) -> None:
        super().__init__(firstName, lastName)
        self.projects = 0

    def add_projects(self, num_of_projects):
     """ Add items to project count.
    
     Args:
        num_of_projects(int): Number of Projects
     """
     if num_of_projects >= 0:
         self.projects += num_of_projects

    def failed(self):
        super().failed() #call parent class method
        print('Another failed method..')
    
    @staticmethod
    def calculate_sum(num1, num2):  #static class method
        return num1 + num2

   

   

test = Employee('Morel', 'Sami')
test.setTeamAndPosiitonInfo('Business Department', 'Customer Service Agent')
print(test.__dict__)
print(test.firstName)
fullname = test.getEmployeeFullName()
print(fullname)
print(test.company_division)
test.company_division = 'Project Manager'
print(test.company_division)
test.firstName = 'Santos'
print(test.getEmployeeFullName())

employee = Employee.construct_with_one_string('Morel Sami')
if Employee.message != 'failed':
    print(employee.__dict__)
else:
    print(Employee.message)

test2 = Engineer('Audrey', 'Taiwo')
print(test2.__dict__)

