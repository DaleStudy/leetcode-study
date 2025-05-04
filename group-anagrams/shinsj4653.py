"""
[문제풀이]
# Inputs
- 문자열 배열 strs
# Outputs
- anagram 끼리 그룹핑하여 배열 return
# Constraints
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
# Ideas
하나를 기준으로 두고 나머지 요소들을 탐색
1. 왠지 bfs느낌?
한 기준 두고, 그 기준이랑 같은 요소 찾아서 묶기
-> 묶여진 요소는 visited true로 마킹
visited 가 모두 true면 탐색 끝

같은 anagram인지는 정렬로 파악 가능

위의 방법으로 하니 시간초과 발생
-> 기준이 되는 녀석 고르고, 그 녀석의 anagram찾는 과정이 모두 for문이라 비효율적인듯

2. 한번의 for문으로 되나?
for문 돌며 defaultdict에
만약 dict에 없는 키(문자열 sort된 값)라면 키 등록하고, value에 원래 값 삽입
있는 키라면 그 키의 value에만 삽입
-> O(n)으로 가능할듯

[회고]

"""

# 첫 제출 - 테케만 정답. 시간초과
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        n = len(strs)
        v = [False for _ in range(n)]


        while not all(v):
            q = []
            for idx, s in enumerate(strs):
                if not v[idx]:
                    q.append(strs[idx])
                    v[idx] = True
                    break

            for idx, vv in enumerate(v):
                if not vv and sorted(strs[idx]) == sorted(q[-1]):
                    q.append(strs[idx])
                    v[idx] = True

            ret.append(q)

        return ret

# 두 번째 제출 - 정답
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        dic = defaultdict(list)

        for s in strs:
            dic[str(sorted(s))].append(s)

        for v in dic.values():
            ret.append(v)

        return ret

