import random 

FileData = open("ranks.txt", "r")

FileLines = FileData.read().split('\n')

FileData.close()

idek = []

for o in range(10):
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
      thing = i
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


  def dealing():
    random.shuffle(cards)
    Deal1 = cards[0:int(len(cards)/2)]
    Deal2 = cards[int(len(cards)/2): len(cards)]
    for i in range(0, int(len(cards)/2) - 1):
      Dealone = Deal1.pop()
      Dealtwo = Deal2.pop()
      print(Player1, "has been dealt: ", Deal1[-1][0], "\n", Player2, "has been dealt: ", Deal2[-1][0])
      if Deal1 == Deal2:
        Dealone = Deal1.pop()
        Dealtwo = Deal2.pop()
        print(Player1, "has been dealt: ", Deal1, "\n", Player2, "has been dealt: ", Deal2)
    print(Player1, "Deck:")
    print('[', end='')
    for i in range(0, int(len(cards) / 2)):
        if i != int(len(cards) / 2) - 1:
            print("'" + cards[i][0] + "', ", end='')
        else:
            print("'" + cards[i][0] + "'", end='')
    print(']')
    print(Player2, "Deck:")
    print('[', end='')
    for i in range(int(len(cards) / 2), len(cards)):
        if i != len(cards) - 1:
            print("'" + cards[i][0] + "', ", end='')
        else:
            print("'" + cards[i][0] + "'", end='')
    print(']')


  def finalscore():
    Score1 = len(Player1 + " Won!")
    Score2 = len(Player2 + " Won!")
    if Score1 > Score2:
      print(Player1 + " !")
    elif Score1 == Score2:
      print("Draw")
    else:
      print(Player2 + " ! ")

  dealing()

  print("=============================================")
  print("\t\t\tLevel 4 Playing")
  print("=============================================")


  Pone = []
  Ptwo = []
  overflow = []


  for i in range(0, int(len(cards) / 2)):
      firstIndex = cards[int(len(cards) / 2)]
      if int(cards[0][1]) > int(firstIndex[1]):
          print(cards[0][0] + ' beats ' + firstIndex[0] + ', cards go to player 1.')
          Pone.append(cards[0])
          Pone.append(cards[int(len(cards) / 2)])
          cards.pop(0)
          cards.pop(int(len(cards) / 2))

      elif int(cards[0][1]) < int(firstIndex[1]):
          print(firstIndex[0] + ' beats ' + cards[0][0] + ', cards go to player 2.')
          Ptwo.append(cards[0])
          Ptwo.append(cards[int(len(cards) / 2)])
          cards.pop(0)
          cards.pop(int(len(cards) / 2))

      else:
          print('Tie!!  Both players show ' + cards[0][0] + '.  Added to the overflow deck.')
          overflow.append(cards[0])
          overflow.append(firstIndex)
          cards.pop(0)
          cards.pop(int(len(cards) / 2))


  print('Game Over.')
  print("there is", len(overflow), "cards in overflow deck")
  idek.append([o, len(Pone), len(Ptwo), len(overflow)])


print('Game Number \t\t Player 1 Cards \t\t Player 2 Cards \t\t Overflow Deck')
print('==================================================================================')
avgCard1 = 0
avgCard2 = 0
avgOverflow = 0
for i in range(len(idek)):
    print('\t', idek[i][0], '\t\t\t\t\t\t', idek[i][1], '\t\t\t\t\t\t', idek[i][2], '\t\t\t\t\t\t', idek[i][3], sep='')
    avgCard1 += idek[i][1]
    avgCard2 += idek[i][2]
    avgOverflow += idek[i][3]

avgCard1 /= idek[-1][0]
avgCard2 /= idek[-1][0]
avgOverflow /= idek[-1][0]

print('Average\t\t\t\t\t  ', round(avgCard1, 1), '\t\t\t\t  ', round(avgCard2, 1), '\t\t\t\t  ', round(avgOverflow, 1))