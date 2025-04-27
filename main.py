import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,0,-1])
print("YOU have to choose: s=snake, w=water,g=gun Enter only the charcter: ")
youstr=input("Enter your choice: ")
you_dict={"s":1,"w":-1,"g":0}
reverse_dict={1:"snake",-1:"water",0:"gun"}
you=you_dict[youstr]
print(f"You choose: {reverse_dict[you]}\n Computer choose: {reverse_dict[computer]}")
if(computer==you):
    print("Match be draw")
else: 
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==0 and you==1):
        print("You lose!")
    elif(computer==0 and you==-1):
        print("You win!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    else:
        print("Something went wrong!!")