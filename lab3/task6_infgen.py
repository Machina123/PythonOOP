import collections.abc as coll

def flatten(data):
    for item in data:
        if isinstance(item, coll.Iterable) and not isinstance(item, str):
            yield from flatten(item)
        else:
            yield item

mydata = ([1, "kot"], 3, (4, 5, [6, "7", {8, 9, "10", (11, 12)}]))

for myitem in flatten(mydata):
    print(myitem)