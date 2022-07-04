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
    #save length of the data
    return data

#ruterns me the indexes of the #
def index_all(x, list):
    indices = []
    start = 0
    while start < len(list):
        try:
            i = list.index(x, start)
            indices.append(i)
            start = i + 1
        except ValueError:
            break
    return indices

#return the character at # index +1
def pass_return(indexes,passw):
    values=[]
    for i in range(0,len(indexes)):
        test_value=passw[indexes[i]+1]
        if test_value=='\n':
            test_value=test_value=passw[indexes[i]+2]
        values.append(test_value)
    return values


                                                            #######################
                                                            #   END OF FUNCTIONS  #
                                                            ######################

filename=input('Enter a file name(example: password.txt): ')
code=read(filename)
indexes=index_all('#',code)
password=pass_return(indexes,code)
password=''.join(map(str,password)) #password list to string
print(password)
