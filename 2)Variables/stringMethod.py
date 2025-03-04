# STRINGS ARE NOT CHANGABLE IN PYTHON, It only creates new string
a = "!!!!!!! !!! sahil !!!! !6956! !!!!!!!!!"
print(len(a))
print(a.upper())

print(a.lower())

print(a.rstrip("!"))   #Only for skiping tralling element
print(a.lstrip("!!"))   #Only for skiping tralling element

print(a.replace("sahil","John"))

x = a.split('!')
print(x)

blogHeading = "introduction to jS"  #First letter capitalize ho jayega,baki small letter
print(blogHeading.capitalize())

str1 = "welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

print(a.count("sahil"))

str1 = "welcome to the Console!!!"
print(str1.endswith("!!!"))            #str1 !!! is se end ho rahi hai kya ye batata hai

str1 = "He's neme is Dan. He is an honest man."
print(str1.find("ishh"))
#print(str1.index("ishh"))

str1 = "WelcomeToTheconsole"
print(str1.isalnum())

str1 = "WelcomeToTheconso4le"
print(str1.isalpha())

str1= "hello world"
print(str1.islower())

king = "I AM A KING"
print(king.swapcase())   #upper ko lower or lower ko upper


