grade = int(input("Enter your numeric grade:"))

if 100 >= grade >= 90:
    print ("A")
elif 100 >= grade >= 80:
    print ("B")
elif 100 >= grade >= 70:
    print ("C")
elif 100 >= grade >= 60:
    print ("D")
elif 100 >= grade < 60:
    print ("F")
else: 
    print ("The number is not between 0 and 100")