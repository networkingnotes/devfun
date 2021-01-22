def circumference(radius):
    #Formula for a circumference is c = pi * diameter
        #Formala for a diameter is d = 2 * radius
    pi = 3.14 # (Will hardcode pi in this example)
    circumferenceValue = pi * radius * 2
    return circumferenceValue
    
def printCircumference(radius):
    myCircumference = circumference(radius)
    
    print ("Circumference of a circle with a radius of " + str(radius) + " is " + str(myCircumference))