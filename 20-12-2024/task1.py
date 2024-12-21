#password -min 10 char max 15 char
#atleast 1 upper case,1 lower case,1 digit and 1 special char
#not white spaces
#should not end with dot(.) or @ symbol
sp = ["@", "!", "#", "$", "%", "^", "&", "*"]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def check_strength(pwd):
    if (len(pwd) < 10 or len(pwd) > 15):
        return "----INVALID PASSWORD----\nPassword should be minimum 10 characters and maximum 15 characters."
    if( " " in pwd):
        return "No white spaces please."
    if (pwd.endswith(".") or pwd.endswith("@")):
        return "----INVALID PASSWORD----\nPassword should not end with '.' or '@'."
    has_lower = any(c in alpha for c in pwd)
    has_upper = any(c in caps for c in pwd)
    has_digit = any(c in digit for c in pwd)
    has_special = any(c in sp for c in pwd)
    if(not (has_lower and has_upper and has_digit and has_special)):
        return "----INVALID PASSWORD----\nPassword should contain at least one lowercase letter, one uppercase letter, one digit, and one special character."
    return "Password is valid."

password = input("Enter your password: ")
print(check_strength(password))
