while True :
    name =  input("enter the name : ")
    name1 = input("enter the product name : ")
    total = 0

    while True :
    
     quantity = float(input("enter the quantity : "))
     amount = float(input("enter the amount : "))
     total += amount*quantity 
     repeate = input("do you want to add more items (yes \ no): ")
     if(repeate == "no" or repeate == "No"):
        break
    print("-"*40)
    print("name : ",name)
    print("product : ",name1)
    print("Amount to be paid : ",total)
    print("-"*40)
    print("*************HAPPY CUSTOMER*************")
    repeate1 = input("do you want to go to next customer ?(yes\ no) : ")
    if( repeate1 == "no" or repeate1 =="No"):
        break
