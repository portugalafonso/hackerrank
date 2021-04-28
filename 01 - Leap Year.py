# Given a year, determine whether it is a leap year. If it is a leap year, 
# return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and 
# passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    #If year%4==0 is leap year
    if year%4==0:
        leap = True
        #If year%100==0 is not leap year
        if year%100==0:
            leap = False
            #If year%400==0 is  leap year
            if year%400==0:
                leap = True
    
    return leap

#year = int(raw_input())