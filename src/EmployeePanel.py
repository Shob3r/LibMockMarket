class EmployeePanel:
    employeePassword = "thisPasswordIsVerySecure"

    def verifyPassword(self):
        print("Attempting to access employee panel, please enter password.")
        userPassword = str(input())
        print(userPassword)

        if userPassword is self.employeePassword:
            self.EmployeePanelMenu()
        else:
            print("Incorrect password!")

    def EmployeePanelMenu(self):
        print("Welcome to the employee menu!")
