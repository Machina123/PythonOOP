from collections.abc import Sequence

class SortedList(Sequence):

    def __init__(self, seq = None, key = None):
        if key is None:
           self.key = lambda a: a
        else:
            self.key = key

        if seq is None:
            self._list = []
        elif isinstance(seq, SortedList) and self.key == seq.key:
            self._list = seq._list
        else:
            self._list = sorted(list(seq), key = self.key)


    def __getitem__(self, item):
        return self._list[item]

    def __len__(self):
        return len(self._list)

    def add(self, other):
        index = self._find_index(other)
        self._list.insert(index, other)

    def clear(self):
        self._list = []

    def pop(self, i = -1):
        return self._list.pop(i)

    def extend(self, seq):
        for i in seq:
            self.add(i)

    def _find_index(self, item):
        l = 0
        r = self.__len__() - 1
        itemKey = self.key(item)
        while l <= r:
            m = (l+r) // 2
            if self.key(self._list[m]) < itemKey:
                l = m + 1
            else:
                r = m - 1
        return l

    def count(self, x):
        count = 0
        idx = self._find_index(x)
        length = self.__len__()
        while idx < length and self._list[idx] == x:
            count += 1
            idx += 1

        return count

    def remove(self, x):
        idx = self._find_index(x)
        if idx < self.__len__() and self._list[idx] == x:
            del self._list[idx]

    def remove_all(self, x):
        idx = self._find_index(x)
        length = self.__len__()
        while idx < length and self._list[idx] == x:
            del self._list[idx]

    def __str__(self):
        return str(self._list)

list = SortedList([1,1])
print(list._find_index(2))
list.add(2)
list.add(10)
list.add(-1)
list.add(3)
print(list)
print(list.count(1))
list.remove_all(1)
print(list)