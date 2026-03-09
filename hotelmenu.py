#define the restaurant
menu={
    'pizza':80,
    'pasta':50,
    'maggii':35,
    'salad':70,
    'burger':50,

}

#greet
print("welcome to blv restaurant")
print("pizza:Rs80\npasta:Rs50\nmaggi:Rs35\nsalad:Rs70\nburger:Rs50\n")
order_total=0
#70+50

item_1=input("enter the name of iteam you want to order:")
if item_1 in menu:
 order_total += menu[item_1]
 print(f"your item {item_1}has been added to your order")

else:
 print(f"ordered item {item_1} is not avaialable yet!")

another_order =input("do you want to add another item? (yes/no)")
if another_order == "yes":
  item_2 =input("enter the name of the item:")
  if item_2 in menu:
   order_total += menu[item_2]
   print(f"your item {item_2}has been added to your order")
  else:
    print(f"ordered item {item_1} is not avaialable yet!")

print(f"the total amount need to pay is{order_total}")
print("thankyou")