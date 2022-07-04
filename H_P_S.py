import random
from random import randint
import string

                                                        #######################
                                                        #      FUNCTIONS      #
                                                        ######################
def read(name):
    #read the password from txt
    text_file = open(name, "r")
    #make it string
    data = text_file.read()
    #close the file
    text_file.close()
    if '#' in data:
        print('choose a password with no hashtag in and try again!')
        quit()
    else:
        print('file OK!')
    #save length of the data
    len_of_data=len(data)
    return data , len_of_data

#Create a random string
def random_string(Length):
    #length of string
    L= Length
    #unwanded char
    ban_char = '#'
    #random with upper and capital letterr,punctuation characters and digits
    ran = ''.join(random.choices([s for s in string.ascii_letters+string.punctuation + string.digits if s not in ban_char], k = L))
    #to string
    rand_Str=str(ran)
    return rand_Str
#create the new string to write
def create_string(rand_str,len_of_pass,passw):
    string2=""
    string0=""
    ban_char = '#'
    rand_positions=random.sample(range(0, len(rand_str)),len_of_pass )
    ran2 = ''.join(random.choices([s for s in string.ascii_letters+string.punctuation +string.digits if s not in ban_char], k = 10))
    for i in range(0,len(rand_positions)):
        string1 = rand_str[:rand_positions[i]] + '#'+passw[i] + rand_str[rand_positions[i]+1:]
        string0=string0+string2+string1+ran2
    return string0
#adds a new line to the string every n char
def add_lines(string0,number):
    return'\n'.join(string0[i:i+number] for i in range(0, len(string0), number))

#write in file
def write(name2,string0):
    text_file2 = open(name2, 'w')
    #write in file
    text_file2.write(string0)
    #close the file
    text_file2.close()

                                                            #######################
                                                            #   END OF FUNCTIONS  #
                                                            ######################

filename=input('Enter a file name(example: password.txt): ')
passw,len_of_pass=read(filename)

num = int(input("Choose length for the random string(bigger than your password): "))
while num<=len_of_pass:
    num = int(input("Choose length for the random string(bigger than your password): "))
rand_str=random_string(num)

string0=create_string(rand_str,len_of_pass,passw)

numnew=60
string0=add_lines(string0,numnew)
exportname=input('Enter name for saving(example: password2.txt): ')
write(exportname,string0)
