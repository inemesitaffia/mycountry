"""Pick a number, any number."""
from Crypto.Random import random as rn
import Crypto
Crypto.Random.atfork()
sinput = input('pick a number any number:')
if sinput.isdigit():
    pass
else:
    print("      !!@input error@!!")
    print("try entering a number instead")
    sinput = 0
    exit("\n        quit")

    pass
#sinput = int(sinput) + 1
#sinput = sinput+1
chosennumbers = list(range(1, int(sinput) + 1))
#i = ""
#chosennumbers = rn.choice(range(1000, 250000))
nShuffles = rn.choice(range(9, 19))
print("number of shuffles is ", nShuffles)
while nShuffles > 0:
    rn.shuffle(chosennumbers)
    nShuffles = nShuffles - 1

    pass

nHeadOfSnake = 10
CriticalLength = 22

if len(chosennumbers) > CriticalLength:
    stripped = chosennumbers[:nHeadOfSnake]
    chosennumbers[:nHeadOfSnake] = sorted(stripped)
    """s[i:j] = t"""

    pass
cou = 0
for i in chosennumbers:
    cou = cou + 1
    print("")
    print(cou)
    print(i)


print("")
print(chosennumbers)
print("")
