import time
import random
from tqdm import tqdm, trange

class Player:

   def __init__(self, gender, name, age):
       self.gender = gender
       self.name = name
       self.age = age

   def loading(self):
       pbar = tqdm(total = 100)
       for i in range(10):
           time.sleep(0.3)
           pbar.update(10)
       pbar.close()
       print("Player has been created!")

   def player_description(self):
       if self.age >= 18:
           print(f"You have created {self.age} years old {self.gender} adult named {self.name}")
       elif self.age < 18 and self.age >= 14:
           print(f"You have created {self.age} years old {self.gender} teenager named {self.name}")
       elif self.age < 14 and self.age >= 5:
           print(f"You have created {self.age} years old {self.gender} child named {self.name}")
       elif self.age <= 0:
           print("Age should be greater than 0")
       else:
           print(f"You have created {self.age} years old {self.gender} virtual baby named {self.name}")

class Baby(Player):

   def __init__(self, gender, name, age):
       Player.__init__(self, gender, name, age)

   def loading(self):
       pbar = tqdm(total = 100)
       for i in range(10):
           time.sleep(0.3)
           pbar.update(10)
       pbar.close()
       print("Your virtual baby has been created!")

   def feeding(self):
       self.age += 1
       print(f"Your virtual baby is {self.age} years old")

class Forest:

   def __init__(self, food1, food2, food3):
       self.food1 = food1
       self.food2 = food2
       self.food3 = food3

   def __str__(self):
       c_name = input("Enter the country that you want to create a forest in: ")
       time.sleep(1)
       return f"{self.food1, self.food2, self.food3} grow in the forest in {c_name}"

   def loading(self):
       pbar = tqdm(total = 100)
       for i in range(10):
           time.sleep(0.3)
           pbar.update(10)
       pbar.close()
       print("The most creative forest in the world has been created with some poisonous foods!")

   def mix_up(self):
       num = [1,2,3]
       foods = [self.food1, self.food2, self.food3]
       print(f"Your foods are: {self.food1}, {self.food2}, {self.food3}\nEach time one of them will be poisonous")
       time.sleep(1)
       choice = input("Type your selection: ")
       random.shuffle(num)
       dict_list = {}

       for i in range(len(num)):
           dict_list[foods[i]] = num[i]
       # select one food randomly each time. This food will be poisonous
       return random.randint(1,3) == dict_list[choice]


print("Welcome to Buse's imagination game ;)) \nBe ready and think twice before your selection!")

cont = True
while cont:
   time.sleep(2)
   print("Let's create a player. Please provide require information.")
   time.sleep(1)
   gender = input("Enter the gender: ")
   name = input("Enter the name: ")
   age = int(input("Enter the age: "))

   player = Player(gender,name,age)
   player.loading()
   time.sleep(1)
   player.player_description()

   time.sleep(3)
   print("\n")
   print("Let's create your virtual baby and start feeding him/her ")
   time.sleep(2)
   print("You can feed your virtual baby three different foods which you can find in the forest that you are going to create ")
   time.sleep(2)
   print("Be careful each time when you pick the food, one of them will be poisonous!")
   time.sleep(2)
   print("Let's create your virtual baby. Please provide require information.")
   time.sleep(2)
   gender = input("Enter the gender: ")
   name = input("Enter the name: ")

   baby = Baby(gender, name, age = 0)
   baby.loading()
   time.sleep(2)
   print("\n")
   print("Let's create your forest in any country and decided your foods in it")
   f1 = input("Enter 1. food: ")
   f2 = input("Enter 2. food: ")
   f3 = input("Enter 3. food: ")
   forest = Forest(f1, f2, f3)
   time.sleep(1)
   print(forest)
   forest.loading()
   time.sleep(2)
   print("\n")

   right = 0

   while True:
       if forest.mix_up() == False:
           baby.feeding()
           if baby.age == 5:
               print("You grown up your virtual baby. Congratulations!!!")
               break
       else:
           right += 1
           if right == 1:
               print("Try again!")
           elif right == 2:
               print("This is your last chance, try again!")
           else:
               print("You poisoned your virtual baby, Game over :(")
               break
   time.sleep(2)
   print("\n")
   ask = input("Do you want to play again? y/n: ")
   if ask == "y":
       continue
   else:
       cont = False



