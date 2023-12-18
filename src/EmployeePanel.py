from ClampValue import ClampValue


class EmployeePanel:
    employeePassword = "thisPasswordIsVerySecure"

    def VerifyEmployeePassword(self):
        passEntry = input('Attempting to access employee panel, please enter password: ')
        if self.employeePassword == passEntry:
            return True
        else:
            print('Incorrect password!')
            return False

    def EmployeeMenu(self):
        if self.VerifyEmployeePassword():
            print("Welcome to the employee menu!")
            print("What would you like to do?")
            print("1. Restock items to inventory")
            print("2. Remove items from stock")
            print("3. View recent purchases from customers")
            print("4. Back to storefront")
            employeeMenuChoice = ClampValue(int(input("(1-4) ")), 1, 4)

            match employeeMenuChoice:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    return
        else:
            print("Unable to access employee panel")
