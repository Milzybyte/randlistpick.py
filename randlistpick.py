"""
Program: randlistpick.py
"""
from breezypythongui import EasyFrame
import random

n = ["Miles", "Alexa", "Andrew", "George", "James", "Kofi", "Kurt", "Letisha", "Michael", "Nicolas", "Stepanie", "Thomas"]

class RandListPick(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, "Random winner pick")
        
        self.addLabel("winner is",
                      row = 0, column = 0)
        
        self.nameF = self.addTextField(text = "",
                                   row = 0, column = 1)
                                      
        self.addButton(text = "Random Pick!",
                       row = 1, column = 0,
                       columnspan = 2,
                       command = self.randPick)
        self.lastWinner = ""
        
        
    def randPick(self):
        name = random.choice(n)
       
        while name == self.lastWinner:
            name = random.choice(n)
            
        self.nameF.setText(name)
        self.lastWinner = name
        
        
        
#Definition of the main() function
def main():
    """instantiantes and pops up the window"""
    RandListPick().mainloop()
    
if __name__ == "__main__":
    main()                      