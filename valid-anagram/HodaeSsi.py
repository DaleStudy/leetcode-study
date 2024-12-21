class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetterDict = {}
        tLetterDict = {}

        for letter in s:
            sLetterDict[letter] = sLetterDict.get(letter, 0) + 1
        for letter in t:
            tLetterDict[letter] = tLetterDict.get(letter, 0) + 1

        if len(sLetterDict) != len(tLetterDict):
            return False

        for sKey in sLetterDict.keys():
            if sKey not in tLetterDict or sLetterDict[sKey] != tLetterDict[sKey]:
                return False

        return True

