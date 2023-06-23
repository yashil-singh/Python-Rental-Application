#Importing python files
import contents
import userInputs
import bills

#Funtion to return the costumes
def return_(mainData):
    #list to store the costumes that are returned
    costumesReturned = []

    #To continue the loop until the user doesn't return more costumes
    continueLoop = True
    while (continueLoop == True):
        
        #Calling the printCostume function from the contents file
        contents.printCostume(mainData)

        #Calling funtion from contents file to get the serial number
        SNo = userInputs.getValidSNnoToReturn(mainData)

        #Calling the getValidStock function to get the quantity
        quantity = userInputs.getValidStockToReturn(mainData,SNo)

        #Appending the costumes returned list
        costumesReturned.append([SNo,quantity])

        #Calling the increasedStock funtion to update the values in the txt file
        mainData = contents.increasedStock(mainData,SNo,quantity)
        
        #To validate user input
        validUserInput = False
        while (validUserInput == False):
            userInput = input("\nDo you want to return more costumes?(yes/no)\n")
            userInput = userInput.lower()
                            
            if (userInput == "yes"):
                validUserInput = True

            elif(userInput == "no"):
                #Calling the funtion to calculate fine and show the bill
                bills.showBillToReturn(costumesReturned)
                continueLoop = False
                break

            else:
                print("\nInvalid Input. Please enter either yes or no.")
