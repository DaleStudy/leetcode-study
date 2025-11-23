'''
Approach 1: Sorting
- 제일 먼저 생각나는 간단한 방법은 sorted 함수를 활용해서 분류해서 s 와 t가 동일한지 확인하는 방법입니다.
- 정렬메소드를 사용하면 n log n의 시간복잡도가 발생하는 것을 인지하고도 풀어봤습니다.

Time Complexity: O(n log n)
- 분류 정렬에서 O(n log n) 발생

Space Complexity: O(n)
- 분류 문자열을 생성하는 공간 때문에 O(n) 발생
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        if(sorted_s == sorted_t):
            return True
        else: 
            return False

'''
Approach 2: 빈도수 카운팅
- 두 문자열의 길이를 먼저 비교해서 다르면 False를 반환해서 1차 필터링
- count 딕셔너리를 생성해서 s 문자열의 빈도수를 카운팅
- t 문자열을 순회하면서 딕셔너리에 포함되어 있으면 카운팅을 감소시키고, 값이 없으면 False를 반환


Time Complexity: O(n)
- 두 문자열을 각각 순회하면 딕셔너리 생성, 빈도수 카운팅 및 감소 에서 O(n) 발생

Space Complexity: O(n)
- count 딕셔너리 저장 공간 때문에 O(n) 발생
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 길이가 일치하지 않으면 False 
        if len(s) != len(t):
            return False
        # 문자 개수 카운트
        count = {}
        for val in s:
            count[val] = count.get(val, 0) + 1
        for val in t:
            if val not in count:
                return False
            count[val] -= 1
            # 예시 : s = "aacc", t = "ccac" 인 경우 count[val] 이 음수가 될 수 있음
            if count[val] < 0:
                return False
        return True
