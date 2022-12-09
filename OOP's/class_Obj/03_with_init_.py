
'''
class person:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname


myname = person("xyz", "pqr")
print(myname.last)


'''


class MyCompany:

    # methods
    def __init__(self, compname, revenue, employeesize):
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize

    def productivity(self):
        return self.revenue / self.no_of_employees


a = MyCompany('XYZ Bank', 1000, 100).productivity()

print(a)

