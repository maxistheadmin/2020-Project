mussleN = int(input("How many mussels are in the quadrant: "))
width = int(input("Please enter the width of the bed: "))
length = int(input("Please enter the length of the bed: "))
area = (width*2)*(length*2)
totalM = mussleN*area
totalW = totalM*0.97
print("Total Mussels in the Bed: " + str(totalM) + " mussels")
print("Total water filter in 1 hour: " + str(totalW) + " Liters")
