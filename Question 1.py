import re

def isValid(s):

    Pattern = re.compile("^\+?(\d.\s)?\(?\d{3}\)?[-.\s]?\d{3}?[-.\s]?\d{4}?")
    return Pattern.match(s)


s = "2124567890" # Enter Contact Number Format here
if (isValid(s)):
    print ("Valid Number")    
else :
    print ("Invalid Number")


# 2124567890 , 212-456-7890 , (212)456-7890 , (212)-456-7890 , 212.456.7890 , 
# 212 456 7890, +12124567890 , +1 212.456.7890 , +212-456-7890 , 1-212-456-7890