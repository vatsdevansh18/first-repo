import random
#Damages
spider_attack=random.randint(1,100)
snake_attaack=random.randint(1,250)
levithan_attack=random.randint(50,300)
player_attack=random.randint(40,300)

#Health
spider_health=500
snake_health=600
levithan_health=1000
player_health=2500


#Block and Heal
block_amt=3
heal_amt=3


#Intro
name=input("Hello adventurer, What is your name?")
print(f"I hope you are ready to take on this adventure {name} and hope you dont die...")

#Story
print(f"As {name} was traversing through the world of corrupted coding, he encounters 3 paths.\n1.The den of the Deadly Spider\n2.The Snake of the Glory Hole.\n3.The King of the sea,Levithan.\nWhich path will you take? 1 or 2 or 3? ")
path=int(input())
print(f"Oh so you have chosen path {path}, Good Luck.")


#Conditions
if path==1:
    print(f"Welcome to the Spider's Den, {name}")
    print("You encountered a Spider!!!!!")
    while player_health>0 and spider_health>0:
        action=int(input(f"What do you want to do? \n1.Block\n2.Attack\n3.Heal"))
        if action==1:
            if block_amt!=0:
                print("You blocked spider's attack")
                block_amt-=1
                continue
            else:
                print("You dont have any blocks left.")
                continue
        elif action==2:
            player_attack=random.randint(40,500)
            spider_health-=player_attack
            print(f"You dealt {player_attack} points of DMG.\n Your Health: {player_health}\n Spider Health: {spider_health}")
            if spider_health<=0:
                break
        elif action==3:
            if heal_amt!=0:
                player_health+=300
                print(f"{name} used Heal. Your health is now: {player_health}")
                heal_amt-=1
            else:
                print("You dont have any heals left.")
                continue

        else:
            print("Invalid Option. Choose Again.")
        spider_attack=random.randint(100,400)
        print("Spider Attacksss")
        player_health-=spider_attack
        print(f"Your health: {player_health}\nSpider Health:{spider_health}")


if path==2:
    print(f"Welcome to the Snake's Glory Hole, {name}")
    print("You encountered a Giant Snake!!!!!")
    while player_health>0 and snake_health>0:
        action=int(input(f"What do you want to do? \n1.Block\n2.Attack\n3.Heal"))
        if action==1:
            if block_amt!=0:
                print("You blocked Snake's attack")
                block_amt-=1
                continue
            else:
                print("You dont have any blocks left.")
                continue
        elif action==2:
            player_attack=random.randint(40,500)
            snake_health-=player_attack
            print(f"You dealt {player_attack} points of DMG.\n Your Health: {player_health}\n Snake Health: {snake_health}")
            if snake_health<=0:
                break
        elif action==3:
            if heal_amt!=0:
                player_health+=300
                print(f"{name} used Heal. Your health is now: {player_health}")
                heal_amt-=1
            else:
                print("You dont have any heals left.")
                continue

        else:
            print("Invalid Option. Choose Again.")
        snake_health=random.randint(100,400)
        print("Snake Attacksss")
        player_health-=snake_attaack
        print(f"Your health: {player_health}\n Snake Health:{snake_health}")

if path==3:
    print(f"Welcome to the Levithnan's Ocean, {name}")
    print("You encountered a Levithan!!!!!")
    while player_health>0 and levithan_health>0:
        action=int(input(f"What do you want to do? \n1.Block\n2.Attack\n3.Heal"))
        if action==1:
            if block_amt!=0:
                print("You blocked Levithan's attack")
                block_amt-=1
                continue
            else:
                print("You dont have any blocks left.")
                continue
        elif action==2:
            player_attack=random.randint(40,500)
            levithan_health-=player_attack
            print(f"You dealt {player_attack} points of DMG.\n Your Health: {player_health}\n Leviathan Health: {levithan_health}")
            if levithan_health<=0:
                break
        elif action==3:
            if heal_amt!=0:
                player_health+=300
                print(f"{name} used Heal. Your health is now: {player_health}")
                heal_amt-=1
            else:
                print("You dont have any heals left.")
                continue

        else:
            print("Invalid Option. Choose Again.")
        levithan_attack=random.randint(100,400)
        print("Levithan Attacksss")
        player_health-=levithan_attack
        print(f"Your health: {player_health}\n Levithan Health:{levithan_health}")
else:
    print("Invalid.")