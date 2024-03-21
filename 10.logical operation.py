#logical operartors (and,or,not)
#and 2 must be tru
#or 1 must be true


temp = int(input("What is the temperature is outside?:  "))

#if temp >= 0 and temp <= 30:
    #print("The temperature is good today")
    #print("Go outside")
#elif temp < 0 or temp > 30:
    #print("The temperature is bad today")
    #print("stay inside")

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today")
    print("stay inside")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside")