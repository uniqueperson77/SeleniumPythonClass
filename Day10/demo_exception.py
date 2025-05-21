f = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\sample.txt","r")
try:
    f2 = open(r"D:\Isha\SeleniumPythonClass\ExternalFiles\sample2.txt", "r")
    print(f.read())
    f.close()
    print("Object f is closed")
except Exception as e:
    print(e)
finally:
    print("Object f is closed from finally block")
    f.close()



exit()
a,b= 10,0
try:
    print(a/b)
except Exception as exp:
    print("Number can't be divide with 0, Error: {}".format(exp))
print("Code finished")