'''Implement a class called player that represents a cricket player.The player class should have a
method called play() which prints "The player is playing cricket.Derive two classes,Batsman and
Bowler,form the player class .overide the play()methods in each derived class to print" The batsman
is batting"and"the bowler is bowling",respectively.Write a program to create objects of both the
batsman and bowler classes and call the play() methode for each object.'''


#define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")

  #define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")

  #define the derived class Bowler
class  Bowler(player):
    def play(self):
        print("The bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method  for each object
batsman.play()
bowler.play()
        