def is_rotation(string1, string2):
    if string1 == None or string2 == None:
        return False
    elif string1 == string2 or (string2 in string1*2 and len(string1) == len(string2)):
        return True
    else:
        return False
