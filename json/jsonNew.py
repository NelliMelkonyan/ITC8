#This program simulates the operation of an json


arrkey=[]       #List of keys
arrval=[]       #List of Values
bracket=[]
length = 0
boolian = 1
#This function checks the data
def check(arg,key):
    str1 = arg.split(':', 1)
    if str1[0][0] != '"' or str1[0][len(str1[0]) - 1] != '"' or len(str1[0]) == 2:
        print "Eror:Invalid key"
        return 0
    str1[0] = str1[0][1:]
    str1[0] = str1[0][:-1]
    if str1[1][0] == '"' and len(str1[1]) == 2:
        arrkey.append(str1[0])
        arrval.append("")
        return 1

    if str1[1][0] == '"' and len(str1[1]) != 2:
        str1[1] = str1[1][1:]
        str1[1] = str1[1][:-1]
    for i in range(length):
        if str1[0] == arrkey[i]:
            print "Eror:Keys are repeated"
            return 0
    arrkey.append(str1[0])
    arrval.append(str1[1])
    return 1

#This function findes value by key
def find(key, length):
    for i in range(length):
        if key == arrkey[i]:
            print "Value - " + arrval[i]
            return 1
    return 0

if __name__ == '__main__':
    string = raw_input('Input your json: ')
    string = string.replace(" ", "")
    if string[0] != "{" or string[len(string) - 1] != "}":
        if string[0] != "[" or string[len(string) - 1] != "]":
            print "Eror:Wrong input (Check brackets)"
            exit(0)
    string = string[1:]
    string = string[:-1]

#This function checks the string for validity and separates it
def cat(string,key):
    keyVal = ""
    countBrack = 0
    colon = 0
    word = 0
    digit = 0
    istrue = 0
    isfalse = 0
    isnone = 0
    true = "true"
    false = "false"
    none = "none"
    j = 0
    end = 0
    if string[0] == ",":
        string = string[1:]
    for i in range(len(string)):
        if end == 1 and string[i] == ",":
            string = string[i:]
            if check(keyVal,key) == 0:
                return 0
            return string
        if colon == 1 and string[i] != ":":
            print "Error: Forgotten ':'"
            return 0
        elif colon == 1 and string[i] == ":":
            colon = 0
            keyVal += string[i]
            if i == len(string) - 1:
                print "Error:(Where is the value)"
                return 0
        if word == 1:
            keyVal += string[i]
        if countBrack == 1:
            keyVal += string[i]
        if countBrack == 2 and colon == 0 and word == 0:
            if string[i] == "t":
                istrue = 1
            elif string[i] == "f":
                isfalse = 1
            elif string[i] == "n":
                isnone = 1
        if end == 1:
            return 0
        if istrue == 1:
            if string[i] == true[j]:
                keyVal += string[i]
                j += 1
                if j == 4:
                    end = 1
            else:
                print "Error:Wrong value"
                return 0
        if isfalse == 1:
            if string[i] == false[j]:
                keyVal += string[i]
                j += 1
                if j == 5:
                    end = 1
            else:
                print "Error:Wrong value"
                return 0
        if isnone == 1:
            if string[i] == none[j]:
                keyVal += string[i]
                j += 1
                if j == 4:
                    end = 1
            else:
                print "Error:Wrong value"
                return 0
        if string[i] == '"':
            countBrack += 1
            if countBrack == 1:
                keyVal += string[i]
            elif countBrack == 2:
                colon = 1
            elif countBrack == 3:
                keyVal += string[i]
                word = 1
            elif countBrack == 4:
                if i == len(string) - 1:
                    string = ""
                else:
                    string = string[i + 1:]
                if check(keyVal,key) == 0:
                    return 0
                return string
        elif colon == 0 and countBrack == 2:
            if string[i].isdigit():
                keyVal += string[i]
                digit = 1
            elif digit == 1 and string[i] == ",":
                string = string[i:]
                if check(keyVal,key) == 0:
                    return 0
                return string
            elif digit == 1:
                print "Error:Wrong value"
                return 0
            elif string[i].isalpha():
                print "Error:Wrong value"
                return 0
    if countBrack == 3:
        print "Error:Wrong value"
        return 0
    elif end == 0 and (istrue == 1 or isfalse == 1 or isnone == 1):
        print "Error:wrong value"
        return 0
    string = ""
    if check(keyVal,key) == 0:
        return 0
    return string

if __name__ == '__main__':
    key = raw_input('input key: ')
    while string != "":
        string = cat(string,key)
        if string == 0:
            boolian = 0
            break
        length += 1
    if boolian != 0:
        if not find(key, length):
            print "Key not found"

