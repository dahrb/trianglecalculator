#David Bareham Student Number: 201060865
#COMP517 SHAPES

#Function 1: Angle Finder - Enables the user to input two angles of a triangle and will output the original values + the missing value
def angleFinder ():
    
    print("\nWelcome to the angle finder!")
    
    #defines the variables for user input as floats
    angleDeg1 = float(input("\nPlease enter the first angle here [in degrees]: ")) 
    print("")                     
    angleDeg2 = float(input("Please enter the second angle here [in degrees]: "))
    print("")
    
    #if-else statement to handle values which would not enable the output values to be of a triangle
    if(angleDeg1<=0 or angleDeg1>=180 or angleDeg2<=0 or angleDeg2>=180 or angleDeg1 + angleDeg2>=180):
        print("The angles you have entered are invalid, please enter two angles with an individual range between 0-180 degrees and total less than 180 degrees.")
    
        #returns to the start of the function after invalid input
        angleFinder() 
        
    else:
        #formula for calculating the missing angle using the triangle angle sum theorem
        missingAngleDeg = 180 - angleDeg1 - angleDeg2 
    
        #output displaying the 'missing angle' and the original angles
        print("The 3 interior angles of your triangle are:")
        print("Angle 1: ",angleDeg1,"°")
        print("Angle 2: ",angleDeg2,"°")
        #rounds the output angle to 2dp
        print("Angle 3: ",round(missingAngleDeg,2),"°")
        
    #returns the function to the menu automatically
    return menu()
    
#Function 2: Hypotenuse Finder - Enables the user to input two sides of a triangle and will output the hypotenuse
def hypotenuseFinder ():
    
    print("\nWelcome to the hypontenuse finder!")
    
    #defines the variables for user input as floats
    sideCentimeters1 = float(input("\nPlease enter the first side here [in centimeters]: "))
    print("")                     
    sideCentimeters2 = float(input("Please enter the second side here [in centimeters]: "))
    print("")
    
    #if-else statement to handle negative values which cannot be valid side lengths of a triangle
    if(sideCentimeters1<=0 or sideCentimeters2<=0):
        print("Invalid Input. Please ensure all values entered are greater than 0.")
        
        #returns to the start of the function after invalid input
        hypotenuseFinder()
        
    else:  
        #formula for calculating the hypotenuse given two other sides
        hypoCentimeters = (sideCentimeters1**2 + sideCentimeters2**2)**0.5
    
        #output displaying the hypotenuse and the sides given
        print("The sides of your triangle are:")
        print("Side 1: ",sideCentimeters1,"cm")
        print("Side 2: ",sideCentimeters2,"cm")
        #rounds the hypotenuse output to 2dp
        print("Hypotenuse:",round(hypoCentimeters,2),"cm")  
    
    #returns the function to the menu automatically
    return menu()
    
#Function 3: Area Finder - Enables the user to calculate the area of a triangle given all 3 sides
def areaFinder ():
    
    print("\nWelcome to the area finder!")
    
    #defines the variables for user input as integers
    sideCentimeters1 = float(input("\nPlease enter the first side here [in centimeters]: "))
    print("")                     
    sideCentimeters2 = float(input("Please enter the second side here [in centimeters]: "))
    print("")
    sideCentimeters3 = float(input("Please enter the third side here [in centimeters]: "))
    print("")
    
    #if-else statement to handle negative values which cannot be valid side lengths of a triangle
    if(sideCentimeters1<0 or sideCentimeters2<0 or sideCentimeters3<0):
        print("Invalid Input. Please ensure all values entered are greater than 0")
        
         #returns to the start of the function after invalid input
        areaFinder()
        
    else:
        #defines the semiperimeter
        semiPerimeter = (sideCentimeters1+sideCentimeters2+sideCentimeters3)/2 
    
        #Heron's formula for calculating the area of a triangle given all 3 sides and using the semiperimeter
        areaCentimetersSq = (semiPerimeter*(semiPerimeter-sideCentimeters1)*(semiPerimeter-sideCentimeters2)*(semiPerimeter-sideCentimeters3))**0.5
    
        #if-else statement to handle the potential for Heron's Formula to result in complex numbers giving an impossible triangle
        if(type(areaCentimetersSq) == complex):
            print("The values you have entered result in an impossible triangle. Please enter new values.")
            
            #returns to the start of the function after impossible triangle dimensions given
            areaFinder()
    
        else:
            #output displaying the area of the triangle and the 3 sides
            print("\nThe sides of your triangle are:")
            print("Side 1: ",sideCentimeters1,"cm")
            print("Side 2: ",sideCentimeters2,"cm")
            print("Side 3: ",sideCentimeters3,"cm")
            #rounds the output area to 2dp
            print("\nThe area of your triangle is: ",(round(areaCentimetersSq,2)),"cm²")
            
    #returns the function to the menu automatically
    return menu()

#Function 4: Menu - Allows the user to select the triangle calculator function they want
def menu ():
    
    #Prints the menu
    print("\nTriangle Calculator Menu\n")
    print("1) Angle Finder")
    print("2) Hypotenuse Finder")
    print("3) Area Finder")
    print("q) Exit Program\n")
    
    #Allows the user to input their choice
    selection = input("Enter your choice followed by [ENTER]: ")
    
    #If-elif-else statements to allow each option to be selected
    if(selection=="1"):
        #Runs the Angle Finder function
        angleFinder()
        
    elif(selection=="2"):
        #Runs the Hypotenuse Finder function
        hypotenuseFinder()
        
    elif(selection=="3"):
        #Runs the Area Finder function
        areaFinder()
        
    elif(selection=="q"):
        #Ends the program immediately
        exit()
        
    else:
        #Handles any incorrect values entered into the menu and returns the user to the menu
        print("\nInvalid choice entered please enter a valid choice from the menu") 
        menu()

#Initiates the program upon running the file
menu()
    

    
    
    
    
    
    
    
    
    
    
    
    
