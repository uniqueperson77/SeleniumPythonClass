#"aaaabbcccd"
#a4b2c3d1

def code():
    a ="aaaabbcccdd"
    checked = ""
    result = ""
    for val in a:
        if val not in checked:
            occ = a.count(val)
            result = result + val+ str(occ)
            checked = checked+val
        else:
            print("This character {} was already checked.".format(val))

    print(result)



