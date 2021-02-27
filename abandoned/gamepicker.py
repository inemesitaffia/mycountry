"""gp."""
from secrets import SystemRandom
stilst = range(1, 9)
print(stilst)
startset = set(stilst)
chosennumbers = (list(startset))

#i = ""
#chosennumbers = SystemRandom().choice(range(1000, 250000))
nshuffles = SystemRandom().choice(range(9, 19))
print("number of shuffles is ", nshuffles)
while nshuffles > 0:
    SystemRandom().shuffle(chosennumbers)
    nshuffles = nshuffles-1
    pass
cou = 0
for i in chosennumbers:
    print("")
    cou = cou+1
    print(cou)
    print(i)

    # i=str(i)


print("")
print(chosennumbers)
print("")
