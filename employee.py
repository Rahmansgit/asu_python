
class Employee:
  #Class variables
  companyName = 'Python Developers'

  #Constructor
  def __init__(self, *args):
    if len(args) < 4:
      self.id = 1000
      self.firstName = 'Unknown'
      self.lastName = 'Unknown'
      self.salary = 0
    else:
      self.id = args[0]
      self.firstName = args[1]
      self.lastName = args[2]
      self.salary = args[3]

  def print(self):
    print('Employee ID: ', self.id, "\nFirst Name: ", self.firstName, "\nLast Name: ", self.lastName, "\nSalary: ", self.salary)

  emp1 = Employee(1213)
  emp2 = Employee(2345, "Bob", "Smith", 36000)