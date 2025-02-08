'''
TC : O(n) 
	문자열 s를 총 한번 순회한다
SC : O(1)
	최대 26개의 글자를 딕셔너리에 저장한다
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_len = 0
        max_cnt = 0
        substr_len = 0
        # 문자열 s에 대한 해시테이블을 만들고 초기 값을 0으로 설정
        dic = {char : 0 for char in s}

        # 기본적으로 end를 오른쪽으로 이동시키는 방향
        for end in range(len(s)):
            dic[s[end]] += 1

            # 현재까지의 최다 빈도 글자수 계산
            max_cnt = max(max_cnt, dic[s[end]])

            # 현재 부분 문자열 안에서(즉 end가 고정된 상태에서)
            # 바꿀 수 있는 글자의 개수가 k에 못미친다면
            # start를 오른쪽으로 한칸 당긴다
            if end - start + 1 - max_cnt > k:
                dic[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
