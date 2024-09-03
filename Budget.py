
#These are the user input statments that ask the user questions to find their monthly spending and their debt

Housing = float(input("What is your rent or mortgage cost per month?"))
Utilties = float(input("What is your utilities cost per month?"))
Groceries = float(input("How much do you spend on groceries per month?"))
Transportation = float(input("How much do spend on transportation per month?"))
Health_Care = float(input("What is your monthly medical bill?"))
Personal_Care = float(input("How much do you spend on personal care per month?"))
Clothing = float(input("How much do your spend on clothing per month?"))
Debt = float(input("How much is your monthly debt cost?"))

#This calculates the total cost of all the spending and debt combined
Total_cost = Housing + Utilties + Groceries + Transportation + Health_Care + Personal_Care + Clothing + Debt

print ("your total cost per month is,", Total_cost )

#This calculates the percentage of each indivual category by taking the category divided by the total cost
print (f"{Housing / Total_cost:.3f}" + " is the percentage of housing takes out of your budget")
print (f"{Utilties / Total_cost:.3f}" + " is the percentage of utlities takes out of your budget")
print (f"{Groceries / Total_cost:.3f}" + " is the percentage of groceries takes out of your budget")
print (f"{Transportation / Total_cost:.3f}" + " is the percentage of transportation takes out of your budget")
print (f"{Health_Care / Total_cost:.3f}" + " is the percentage of health care takes out of your budget")
print (f"{Personal_Care / Total_cost:.3f}" + " is the percent6age of personal care takes out of your budget")
print (f"{Clothing / Total_cost:.3f}" + " is the percentage that clothing takes out of your budget")
print (f"{Debt / Total_cost:.3f}" + " is the percentage that debt takes out of your budget")