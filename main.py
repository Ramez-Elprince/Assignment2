import random 

FileData = open("ranks.txt", "r")

FileLines = FileData.read().split('\n')

FileData.close()

ranks = []
rank = []
power = []
number = []
rep = 10

for i in range(0, len(FileLines)):
    split = FileLines[i].split(',')
    if FileLines[i] == '':
        break

    ranks.append(split)
    rank.append(split[0])
    power.append(split[1])
    number.append(split[2])

print("Rank\t\t\tSkill\t\t\tNumber")
print("=============================================")

for x in range(0, len(rank)):
    if len(rank[x]) >= 12:
        tabs = '\t'
    elif len(rank[x]) >= 8:
        tabs = '\t\t'
    elif len(rank[x]) >= 4:
        tabs = '\t\t\t'
    else:
        tabs = '\t\t\t\t'
    print(rank[x], tabs, power[x], "\t\t", number[x], sep='')


print("=============================================")
print("\t\t\tLevel 3 Build Deck")
print("=============================================")
cards = []


for i in ranks:
  for j in range(0, int(i[2])):
    thing = i[0]
    cards.append(thing)
    countp = cards.count(int)

count = countp
random.shuffle(cards)
print(cards)


print("=============================================")
print("\t\t\tLevel 3 Dealing")
print("=============================================")



Player1 = input("Please Enter Your Name, Player One: ")
Player2 = input("Please Enter Your Name, Player Two: ")


def dealwar():
  random.shuffle(oldDeck)
  Deal1 = cards[0:int(len(cards)/2)]
  Deal2 = cards[0:int(len(cards)/2): len(cards)]
  for i in range(0, int(len(cards)/2)):
    Dealone = Deal1.pop()
    Dealtwo = Deal2.pop()
    print(Player1, "has been dealt: " + Deal1 + "\n" + Player2 + "has been dealt: " + Deal2)
    if Deal1 > Deal2:
      print(Player1 + "Won!")
      print("\n")
    elif Deal1 == Deal2:
      Dealone = Deal1.pop()
      Dealtwo = Deal2.pop()
      print(Player1 + "has player: " + Deal1 + "\n" + Player2 + "has been dealt: " + Deal2)
    if Deal1 > Deal2:
      print(Player1 + "Won!")
    else:
      print(Player2 + "Won!")
  else:
    print(Player2 + "Won!")
    print()

def finalscore():
  Score1 = len(Player1 + " Won!")
  Score2 = len(Player2 + " Won!")
  if Score1 > Score2:
    print(Player1 + " !")
  elif Score1 == Score2:
    print("Draw")
  else:
    print(Player2 + " ! ")

