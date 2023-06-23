#Function to get the contents of the text file
def getFileContents():
    file = open("stock.txt","r")
    lines = (file.readlines())
    file.close()
    return lines

#Function to return the contents of the text file into a dictionary
def returnDictionary(fileContents):
    #Creating a dictionary
    newData = {}
    for index in range(len(fileContents)):
        #Storing the data of finleContents in the newData dictionary
        newData[index+1] = fileContents[index].replace("\n","").split(",")
    return newData

#Function to print the available costumes
def printCostume(mainData):
    print("\n+================================================================================+")
    print("|","SN no.","|","Name","\t","\t","|","Brand","\t","|","Price","\t","|","Quantity","\t","|")
    print("+================================================================================+")
    #Printing all the data of mainData 
    for key,value in mainData.items(): 
        print("|",key,"\t","|",value[0],"\t","|",value[1],"\t","|",value[2],"\t","\t","|",value[3],"\t","\t","|")
        print("+--------------------------------------------------------------------------------+")

#Function to get the reduced stock after renting 
def reducedStock(mainData,SNo,quantity):
    mainData[SNo][3] = str(int(mainData[SNo][3]) - quantity)
    file = open("stock.txt","w")
    for value in mainData.values():
        write_ = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
        file.write(write_)
    file.close()
    print("")
    return mainData

#Function to get the increased stock after returning 
def increasedStock(mainData,id_,cQuantity):
    mainData[id_][3] = str(int(mainData[id_][3]) + cQuantity)
    file = open("stock.txt","w")
    for value in mainData.values():
        write_ = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
        file.write(write_)
    file.close() 
    return mainData
