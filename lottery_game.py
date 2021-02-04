# In a lottery game, there is a container which contains 50 balls numbered from 1 to 50. 
# The lottery game consists in picking 10 balls out of the container, 
# and ordering them in ascending order. 
# Write a Python function which generates the output of a lottery game (it should return a list). 
# Also describe which unit tests you could implement to test the output of your function.
import random
import typing
def lottery_game() -> typing.List[int]: 
    box = [i + 1 for i in range(50)]
    output = []
    random.seed(a = None)
    for i in range(10):
        index = random.randint(0,49-i) #mock this!
        output.append(box.pop(index))
    return sorted(output)

if __name__ == '__main__':
    print(lottery_game())
