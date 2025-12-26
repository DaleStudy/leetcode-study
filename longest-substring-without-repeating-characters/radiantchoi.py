class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 문자열 전체를 순회, 서브스트링이란 서로 붙어 있는 문자열
        # 글자를 볼 때 현재 모아둔 글자 모음에 중복 글자가 있다면?
        # 일단 지금까지의 길이 업데이트
        # 중복된 글자가 등장한 인덱스 체크
        # 현재 모아둔 문자열의 길이에서 해당 인덱스까지의 "머리"를 덜어내고 지금 보는 문자를 더해서, 서브스트링을 이어나감

        current = {}
        tuning = 0
        result = 0

        for (index, letter) in enumerate(s):
            if current.get(letter, index) < index:
                result = max(result, len(current))

                tail_of_head = current[letter]

                new_current = {}
                for key in current:
                    if current[key] > tail_of_head:
                        new_current[key] = current[key]
                
                current = new_current
            
            current[letter] = index
        
        result = max(result, len(current))
            
        return result
