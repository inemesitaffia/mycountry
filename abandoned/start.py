"""Set intersection."""
from secrets import SystemRandom

makestring = frozenset(range(1, 91))
nowstring = set()
for i in makestring:
    i = str(i)
    nowstring.add(i)


chosennumbers = SystemRandom().sample(list(nowstring), k=5)
mychoices = SystemRandom().choices(list(nowstring), k=5)

count = 0
mychoices = set(mychoices)
inter = mychoices.intersection(chosennumbers)
emptyhen = set()
while inter == (emptyhen):
    chosennumbers = SystemRandom().sample(list(nowstring), k=5)
    mychoices = SystemRandom().choices(list(nowstring), k=5)
    mychoices = set(mychoices)
    inter = mychoices.intersection(chosennumbers)
    count = count + 1
    print(count, sep="", end=", ")
    pass

print("")
print(chosennumbers)
print(mychoices)
print(inter)
print("")
