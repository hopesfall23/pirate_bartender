##### William Palmer's Pirate Bartender Project ######

#We set a dictionary which values will be changed by our question_function()

results = {
    "strong" : False,
    "salty"  : False,
    "bitter" : False,
    "sweet"  : False,
    "fruity" : False,
}

#print(results["strong"]) #Tester to see if value changes



def question_function(name):
 """This function serves as a dictionary + loop. The parameter will be replaced by a key in the questions dictionary
 and its value will be printed. A loop will then check the conditions to return a string and enter the responses into a new dictionary"""

 questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
    
 qloop = True # This variable is required in creating a loop

 while qloop == True : #We will use breaks, so I just used this as a place holder
    
  print(questions[name]) #This will print the question(the value of [name]) 
  
  response = input()
  
  if response == 'yes' or response == 'Yes': #This will cover capitalization
      print("The bartender grins and reaches behind the bar, producing a bottle.")
      results[name] = True #This sets the value of results[name] to True, which will hold in the dictionary outside the function.
      break

  elif response == 'no' or response == 'No':
      print('The bartender nods, "So no ' + name +   ' drinks.."')
      break
      
  else:
      print("Are ye stoopid?! Yes or No?") #No breaks, we want it to loop indefinitly 
  
####----------------------------Ingredient Function-----------------------------------####
def drink_function():
 
 import random
    
 ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
 }
 
 drink=[] #This will hold the random ingredients
 num = 0 #This will count how many prints we do to stop an error
 
 if results["strong"] == True :
  num += 1
  drink.append(random.choice(ingredients["strong"]))
 
 if results["salty"] == True :
  num += 1
  drink.append(random.choice(ingredients["salty"]))
  
 if results["bitter"] == True :
  num += 1
  drink.append(random.choice(ingredients["bitter"]))

 if results["sweet"] == True :
  num += 1
  drink.append(random.choice(ingredients["sweet"]))

 if results["fruity"] == True :
  num += 1
  drink.append(random.choice(ingredients["fruity"]))
  
 if num == 0:
  print("Well you are a picky one aren't cha? Go drink somewhere else!")
  
 elif num == 1:
  print("The bartender grabs a " + drink[0] + " and mixes it all up!")
  
 elif num == 2:
  print("The bartender grabs a " + drink[0] + ', and a '  + drink[1] + " then mixes it all up!")
 
 elif num == 3:
  print("The bartender grabs a " + drink[0] + ', a '  + drink[1] + ', and a ' + drink[2] + " then mixes it all up!")
  
 elif num == 4:
  print("The bartender grabs a " + drink[0] + ', a '  + drink[1] + ', a ' + drink[2] + ', and a ' + drink[3] + " then mixes it all up!")

 elif num == 5:
  print("The bartender grabs a " + drink[0] + ', a '  + drink[1] + ', a ' + drink[2] + ', a ' + drink[3] + ', and a ' + drink[4] + " then mixes it all up!")




####---------------------No functions beyond this point-------------------------------####



## The following will run the code for each argument inside the function ##
 
question_function('strong')#Calls upon the function setting the argument 'strong' to the parameter name
question_function('salty')
question_function('bitter')
question_function('sweet')
question_function('fruity')

#print(results) #Tester to see if value changes

drink_function()


