class Solution:
    def hasGroupsSizeX(self, deck):
        if len(deck) == 1:
            return False

        aDict = {}
        for card in deck:
            if card not in aDict:
                aDict[card] = 1
            else:
                aDict[card] = aDict[card] + 1

        minPartition = aDict[deck[0]]
        for key in aDict:
            partition = aDict[key]
            if minPartition > partition:
                minPartition = partition

        if minPartition == 1:
            return False
        for key in aDict:
            partition = aDict[key]
            remainder = partition % minPartition
            if remainder != 0 and partition % 2 != 0:
                return False   
        return True
    
##this fails on some edge case!