#create
#open
#read
#write
#append
#close

#r,w,a

#.txt files

# print(os.environ["USERNAME"])

def writefile():
    obj = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\sample1.txt","w")
    obj.write("Hello Universe!")
    obj.close()

# writefile()

def append_text_to_file(text):
    text = "\n" + text
    obj = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\sample.txt","a")
    obj.write(text)
    obj.close()

# append_text_to_file("Hello World!")

def readfile():
    f = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\reference.txt","r")
    context = f.read()
    print(context)
    f.close()

# readfile()

def readfile_lbl():
    f = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\reference.txt","r")
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# readfile_lbl()

# verify sehwag was present ot not, if there, give me line number

def readfile_lbl_1(target):
    target = target.lower()
    f = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\reference.txt","r")
    lines = f.readlines()
    for index,line in enumerate(lines):
        s = line.strip()        #
        s= s.lower()
        if target in s:
            print(s)
            print("This is the line number {}".format(index+1))
            # break
    # else:
    #     print("{} was not present in the file".format(target))


# readfile_lbl_1("SEhwag")


#Task1: read all the lines from a file and create new file and dump this data to that file (even lines )

