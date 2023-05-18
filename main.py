import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Marks password Generator!")
while True:
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = []

    for let in range(0, nr_letters):
        random_let =  random.choice(letters)
        password += random_let
        #print(password)
    for sym in range(0, nr_symbols):
        random_sym = random.choice(symbols)
        password += random_sym
    for num in range(0, nr_numbers):
        random_number = random.choice(numbers)
        password += random_number
    random.shuffle(password)
    password = ''.join(password)
    print(password)
    
    repeat = input('Would you like to make another password? (Y/N): \n')
    if repeat.lower() != 'y':
        break




