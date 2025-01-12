"""
	anagram은 sort하면 동일하다는 성질을 이용해서 
    sorted str을 key로 문자열 str배열을 value로 가지는 딕셔너리를 만든다
    ans은 컴프리헨션을 이용해 딕셔너리의 value를 배열에 넣어 만든다
    
    TC : O(WlogW * N)
		strs의 평균문자열길이 W, strs의 개수를 N이라고 할 떄
        sort의 시간복잡도 => WlogW
        for문 => N
    
    SC : O(W * N)
        anagrams가 차지하는 공간은 문자열의 길이와 개수에 비례한다

    
    - defaultdict 만들 때 인자로 빈배열([])이 아닌 타입(list)을 넣어줘야한다

    - 알고달레의 다른풀이로 문자열에 나오는 알파벳 빈도 수(count = [0] * 26)로 anagram을 판별하는 법도 있다
        딕셔너리의 key는 불변해야 하기 때문에 count를 튜플로 바꾸는 것 주의

"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        ans = [value for value in anagrams.values()]
        return ans
