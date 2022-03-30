Employees = {'First': 0, 'Second': 0, 'Third': 0, 'Fourth': 0}
EmployeeCount = ('First', 'Second', 'Third', 'Fourth')
DayStart = (0, 1, 2, 3)
DayCounter = 1
Days = 28
Hours = 12

for i in range(len(Employees)):
    Day = DayStart[i]
    DayCounter = 1
    while Day != Days:
        if DayCounter == 1 or DayCounter == 2:
            Employees.update({EmployeeCount[i]: Employees.get(EmployeeCount[i]) + Hours})
        DayCounter += 1
        if DayCounter == 5:
            DayCounter = 1
        Day += 1
