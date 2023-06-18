QUESTION:-1. What is an Exception in python? Write the difference between Exceptions and syntax errors.
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
exceptions :- Exceptions are raised when some internal events occur which changes the normal flow of the program.
Syntax errors :- When the proper syntax of the language is not followed then a syntax error is thrown.



QUESTION:-2. What happens when an exception is not handled? Explain with an example.
When an exception is not handled, it results in an "unhandled exception" error or an "exception propagates" through the program. This means that the normal flow of execution is disrupted, and the program terminates or enters an undefined state.
For example :-
def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print("The result of the division is:", result)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
divide_numbers()



QUESTION:-3. Which python statements are used to catch and handle exceptions? Explain with an example.
In Python, the try-except statement is used to catch and handle exceptions. It allows you to specify a block of code where exceptions might occur and define how to handle those exceptions if they arise. The general syntax of a try-except statement is as follows:
For example :-
def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print("The result of the division is:", result)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
divide_numbers()



QUESTION:-4. Explain with an example.
a. try and else
b. finally
c. raise
a. try and else :- You can use the else keyword to define a block of code to be executed if no errors were raised.
for example :- In this example, the try block does not generate any error.
try: 
    print("Hello")
except: 
    print("something went wrong") 
else: 
    print("Nothing went wrong")       

b. finally :- The finally block will always be executed, no matter if the try block raises an error or not.
for example :-
try: 
    x > 3
except: 
    print("Something went wrong")
else: 
    print("Nothing went wrong")
finally: 
    print("The try...except block is finished")            

c. raise :- The raise keyword is used to raise an exception. you can define what kind of error to raise, and the text to print to the user.
for example :- Raise a TypeError if x is not an integer.
x = "hello"
if not type(x) is int: 
    raise TypeError("Only integers are allowed")



QUESTION:-5. What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example.
In Python, we can define custom exceptions by creating a new class that is derived from the built-in exception class. Custom exceptions will add information about project-related problems.
class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The {self.f} is not in a valid range {self.min_f, self.max_f}'

def fahrenheit_to_celsius(f: float) -> float:
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)
    return (f - 32) * 5 / 9
if __name__ == '__main__':
    f = input('Enter a temperature in Fahrenheit:')
    try:
        f = float(f)
    except ValueError as ex:
        print(ex)
    else:
        try:
            c = fahrenheit_to_celsius(float(f))
        except FahrenheitError as ex:
            print(ex)
        else:
            print(f'{f} Fahrenheit = {c:.4f} Celsius')



QUESTION:-6. Create a custom exception class. Use this class to handle an exception.
class MyCustomError(Exception):
    def __init__(self , *args): 
        if args: 
            self.message = args[0]
        else: 
            self.message = None

    def __str__(self): 
        print('calling str')
        if self.message: 
            return 'MyCustomError , {0} '.format(self.message)
        else: 
            return 'MyCustomError has been raised' 
    raise MyCustomError                   


class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18
try: 
    input_num = int(input("Enter a number : "))
    if input_num < number: 
        raise InvalidAgeException
    else: 
        print("Eligible to vote")
except InvalidAgeException: 
    print("Exception occurred: Invalid Age")        
