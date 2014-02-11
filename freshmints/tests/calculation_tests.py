'''
Created on Feb 11, 2014

@author: cbush
'''
from django_nose import FastFixtureTestCase as TestCase
from freshmints.char_calculator import CharCalculator

class CalculationTests(TestCase):
    
    def testCalculateCharacteristicPricing(self):
        
        testXp = 175
        testBrawn = 1
        
        char_calculator = CharCalculator(exp=testXp, brawn=testBrawn)
        char_calculator.add_brawn(3)
        
        
        TestCase.assertEquals(self, char_calculator.exp, (testXp - 90))
        TestCase.assertEquals(self, char_calculator.brawn, 4)
        
        char_calculator.intellect = 3
        char_calculator.add_intellect(2)
        
        TestCase.assertEquals(self, char_calculator.exp, testXp - 180)
        TestCase.assertEquals(self, char_calculator.intellect, 5)