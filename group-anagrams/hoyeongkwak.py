'''
m : 문자열 길이
n : 반복
time complexity : O(m * n * log m)
space complexity : O(m * n)
algorithm : sort, hash, 
각 문자열에 대해서 정렬을 하고, 정렬을 했을 때 동일한 문자에 대해서 hash table에 정렬 전 문자열을 추가
그리고 마지막에 list 형태로 hash table의 value에 대해서 돌려 준다
nat -> ant
tan -> ant
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strResult = {}
        for word in strs:
            sortedStr = ''.join(sorted(word))
            if sortedStr not in strResult:
                strResult[sortedStr] = []
            strResult[sortedStr].append(word)
        return list(strResult.values())
