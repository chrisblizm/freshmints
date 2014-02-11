'''
Created on Feb 11, 2014

@author: cbush
'''
class CharCalculator:
    
    def __init__(self, exp=0, brawn=1, agility=1, intellect=1, cunning=1, willpower=1, presence=1):
        
        self.brawn = brawn
        self.agility = agility
        self.intellect = intellect
        self.cunning = cunning
        self.willpower = willpower
        self.presence = presence
        self.exp = exp
        
    def add_brawn(self, newBrawn=0):
        
        #while newBrawn > 0:
        #    self.exp = self.exp - (10 * (self.brawn + 1))
        #    newBrawn = newBrawn - 1
        #    self.brawn = self.brawn + 1
        self.increase_characteristic(newBrawn, 'brawn')
        
    def add_intellect(self, newIntellect=0):
        self.increase_characteristic(newIntellect, 'intellect')
            
    def increase_characteristic(self, value=0, name=None):
        
        if name:
            while value > 0:
                try:
                    increaseMe = getattr(self, name)
                    self.exp = self.exp - (10 * (increaseMe + 1))
                    value = value - 1
                    increaseMe = increaseMe + 1
                    setattr(self, name, increaseMe)
                except AttributeError:
                    value = 0
        else:
            pass