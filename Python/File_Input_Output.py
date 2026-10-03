# Input Devices ---> Keyboard, Mouse, Network, Files, Databases
# Output Devices ---> Monitor(Console/Screen), Printer, Speaker, Network, Files, Databases
# Store ---> The process of saving(persistance) state of an object is called Serialization. Eg: Python Data to JSON Type Data
# Deserialization ---> Eg: JSON to Python Data
# Two types to access a File:
#               i) Sequential Access
#               ii) Random Access
# CRUD Operations:
#           i) Create
#           ii) Read
#           iii) Update
#           iv) Delete
# To open a file we have TWO MODES:
#                               i) Text
#                               ii) Binary (Image/ Video/ Audio/ .exe)

# File handling have three major steps:
#                               i) Open file
#                               ii) Read/Write file
#                               iii) Close file

# Mode Parameters of Open func.:# Text is a default mode  #for binary
#                           i) w ---> write               # wb          # w overwrites if file exist otherwise creates new
#                           ii) r ---> read               # rb
#                           iii) a ---> append            # ab
#                           iv) w+ ---> write + read      # wb+
#                           v) r+ ---> read + write       # rb+
#                           vi) a+ ---> append + read     # ab+

def read_write_text():
    str1 = 'Hi! My name is Kshitij Bhardwaj.\n'
    str2 = 'I am currently pursuing BTech in CSE.'

    # Open a file
    f = open('intro.txt', 'w')
    f.write(str1)
    f.write(str2)
    f.close()

    print()

    f = open('intro.txt')
    srt3 = f.read()
    print('str3:',srt3)
    f.close()

    print()

    f = open('intro.txt')
    str4 = f.readline()
    print('str4:',str4)
    f.close()

    print('Reading files using for loop:')
    f = open('intro.txt')
    for i in f:
        print(i, end = '')
    f.close()

    print()

    print('\nReading files using while loop:')
    f = open('intro.txt')

    i = ''
    while True:
        i = f.readline()

        if len(i) == 0:
            break
        else:
            print(i, end = '')

    f.close()

    print()

def my_copy_large():
    f1 = open('intro.txt')
    f2 = open('intro.doc', 'w')

    for str in f1:
        f2.write(str)

    f1.close()
    f2.close()

    print()

def my_read_ch():
    print('Reading and Printing Character by Character:')
    f = open('intro.txt')
    while True:
        ch = f.read(1)

        if len(ch) == 0:   # if ch == ''  # if ch == None
            break
        else:
            print(ch, end = '')

read_write_text()
my_read_ch()