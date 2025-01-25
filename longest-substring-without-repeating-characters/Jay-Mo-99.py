﻿        #해석
        # 


        #Big O
        #- N: str s의 길이

        #Time Complexity: O(N) 
        #- start,end: 각각 최대 N번 움직임 -> O(N)
        #- set의 삽입, 삭제 -> O(1)

        #Space Complexity: O(N)
        #- chars: 최악의 경우 chars는 s의 모든 char을 저장한다 -> O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = set() #현 윈도우 내 중복 없이 존재하는 문자들을 저장하는 set
        start, end = 0, 0 # 슬라이딩 윈도우의 start 인덱스, end 인덱스 
        #end가 s의 마지막 인덱스에 도달할때까지 반복 
        while end < len(s): 
            #s[end]가 chars에 존재하면 
            if s[end] in chars: 
                #chars의 s[start]를 제거 
                chars.remove(s[start]) 
                #start를 오른쪽으로 이동, 윈도우 축소  
                start += 1 
            else: #s[end] 가 chars에 존재하지 않으면 
                chars.add(s[end]) #해당 s[end]를 chars에 추가해준다
                end += 1 #end를 오른쪽으로 옮겨 윈도우 확장 
                max_len = max(end - start, max_len) #start-end 계산하여 update 
        return max_len
    
mySolution = Solution()
mySolution.lengthOfLongestSubstring("pwwkew")

