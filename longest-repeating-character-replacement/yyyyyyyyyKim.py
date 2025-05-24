class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # 슬라이딩 윈도우(투포인터)
        count = {}      # 문자 빈도수
        left = 0        # 왼쪽 포인터
        max_count = 0   # 현재 윈도우에서 최대 문자 빈도수
        answer = 0      # 가장 긴 동일 문자 부분 문자열의 최대 길이

        # 오른쪽 포인터를 한 칸씩 늘려가며 윈도우 확장
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1     # 현재 문자 카운트 증가
            max_count = max(max_count, count[s[right]])     # 가장 많이 등장한 문자 수 갱신

            # 윈도우길이(right-left+1) - 가장자주나온문자 빈도수 > k : 현재 윈도우에서 바꿔야하는 문자가 더 많으면 왼쪽 포인터 이동
            if (right-left+1) - max_count > k:
                count[s[left]] -= 1     # 왼쪽 문자 제거
                left += 1               # 왼쪽 포인터 오른쪽으로 한 칸 이동

            answer = max(answer, right-left+1)

        return answer
