class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 2번째 풀이:  소중한 리뷰 감사합니다:)
        #<시간, 공간 복잡도를 줄일 수 있는 풀이- 정렬 없이>

        # 알파벳 26개로 구성된 정적 배열에 문자별 개수를 세어 비교 
        # 시간 복잡도: O(n)
        # 공간 복잡도: O(1) - input 길이와 관계없이 항상 26칸
        if len(s) != len(t):  # 길이가 다르면  바로 종료
            return False
        count_s = [0] * 26
        count_t = [0] * 26
        for elem in s:
            count_s[ord(elem) - ord('a')] += 1
        for elem in t:
            count_t[ord(elem) - ord('a')] += 1
        return count_s == count_t

# 첫번째 풀이
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # 정렬을 해서 anagram이면 정렬된 리스트의 원소가 동일
#         # 시간 복잡도: O(n log n) - 정렬, 공간 복잡도: O(n) - sorted로 list 생성
#         # 정렬 말고 다른 효율적 풀이가 있을까요?? 코멘트 많이 부탁드립니다~!!
#         return sorted(s) == sorted(t)
