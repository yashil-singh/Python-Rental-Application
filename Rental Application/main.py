#Importing python files
import contents
import rent
import return_

#Calling a funtion from contents file to read values in the txt file
fileContents = contents.getFileContents()

#Calling a funtion from contents file to retrun the list as a dictionary
mainData = contents.returnDictionary(fileContents)

loop = True
#Loop for the the whole program to run unless option to exit is choosen
while(loop == True):
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("Welcome to costume Rental Application\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("\nSelect the desirable service option")
    print("1. Press 1 to rent a costume.")
    print("2. Press 2 to return a costume.")
    print("3. Press 3 to exit.\n")

    #Taking user input  
    userOption = (input("Enter an option: "))
    
    validUserOption = True
    #If conditions for the user input
    if (userOption == "1"):
        #Calling rent function from the rent file
        rent.rent(mainData)
      
    elif(userOption == "2"):
        #Calling return_ function from the return_ file
        return_.return_(mainData)
                     
    elif(userOption == "3"):
        print("\nThank you for using our application.\n")
        #To terminate the program
        loop = False
            
    else:
        #Condition for invalid input
        print("\nInvalid Input, Please enter the value as per the provided options.\n")
