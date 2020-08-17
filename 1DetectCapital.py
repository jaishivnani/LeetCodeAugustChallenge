#https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/

#Given a word, you need to judge whether the usage of capitals in it is right or not.
#We define the usage of capitals in a word to be right when one of the following cases holds:
#1All letters in this word are capitals, like "USA".
#2All letters in this word are not capitals, like "leetcode".
#3Only the first letter in this word is capital, like "Google".
#4Otherwise, we define that this word doesn't use capitals in a right way.

class Solution:
    def detectCapitalUse(self,word): #Method to detect capital use is correct or not
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word == word.capitalize():
            return True
        else:
            return False   #Use the code up to here if using in Leet Code i have created an object below for testing purpose.

    def __init__(self,word): #Init method to pass values by creating an object of Solution and passing word as Input.
        self.word = word

s1 = Solution('USA')

print(s1.detectCapitalUse('USA'))
print(s1.detectCapitalUse('usa'))
print(s1.detectCapitalUse('Usa'))
print(s1.detectCapitalUse('UsA'))
