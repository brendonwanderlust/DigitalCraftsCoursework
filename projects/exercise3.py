totalAmount = int(raw_input("What is the total amount of your bill? "))
tipPercent = float(raw_input("What percent tip would you like to provide?"))/ 100
print "Your total = " + str((totalAmount + (totalAmount * tipPercent)))
