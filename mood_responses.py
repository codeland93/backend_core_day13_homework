mood = "Happy, Sad, Excited, Overwhelmed" 

def mood_response(mood):
  if mood == "Happy":
   return "I'm extremely happy and feel great!"
  elif mood == "Sad":
   return "I'm very sad and feel down!"
  elif mood == "Excited":
   return "I'm very excited and feel awesome!"
  elif mood == "Overwhelmed":
   return "I'm a bit overwhelmed and feel like I need a minute!"
  else:
   return "I'm not sure what that mood means."