# Creates class Company
class Company:
    # attributes
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    no_of_employees = 100

    # method
    def productivity(self):
        return Company.revenue / Company.no_of_employees

c1 = Company()
print(c1.productivity())