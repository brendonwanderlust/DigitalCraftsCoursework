
#1 to 10 
for x in range(1, 11):
    print x

# n to m    
question1 = int(raw_input("Starting number? "))
question2 = int(raw_input("Ending number? "))
if question2 is not > question1:
    print "Sorry, ending number must be larger than the beginning number?"
else:
    for x in range(question1, question2)
    
#ODD NUMBERS
for x in range(1,10,2):
    print x

#PRINT A SQUARE
stars = '*****'
for x in range(5):
    print stars    

#PRINT SQUARE II
stars = '*****'
squareSize = int(raw_input("How big of a square would you like? "))
for x in range(squareSize):
    print stars

#PRINT A BOX
star = '*'
space = ' '
squareHeight = int(raw_input("Height? "))
squareWidth = int(raw_input("Width? "))
for height in range(squareHeight):
    if (height == 0 or height + 1 == squareHeight):
        print star * squareWidth
    else:
        print star + (space * (squareWidth - 2)) + star    

#PRINT A TRIANGLE
star = '*'
space = ' '
tHeight = int(raw_input("Height? "))
base = (tHeight * 2) - 1
for row in range(1, tHeight + 1):
    spaces = tHeight - row
    stars = (row * 2) - 1
    print (space * spaces) + (star * stars)

#MULTIPLICATION TABLE
for fNum in range(1, 11):
    for sNum in range(1, 11):
        print "%s X %s = %s" % (fNum, sNum, fNum * sNum)

#BONUS: PRINT A BANNER
banner = raw_input("What's you banner? ")
bannerLength = len(banner)
for index in range(1):
    print "*%s***" % (bannerLength * "*")
    print "* %s *" % (banner)
    print "*%s***" % (bannerLength * "*")

#BONUS: Triangle Numbers
x = 0
while x <= 100:
    for n in range(101):
        if n == 0:
            pass
        else: 
            y = (n * (n + 1)) / 2
            print y
            x = y   

#BONUS: Factors
factor = int(raw_input("Give me a number: "))
for x in range(factor + 1):
    if x == 0:
        pass
    elif factor % x == 0:
        print x