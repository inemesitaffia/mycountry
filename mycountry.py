"""order of nations."""
from secrets import SystemRandom
thelist = [line.rstrip() for line in open('countriescleanednoextras.txt')]
sett = set(thelist)
mylist = list(sett)
#i = ""
#chosennumbers = SystemRandom().choice(range(1000, 250000))
nShuffles = SystemRandom().choice(range(9, 19))
while nShuffles > 0:
    SystemRandom().shuffle(mylist)
    nShuffles = nShuffles - 1

    pass
print("")
cou = 0
for i in mylist:
    cou = cou + 1

    print(cou, end="")
    print("  ", end="")
    print(i)
    pass


print("")
print(mylist)
print("")
