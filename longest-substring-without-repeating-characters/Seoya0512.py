'''
set_arr(현재 윈도우)에 중복 없는 부분 문자열을 유지하며 가장 긴 길이를 갱신한다.

예) s="dvdf"
1. ['d']
2. ['d','v']
3. 중복 'd' 발생 → 앞에 있던 중복 문자(d)까지는 버리고, 그 뒤에 있는 문자(v)부터 다시 윈도우로 유지한다
4. 'f' 추가 → ['v','d','f']
5. 최종 max_length=3

Time Complexity: O(n^2)
- 문자열을 한 번 순회하지만, 매 단계마다 리스트에서 in, index, 슬라이싱이 선형 시간이어서 최악 O(n^2)

Space Complexity: O(n)
- 최악의 경우 윈도우가 길이 n까지 커질 수 있음
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_arr = []
        max_length = 0
        for char in s:
            if char not in set_arr:
                set_arr.append(char)
            else:
                # 중복 문자가 발견되면 처음 중복 문자의 인덱스를 찾아 그 이전까지 자르고 현재 문자 추가
                dup_idx = set_arr.index(char)
                set_arr= set_arr[dup_idx+1:]
                set_arr.append(char)
            max_length = max(max_length, len(set_arr))
        return max_length
