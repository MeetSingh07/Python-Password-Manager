# Random Password Generator

def generator():
    password_lst=[]

    for i in range(1,int((30/100)*n)+1):
        password_lst.append(random.choice(uppercase_alphabets))

    for i in range(1,int((20/100)*n)+1):
        password_lst.append(random.choice(numbers))

    for i in range(1,int((30/100)*n)+1):
        password_lst.append(random.choice(lowercase_alphabets))

    for i in range(1,int((20/100)*n)+1):
        password_lst.append(random.choice(special_characters))

    if len(password_lst)!=n:
        for i in range(1,n-len(password_lst)+1):
            password_lst.append(random.choice(to_fill_characters))

    random.shuffle(password_lst)

    global password_str
    password_str=''.join(password_lst)

import random

# region Variables
uppercase_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alphabets="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special_characters="@#$&*_"
to_fill_characters="0123456789@#$&*_"
# endregion

purpose=''
password_str=''

print('Enter 1 to create password')
print('Enter 2 to save password')
print('Enter 3 to clear password')
print('Enter 4 to store password')
print('Enter 5 to retrieve password')
print('Enter 0 to exit')

while True:
    try:
        choice = int(input('Enter your choice : '))
        
        if choice==1:
            purpose=input("For which app or service you are generating a password ? : ").lower()

            while True:
                try:
                    n=int(input("How many characters long you want to generate a password? : "))
                    if n<=3:
                        print("Please Choose atleast 4 characters.")
                    else:
                        break
                except ValueError as e:
                    print(f'Error : {e}')
                    print("Please enter an integer value")

            while True:
                generator()

                with open('passwords.txt','r') as f:
                    content = f.read()
    
                    if password_str not in content:
                        break
            
            print(f'Password for {purpose} is {password_str}')

        elif choice==2:
            f=open("passwords.txt","a")
            
            if password_str=='' or purpose=='':
                print('Nothing to Save')
            else:
                f.write(f"{purpose} -> {password_str}\n")
                print('Password Saved')
            
            f.close()

            purpose = ''
            password_str = ''

        elif choice==3:
            purpose = ''
            password_str = ''
            print('Cleared')

        elif choice==4:
            if purpose == '' and password_str == '':
                purpose=input("For which app or service you are generating a password ? : ").lower()
                password_str=input('Enter your password : ')
            else:
                print('Save or Clear the old password first')
        
        elif choice==5:
            password_purpose = input("Enter the purpose of the password you want to search : ").lower()
            
            with open('passwords.txt','r') as f:
                content_lst = f.readlines()
                length_of_content_lst = len(content_lst)

                for line in content_lst:
                    parts = line.split('->')
                    
                    saved_purpose = parts[0].strip()

                    if password_purpose == saved_purpose:
                        print(line)

        elif choice==0:
            print('Program Terminated')
            break
            
    except ValueError as e:
        print(f'Error : {e}')
        print('Please enter a valid choice.')