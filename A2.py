CP =int(input("Enter the cost price of the item: "))
SP= int(input("Enter the selling price of the item: "))

if SP > CP:
    profit = SP - CP
    print("Profit:", profit)

else:
    print("No profit in this item", " loss")