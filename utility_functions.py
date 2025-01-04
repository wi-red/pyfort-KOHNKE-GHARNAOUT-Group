def introduction():
    return ("Hello player!\n\nYour goal is to access the treasure room. In order to do that you and your team will have to earn 3 keys by completing challenges.\n\nGood Luck !")

def compose_equipe():
    team=[]
    c=0
    c_2=0
    while True:
        try:
            equipe=int(input("How many players are on the team ? [1-3] : "))
            while equipe<1 or equipe>3:
                if equipe<1:
                    print("Invalid value! Your team must have at least one player ! \n")
                    equipe=int(input("How many players are on the team ? [1-3] : "))
                elif equipe >3:
                    print("Invalid value! Your team must have 3 players at maximum ! \n")
                    equipe=int(input("How many players are on the team ? [1-3] : "))
            if equipe >= 1 and equipe <= 3:
                for i in range(equipe):
                    print("------PLAYER", i+1,"------")
                    name=str(input("Enter your name : "))
                    profession=str(input("Enter your profession : "))
                    leader=False
                    if c<1:
                        leader_Q=str(input("Are you the team leader ? [Yes/No] : "))
                        while leader_Q!="Yes" and leader_Q!="No" and leader_Q!="yes" and leader_Q!="no" and leader_Q!="Y" and leader_Q!="N":
                            print("Invalid Input! Your answer should be 'Yes' or 'No'! ")
                            leader_Q=str(input("Are you the team leader ? [Yes/No] : "))
                        if leader_Q=="Yes" or leader_Q=="Y" or leader_Q=="yes":
                            leader=True
                            c+=1
                            c_2+=1
                    if c>1:
                        leader=False
                    team.append({ 'Name': name ,'Profession' : profession , 'Leader': leader, 'key_wons': 0  })
                if c==0:
                    print("\nPlayer 1 has been designated as the leader by default.\n")
                    team[0]["Leader"]=True
            return team
        except ValueError:
            print("Your value should be an integer. Please try again.")
    
#print(compose_equipe())

def challenges_menu():
    a=int(input("Choose a challenge.\n\n1.Mathematics Challenge\n2.Logic Challenge\n3.Chance Challenge\n4.Père Fouras' riddle\n\nYour choice is : "))
    if a==1:
        return "You chose the Mathematics Challenge"
    if a==2:
        return "You chose the Logic Challenge"
    if a==3:
        return "You chose the Chance Challenge"
    if a==4:
        return "You chose the Père Fouras' riddle"


def choose_player(team):
    for i in range(len(team)):
        if team[i]["Leader"]==True:
            print(f'{i+1}. {team[i]["Name"]} ({team[i]["Profession"]}) - Leader')
        else:
            print(f'{i+1}. {team[i]["Name"]} ({team[i]["Profession"]}) - Member')
    a=int(input("Enter the player's number: "))
    while a<1 or a>len(team):
        print(f"Invalid Value! The player's number must be between 1 and {i+1}")
        a=int(input("Enter the player's number: "))
    return team[a-1]
random_team=[{'Name': 'A', 'Profession': 'A', 'Leader': False, 'key_wons': 0}, {'Name': 'B', 'Profession': 'B', 'Leader': True, 'key_wons': 0}]
print(choose_player(random_team))