import copy
userInputName=""
userInputQuantity=""
userInputPrice=""
netAPayer=0

myBillList=[]

myFournitures = {
"name" : "<empty>",
"price" :"0",
"quantity" : "0"
}

print("Bonjour")

for key, value in myFournitures.items():
    print("{} : {}".format(key,value))
    
    
while ((userInputName==userInputPrice==userInputQuantity=="") or (userInputName==""or userInputPrice=="") or (userInputQuantity=="" or userInputName=="") or(userInputPrice=="" or userInputQuantity=="") or( userInputName=="" and userInputQuantity=="") or (userInputName==""and userInputPrice=="") or (userInputPrice=="" and userInputQuantity=="")):    
    userInputNumberOfItems=int(input("Combien de produits souhaitez-vous renseigner ?"))
    for x in range(0,userInputNumberOfItems):
        userInputName=input("Veuillez saisir le nom du produit: ")
        userInputPrice=input("Quel est son prix en FCFA ? :")
        userInputQuantity=input("Quelle quantité a été prise ? :")
        if ((userInputName==userInputPrice==userInputQuantity=="") or (userInputName==""or userInputPrice=="") or (userInputQuantity=="" or userInputName=="") or(userInputPrice=="" or userInputQuantity=="") or( userInputName=="" and userInputQuantity=="") or (userInputName==""and userInputPrice=="") or (userInputPrice=="" and userInputQuantity=="")): 
            print("Attention de ne laisser aucune case vide !")
        
        prixParProduit=int(userInputPrice)*int(userInputQuantity)

            
        currentFournitures=copy.deepcopy(myFournitures)
        currentFournitures["name"]=userInputName
        currentFournitures["price"]=int(userInputPrice)
        currentFournitures["quantity"]=int(userInputQuantity)
        currentFournitures["total"]=prixParProduit
       
        
        netAPayer+=currentFournitures["total"]

        myBillList.append(currentFournitures)  
    
            
    for items in myBillList:
        for key, value in currentFournitures.items():
            print("{} : {}".format(key,value))
            print("-----")

print(myBillList)
print("Vous allez devoir payer : {} F CFA ".format(netAPayer))


    

    

