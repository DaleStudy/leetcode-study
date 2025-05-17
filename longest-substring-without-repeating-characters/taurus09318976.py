'''
해결 방법 : 
1) 슬라이딩 윈도우 기법을 사용해 중복 없는 가장 긴 부분 문자열을 찾음
2) char_index 딕셔너리로 각 문자의 마지막 등장 위치를 추적함
3) 중복 문자를 발견하면 start를 중복 문자의 다음 위치로 이동시킴

시간 복잡도: O(n) 
    문자열을 한 번씩 순회
공간 복잡도: O(min(m, n)) 
    (m=문자 집합 크기, 보통 O(1)로 간주)

Example 1.의 경우 s = "abcabcbb"

단계	end	문자	start	char_index	                max_length
0	    0	a	    0	    {'a':0}	                    1   
1	    1	b	    0	    {'a':0, 'b':1}	            2
2	    2	c	    0	    {'a':0, 'b':1, 'c':2}	    3
3	    3	a	    1	    {'a':3, ...}	            3
4	    4	b	    2	    {'b':4, ...}	            3
5	    5	c	    3	    {'c':5, ...}	            3
6	    6	b	    5	    {'b':6, ...}	            3
7	    7	b	    7	    {'b':7, ...}	            3

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 각 문자의 최근 위치 저장
        start = 0         # 현재 윈도우 시작 인덱스
        max_length = 0    # 최대 길이
        
        # 문자열 끝까지 순회
        for end in range(len(s)):
            # 중복 문자 확인 -> start 갱신 & 현재 문자 위치 기록          
            if s[end] in char_index and char_index[s[end]] >= start:
                # 중복 문자 발견: 시작점을 중복 문자 다음으로 이동
                start = char_index[s[end]] + 1
            # 현재 문자의 위치 갱신
            char_index[s[end]] = end
            # 현재 윈도우 길이 계산
            current_length = end - start + 1
            if current_length > max_length:
                # max_length 갱신
                max_length = current_length
        
        return max_length


  