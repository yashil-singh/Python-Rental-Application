#importing python files
import contents
import userInputs
import datetime
    
#Calling getFileContents function form the contents file
fileContents = contents.getFileContents()

#Calling the returnDictionary function form the contents file
mainData = contents.returnDictionary(fileContents)

#Function to get the current date 
def getDate():
    date = datetime.datetime.now().date()
    return date

#Function to get the current time
def getTime():
    time = datetime.datetime.now().time().strftime("%H:%M:%S")
    return time

#Function to get the customer name
def getCusName():
    cusName = input("\nEnter your name: ")
    return cusName

#Function to get the customer contact number
def getCusNum():
    cusNum = input("\nEnter your contact number: ")
    return cusNum

#Function to show bill after renting process
def showBillToRent(costumesRented):
    #Taking user input for name and number
    cusName = getCusName()
    cusNum = getCusNum()

    #Getting the current date and time
    billDate = getDate()
    billTime = getTime()
    
    print("\n+================================================================================+")
    print("|\t\t\t\tInvoice(For 5 days)\t\t\t\t\t")   
    print("+--------------------------------------------------------------------------------+")
    print("| Name: ",cusName)
    print("| Number: ",cusNum)
    print("| Date: ",billDate)
    print("| Time: ",billTime)
    print("+================================================================================+")
    print("|","SN no.","Name","\t\t\t","Brand","\t\t","Quantity","\t","Price")
    print("+================================================================================+")
    total = 0

    #Printing the rented costumes using the costumesRented list
    for index in range(len(costumesRented)):
        id_ = int(costumesRented[index][0])
        cQuantity = int(costumesRented[index][1]) 
        name = mainData[id_][0]
        brand = mainData[id_][1]
        price = int(mainData[id_][2].replace("$","")) * cQuantity
        total = total + int(price)
                
        print("|",(index+1),"\t",name,"\t",brand,"\t",str(cQuantity),"\t\t",("$"+str(price)))

    total = "$"+str(total)
    print("")
    print("+--------------------------------------------------------------------------------+")
    print("|","Total Price:","\t\t\t\t\t\t\t",total)
    print("+--------------------------------------------------------------------------------+")
    print("| Notice: This bill is only upto 5 days of renting. After 5 days, fine will be\n| charged of $2 per costume per day.")
    print("+================================================================================+")
    print("")

    #Assinging the text file name to a variable
    dateAndTime = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
    fileName = "rent"+"_"+str(dateAndTime)+"_"+cusName+".txt"
    
    #Opening a text file
    file = open(fileName,"w")
    file.write("\n+================================================================================+\n")
    file.write("|\t\t\t\t\tInvoice(For 5 days)\t\t\t\t\t\n")   
    file.write("+--------------------------------------------------------------------------------+\n")
    file.write("| Name: "+cusName+"\n")
    file.write("| Number: "+cusNum+"\n")
    file.write("| Date: "+str(billDate)+"\n")
    file.write("| Time: "+str(billTime)+"\n")
    file.write("+================================================================================+\n")
    file.write("| SN no."+"\t"+"Name"+"\t\t\t"+"Brand"+"\t\t\t"+"Quantity"+"\t\t"+"Price"+"\n")
    file.write("+================================================================================+\n")
    total = 0

    #Printing the costumes rented using the costumesRented list
    for index in range(len(costumesRented)):
        id_ = int(costumesRented[index][0])
        cQuantity = int(costumesRented[index][1]) 
        name = mainData[id_][0]
        brand = mainData[id_][1]
        price = int(mainData[id_][2].replace("$","")) * cQuantity
        total = total + int(price)
                
        file.write("| "+str(index+1)+"\t\t"+name+"\t"+brand+"\t\t"+str(cQuantity)+"\t\t\t"+("$"+str(price))+"\n")

    total = "$"+str(total)
    file.write("\n")
    file.write("+--------------------------------------------------------------------------------+\n")
    file.write("| Total Price:"+"\t\t\t\t\t\t\t\t\t"+total+"\n")
    file.write("+--------------------------------------------------------------------------------+\n")
    file.write("| Notice: This bill is only upto 5 days of renting. After 5 days, fine will be\n| charged of $2 per costume per day.\n")
    file.write("+================================================================================+\n")
    file.close()

#Function to show bill after returning process
def showBillToReturn(costumesReturned):
    #Taking user input for name and number
    cusName = getCusName()
    cusNum = getCusNum()

    #Getting the current date and time
    billDate = getDate()
    billTime = getTime()

    #To validate the user input
    validReturnDays = False
    while(validReturnDays == False):
        #Exception handling for invalid input
        try:
            rentDays = int(input("\nEnter the number of days before returning the costume: "))
            if rentDays > 0:
                #Validating the user input and ending the loop
                validReturnDays = True
            else:
                print("\nInvalid Input. Please enter a positive value.")
        except:
            print("\nInvalid Input. Please enter the number of days the costume(s) has been rented.")
            
    #To check if the renting days is more than 5 days 
    if(rentDays <= 5):
        extraDays = 0
    else:
        #Calculating extra days
        extraDays = rentDays - 5
        
    print("\n+====================================================================+")
    print("|\t\t\t\tInvoice")   
    print("|--------------------------------------------------------------------|")
    print("| Name: "+cusName)
    print("| Contact number: "+cusNum)
    print("| Date: "+str(billDate))
    print("| Time: "+str(billTime))
    print("|", "Total no. of days rented: ",rentDays)
    print("+====================================================================+")
    print("|","SN no.","Name","\t\t\t","Brand","\t\t\t","Quantity")
    print("+====================================================================+")
    fine = 0

    #Printing the costumes returned using the costumesReturned list
    for index in range(len(costumesReturned)):
        id_ = int(costumesReturned[index][0])
        cQuantity = int(costumesReturned[index][1]) 
        name = mainData[id_][0]
        brand = mainData[id_][1]
        price = int(mainData[id_][2].replace("$","")) * cQuantity
        #Fine for a costume per day is 2
        fine += extraDays *(cQuantity * 2)
        print("|",(index+1),"\t",name,"\t",brand,"\t\t",str(cQuantity))
    
    fine = "$"+str(fine)
    print("")
    print("|--------------------------------------------------------------------|")
    print("|","Extra No. of days rented: ",extraDays)
    print("|","Fine: ",fine)
    print("|--------------------------------------------------------------------|")
    print("| Notice: Fine per costume per day is $2")
    print("+====================================================================+")
    print("")

    #Assinging the text file name to a variable
    dateAndTime = datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")
    fileName = "return"+"_"+str(dateAndTime)+"_"+cusName+".txt"
    
    #Opening a text file
    file = open(fileName,"w")
    file.write("+=============================================================+\n")
    file.write("| \t\t\t\t\tInvoice\t\t\t\t\t\n")   
    file.write("|-------------------------------------------------------------+\n")
    file.write("| Name: "+cusName+"\n")
    file.write("| Contact number: "+cusNum+"\n")
    file.write("| Date: "+str(billDate)+"\n")
    file.write("| Time: "+str(billTime)+"\n")
    file.write("| Total no. of days rented: "+str(rentDays)+"\n")
    file.write("+=============================================================+\n")
    file.write("| SN no."+"\t"+"Name"+"\t\t\t"+"Brand"+"\t\t\t"+"Quantity"+"\t\t"+"\n")
    file.write("+=============================================================+\n")
    fine = 0

    #Printing the costumes returned using the costumeReturned list
    for index in range(len(costumesReturned)):
        id_ = int(costumesReturned[index][0])
        cQuantity = int(costumesReturned[index][1]) 
        name = mainData[id_][0]
        brand = mainData[id_][1]
        price = int(mainData[id_][2].replace("$","")) * cQuantity
        #Fine for a costume per day is 2
        fine += extraDays *(cQuantity * 2)
        
        file.write("| "+str(index+1)+"\t\t"+name+"\t"+brand+"\t\t"+str(cQuantity)+"\n")
    
    fine = "$"+str(fine)
    file.write("\n")
    file.write("|-------------------------------------------------------------+\n")
    file.write("| Extra No. of days rented: "+str(extraDays)+"\n")
    file.write("| Fine: "+str(fine)+"\n")
    file.write("|-------------------------------------------------------------+\n")
    file.write("| Notice: Fine per costume per day is $2\n")
    file.write("+=============================================================+\n")
    file.write("")
    file.close()
