import unittest
import lottery_game
'''
    Explaination: 
    Due to my lottery_game() function includes random with seed of timestamp, 
    so it cannot be test directly.
    Therefore, I use stubs in unit tests that fixed the output value of random.randint() 10 times,
    then it can pop values for box list constantly.
    With this, I can test my function.
'''
class lotteryGameTest(unittest.TestCase):
    
    def test_lottery(self):
        random_numbers = [19,41,39,9,25,16,39,5,31,11]
        lottery_game.random.randint = lambda n, m : random_numbers.pop(0) #fixed output of randint
        self.assertListEqual(lottery_game.lottery_game(), [6,10,14,18,20,28,37,41,43,46])

    def test_lottery_repeated(self):
        random_numbers = [1,1,1,1,1,1,1,1,1,1]   
        lottery_game.random.randint = lambda n, m : random_numbers.pop(0) 
        self.assertListEqual(lottery_game.lottery_game(), [2,3,4,5,6,7,8,9,10,11])

    def test_lottery_ordered(self):
        random_numbers = [i for i in range(10)]
        lottery_game.random.randint = lambda n, m : random_numbers.pop(0) 
        self.assertListEqual(lottery_game.lottery_game(), [1,3,5,7,9,11,13,15,17,19])
