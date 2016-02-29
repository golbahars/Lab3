def isValidSSN(SSN):
    ''' Returns True if String is in form ###-##-####, returns false otherwise
    Precondition: the temSSN needs to be a string'''
    # check the length of SSN
    if len(SSN) != 11:
        return False
   
    #check the format of the SSN      
    elif SSN[3] == "-" and SSN[6] == "-" and SSN[0:3].isdigit()\
         and SSN[4:6].isdigit() and SSN[7:].isdigit():

        return True
     
    else:
         return False
