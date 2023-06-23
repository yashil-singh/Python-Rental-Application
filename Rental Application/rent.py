#Importing python files
import contents
import userInputs
import bills

#Function to rent costumes
def rent(mainData):
    #Creating a list to store the costumes that are rented
    costumesRented= []

    #To continue the loop until the user doesn't rent more costumes
    continueLoop = True
    while (continueLoop == True):
        
        #Calling the printCostume function from the contents file
        contents.printCostume(mainData)
        
        #Calling funtion from contents file to get the serial number
        SNo = userInputs.getValidSNnoToRent(mainData)
        
        #Calling the getValidStock function to get the quantity 
        quantity = userInputs.getValidStockToRent(mainData,SNo)
        
        #Appending the costumes rented list
        costumesRented.append([SNo,quantity])
        
        #Calling the reducedStock funtion to update the values in the txt file
        mainData = contents.reducedStock(mainData,SNo,quantity)

        #To validate the user input
        validUserInput = False
        while (validUserInput == False):
            userInput = input("Do you want to rent more costumes?(yes/no)\n")
            userInput = userInput.lower()
                        
            if (userInput == "yes"):
                validUserInput = True

            elif(userInput == "no"):
                #Calling the function to calculate total and show the bill
                bills.showBillToRent(costumesRented)
                continueLoop = False
                break

            else:
                print("\nInvalid Input. Please enter either yes or no.\n")
