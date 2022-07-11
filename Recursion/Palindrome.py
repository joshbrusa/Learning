def Palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    
    if string[0] == string[-1]:
        return Palindrome(string[1:len(string)-1])
    
    return False

print(Palindrome("racecar"))