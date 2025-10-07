print("...........KALAYAN JWELLERS...............")
name = input("Enter the Name")
print("Name is : ",name)
gender= input("Enter the Gender")
print("Gender is :",gender)
Age = int(input("Enter the Age"))
print("Age is :",Age)

product= input("Enter the Product")
print("Product is:",product)
gram =int(input("Enter Product Gram:"))
Gold_Price=11190
print(f"Currect Gold 1 gram Prize:{Gold_Price}")
print(".......................")
Gold=gram*Gold_Price
print(f"Total gold Rate :{Gold}")

Making_Charges=845
Total_Making_Charges=gram*Making_Charges
print(f"Total Making Charges:{Total_Making_Charges}")

print("...........................")

Total_amount=Gold+Total_Making_Charges
print(f"Total Amount:{Total_amount}")


if gender=='M':
    if Age>= 65:
        if Total_amount >= 210000 and Total_amount <= 310000:
            Discount =Gold*20/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif Total_amount >= 310000 and Total_amount <= 510000:
            Discount =Gold*30/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif  Total_amount > 510000 :
            Discount =Gold*35/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        else:
            print(f"Total Final Amount :{Total_amount}")

    if Age < 65:
        if Total_amount >= 210000 and Total_amount <= 310000:
            Discount =Gold*10/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif Total_amount >= 310000 and Total_amount <= 510000:
            Discount =Gold*20/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif  Total_amount > 510000 :
            Discount =Gold*25/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        else:
            print(f"Total Final Amount :{Total_amount}")

if gender=='F':
    if Age>= 65:
        if Total_amount >= 210000 and Total_amount <= 310000:
            Discount =Gold*25/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif Total_amount >= 310000 and Total_amount <= 510000:
            Discount =Gold*35/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif  Total_amount > 510000 :
            Discount =Gold*40/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        else:
            print(f"Total Final Amount :{Total_amount}")
    if Age < 65:
        if Total_amount >= 210000 and Total_amount <= 310000:
            Discount =Gold*15/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif Total_amount >= 310000 and Total_amount <= 510000:
            Discount =Gold*25/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        elif  Total_amount > 510000 :
            Discount =Gold*30/100
            print(f"Discount Price :{Discount}")
            amount=Total_amount-Discount
            print(f" Total Amount :{Total_amount} - {Discount} ={amount}")
        else:
            print(f"Total Final Amount :{Total_amount}")
                     


