import random
import string# public module variables:

pass_length = int(input("Enter your password length: "))

str_vlaues = string.ascii_letters + string.digits + string.punctuation

password = ""
# for i in range(pass_length):
#   password += random.choice(str_vlaues)

# print("Your random password is:", password)

# list coprehension
password = "".join([random.choice(str_vlaues) for i in range(pass_length)])
# "*".join : --> ye method join karata hai sentence ke bitch me jo bhi waha par lihe hoge aap is condition me * join karake dikhayega output me like 4 digit password hua tab : 2*%*a*0 aise
print("Your random password is:", password)

# print(string.punctuation)
# print(string.ascii_letters)

# print(random.choice("hello")) #o/p: h,or,o
