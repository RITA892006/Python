import random
choices = ["paper","stone","scissor"]
user_choices=input("paper,stone orscissor") 
computer_choices= random.choice(choices)
print("computer_choices is",computer_choices)
if user_choices==computer_choices:
 print("it's tie")
elif user_choices =="paper" and computer_choices =="scissor":
 print("computer win")
elif user_choices=="rock" and computer_choices=="paper":
 print("computer win")
elif user_choices=="scissor" and computer_choices=="rock":
 print("computer win")
else:
 print("you win!")