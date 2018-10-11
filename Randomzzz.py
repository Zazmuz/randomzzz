import time
import random

namelist = ["Elvina", "Sherry", "Evonne", "Ariane", "Dorie", "Pinkie", "Somer", "Soledad", "Digna", "Susana", "Lael",
            "Elias", "Cody", "Cyrus", "Anjanette", "Aubrey", "Earline", "Chan", "Kandice", "Bernadine", "Judi",
            "Leatrice", "Miguelina", "Libbie", "Ginger", "Karine", "Lorri", "Charlette", "Eartha", "Beverlee",
            "Lizabeth", "Judie", "Lennie", "Johnnie", "Laverna", "Orville", "Jamee", "Claretha", "Jami", "Philomena",
            "Cole", "Reid", "Cara", "Wanetta", "Lila"]
locationlist = ["the shop", "the airport", "work", "Cybercom", "a esports tournament"]
foodlist = ["moldy cheeseburger", "poisoned cupcake", "regular pbj-sandwich"]
eventlist = ["party", "swiming practice", "programming course", "family reunion"]
Name = input('What is your name?: ')
random_name = random.choice(namelist)
random_location = random.choice(locationlist)
random_food = random.choice(foodlist)
random_event = random.choice(eventlist)
if Name == "secret":
    print("This is a story about an human being named " + random_name + "!")
    print(
        "One day when " + random_name + " was at " + random_location + ", " + random_name +
        " had a weird feeling. It was probably the " + random_food + " from yesterdays " +
        random_event + ". Too bad " + "that " + random_name + " had eaten that.      ***THE END***")

else:
    time.sleep(0.5)
    print("Hello" + "," + " " + Name + "!")
    time.sleep(1)

Mood = input('How are you?: ')

for goodmode in ["good", "fine", "nice", "happy", "amused"]:
    if goodmode in Mood.lower():
        print("Good that you are " + goodmode.lower() + "!")
        break

temperature = float(input('What is the temperature?: '))

if temperature > 22:
  if temperature > 40:
        print("Wear nothing.")
  else:
        print("Wear shorts.")
else:
    print("Wear long pants.")
