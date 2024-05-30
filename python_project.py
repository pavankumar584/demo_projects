# Password Generator 
import random

alphabete = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number =[0,1,2,3,4,5,6,7,8,9]

special_charecter = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=']


char_in_password = int(input('How many alphabate you want in your password : '))
number_in_password = int(input('How many number you want in your password : '))
special_char = int(input('How many special charecter you want : '))

password_list = []

for j in range(1,char_in_password+1):
    ch = random.choice(alphabete)
    password_list.append(ch)
for k in range(1,number_in_password+1):
     num = str(random.choice(number)) # choice method choose random item from list
     password_list.append(num)
for l in range(1,special_char+1):
    sp = random.choice(special_charecter)
    password_list.append(sp)
    
random.shuffle(password_list)
password = ''.join(password_list)
print(f'your password is [ {password} ]')