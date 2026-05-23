#Collatz sequence
def collatz(number):
    if number%2==0:
        result = number//2
    else:
        result = 3*number + 1    
    print (result)
    return result

try:
    user_input = input("Enter number:\n") 
    current_number = int(user_input)

    #keeps calling the function until it reaches 1
    while current_number != 1:
        current_number = collatz(current_number)   
except ValueError:
    print("Error: You must enter an integer")