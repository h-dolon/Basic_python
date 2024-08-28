def getWage():
    print(base_salary + overtime*rate)

if "__main__":
    base_salary = 20000
    overtime = 2
    rate = 0.25
    getWage()