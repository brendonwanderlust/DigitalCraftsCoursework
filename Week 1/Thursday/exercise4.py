totalAmount = int(raw_input("What is the total amount of your bill? "))
serviceQuality = raw_input("How was your service today? (good, fair, bad?)") 

def tipCalc():
    if serviceQuality == 'good':
        return float(1.2)
    elif serviceQuality == 'fair':
        return float(1.5)
    elif serviceQuality == 'bad':
        return float(1.1)

totalWithTip = totalAmount * tipCalc()
tipSplit = int(raw_input("How many people will you be spliting the bill with? "))
print "Each person should pay = %s" % float(totalWithTip / tipSplit)
