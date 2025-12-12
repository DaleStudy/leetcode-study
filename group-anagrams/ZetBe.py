'''
문제: 주어진 문자열들을 아나그램끼리 그룹화하는 코드를 작성하시오.
풀이: 각 문자열을 정렬하여 동일한 아나그램끼리 같은 키로 묶어 딕셔너리에 저장한 후, 그 값을 반환합니다.(이 때, 해당 문자열을 정렬함으로써 일종의 키 값을 만듭니다.)
시간복잡도: O(n * k log k) (n은 문자열의 개수, k는 각 문자열의 최대 길이)
공간복잡도: O(n)

'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            k = ''.join(sorted(i))
            if k not in d:
                d[k] = []
            d[k].append(i)
        return list(d.values())
    

