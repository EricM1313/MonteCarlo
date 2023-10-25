import random as rand


def collect():
    count = 0
    collection = []
    while (len(set(collection)) < 10):
        collection.append(rand.randint(1,10))
        count +=1
    return count



def multipleTrials(trials):
    total = 0
    for t in range(trials):
        total += collect()
    return total/trials



print(multipleTrials(10000))