"""amount target."""
from secrets import SystemRandom

startset = {"1111", "2222", "3333", "4444",
            "5555", "6666", "7777", "8888", "9999"}
chosennumbers = (list(startset))

#i = ""
#chosennumbers = SystemRandom().choice(range(1000, 250000))
nshuffles = SystemRandom().choice(range(9, 99))
print("number of shuffles is ", nshuffles)
while nshuffles > 0:
    SystemRandom().shuffle(chosennumbers)
    nshuffles = nshuffles-1
    pass

for i in chosennumbers:
    print("")
    print(i)

    # i=str(i)


print("")
print(chosennumbers)
print("")
print("")
