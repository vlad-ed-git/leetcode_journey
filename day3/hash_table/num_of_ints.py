class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        stripped = {}
        i = 0
        for c in word:
            if c in {"0":1, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1}:
                if i in stripped:
                    if stripped[i] == "0":
                        stripped[i] = c
                    else:
                        stripped[i] = stripped[i] + c
                else:
                    stripped[i] = c
            else:
                i = i + 1
        counter = {}
        for key in stripped:
            if stripped[key] not in counter:
                counter[stripped[key]] = 1
            else:
                counter[stripped[key]] = counter[stripped[key]] + 1
        return len(counter)