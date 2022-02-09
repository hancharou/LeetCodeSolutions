class Fancy:

    def __init__(self):
        self.sequence = []
        pass

    def append(self, val: int) -> None:
        self.sequence.append(val)

    def addAll(self, inc: int) -> None:
        self.sequence = list(map(lambda x: x+inc, self.sequence))

    def multAll(self, m: int) -> None:
        self.sequence = list(map(lambda x: x*m, self.sequence))

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.sequence):
            return -1
        return self.sequence[idx]

if __name__ == '__main__':
    fancy = Fancy()
    fancy.append(2) # fancy sequence: [2]
    fancy.addAll(3) # fancy sequence: [2 + 3] -> [5]
    fancy.append(7) # fancy    sequence: [5, 7]
    fancy.multAll(2) # fancy    sequence: [5 * 2, 7 * 2] -> [10, 14]
    fancy.getIndex(0) # return 10
    fancy.addAll(3) # fancy    sequence: [10 + 3, 14 + 3] -> [13, 17]
    fancy.append(10) # fancy    sequence: [13, 17, 10]
    fancy.multAll(2) # fancy    sequence: [13 * 2, 17 * 2, 10 * 2] -> [26, 34, 20]
    fancy.getIndex(0) # return 26
    fancy.getIndex(1) # return 34
    fancy.getIndex(2) # return 20