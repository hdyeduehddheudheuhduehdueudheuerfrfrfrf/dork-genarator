mport sys
import os
from dlist import dork

os.system("cls") # clears the screen

try:
    os.system('title Z3NToX - Simple Dork Generator')  # title of the terminal window
except:
    pass
   
class color:

   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print(color.BOLD + """\033[91m

 d8888b.  db .88b  d88.  .d88b.  d8888b.  db .d888b. d88888D d88888D 
88  `8D o88 88'YbdP`88 .8P  Y8. 88  `8D o88 88   8D VP  d8' VP  d8' 
88   88  88 88  88  88 88    88 88   88  88 `VoooY'    d8'     d8'  
88   88  88 88  88  88 88    88 88   88  88 .d~~~b.   d8'     d8'   
88  .8D  88 88  88  88 `8b  d8' 88  .8D  88 88   8D  d8'     d8'    
Y8888D'  VP YP  YP  YP  `Y88P'  Y8888D'  VP `Y888P' d8'     d8'     
                                              
\033[92mDork Generator
\033[92mAUTHOR : \033[93mD1MOD1877
\033[92mD1MOD SHOP WEBSITE : \033[93mhttps://d1modshop.ml/
\033[92mDISCORD SERVER : \033[93mhttps://discord.gg/fdU8KGrUu9
""" + color.END)

while True:
   try:
      url = input("\033[96mEnter a country's domain extension:\033[0m ") # asks for the domain extension which the dorks should use
      if not url:
         raise ValueError # raises an error if the input is left empty

      f = open("Latest Dorks.txt", "w+", encoding='utf8') # creates the file 
      countrydomain = dork.replace("countrydomain", "site:" + url) # replaces the "countrydomain" in dorklist.py with the entered input
      f.write(countrydomain) # writes the dorks in the "Latest Dorks" file

      print(color.DARKCYAN + "Dorks saved to \"Latest Dorks.txt\"" + color.END)
      done = input("Press \"Enter\" to exit")
      sys.exit()

   except ValueError:
         print("\033[91mError: Please enter a valid domain extension!") # prints the error 
