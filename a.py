import getpass
print("WELCOME");

print ("please provide the details");

name = raw_input("name :- ")
age = raw_input("age :- ")
mail = raw_input("e-mail id :- ")
pass = raw_input("required password:- ")
;print ("wait.......")

text_file = open("new.txt"' w)
text_file.write("name"+" is "name +", the mail id is " + mail + "and the password is  "+ pass)
text_file.close()
 



