#Defined a Calculator class with arithmetic operations
class Calculator:
    def add(self, a, b):
        return a + b #add two numbers

    def subtract(self, a, b):
        return a - b #subtract two numbers

    def multiply(self, a, b):
        return a * b #multiply two numbers

    def divide(self, a, b):
        if b !=0:
            return a/b #division of numbers
        else:
            print("Error: Dividing by zero")

#Defined a class  Calculate to manage the user input
class Calculate:
    def __init__(self):
   #Initialize the Calculate with Calculator instance.
        self.cal = Calculator()

    def run(self): #Run the calculator program, providing a menu for user interaction
        while True:
            #Display the menu option
            print("Select a mathematical operation:")
            print("1.ADDITION")
            print("2.SUBTRACTION")
            print("3.MULTIPLICATION")
            print("4.DIVISION")
            print("5.EXIT")

            #prompt user to choose the option
            choice = input("Enter Your Operation (1./2./3./4./5.):")

            if choice in ['1','2','3','4',]:
                try:
                    # Taken input from the user for num1 and num2
                    num1 = float(input("Enter First Number:"))
                    num2 = float(input("Enter Second Number:"))
                except ValueError:
                    print("Invalid input. Please enter the number values.")
                    continue
            #Perform the chosen option
                if choice == '1':
                    print(f"The result is:{self.cal.add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is:{self.cal.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is:{self.cal.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is:{self.cal.divide(num1, num2)}")
                elif choice == '5':
                    print("Exiting the calculator.")
                #else print's when the input is invalid
                else:
                    print("Invalid input.Please enter a valid choice.")
#Instantiate and run
if __name__ == "__main__":
    op = Calculate()
    op.run()





