'''
문제핵심 : palindrome인 부분 문자열의 개수를 세는 것임
해결방법 : 
1) 문자열의 각 위치를 palindrome 중심으로 생각함
2) 중심에서 양쪽으로 확장하면서 palindrome 인지 확인
3) 홀수 길이 palindrome (중심이 한 글자)과 짝수 길이 palindrome (중심이 두 글자 사이) 모두 확인

시간 복잡도: O(n²)
    외부 반복문이 n번 실행됨 (n은 문자열 길이)
    각 중심에서 최악의 경우 n번까지 확장할 수 있음
    따라서 총 시간 복잡도는 O(n × n) = O(n²)임

공간 복잡도: O(1)
    추가로 사용하는 메모리는 몇 개의 변수(count, left, right, palindrome_count)뿐임
    입력 크기에 관계없이 일정한 메모리만 사용하므로 O(1)임
'''

class Solution:
    def countSubstrings(self, s: str):
        count = 0  # 전체 회문 개수를 저장할 변수를 0으로 초기화
        
        for i in range(len(s)):  # 문자열의 각 인덱스를 순회
            # i번째 문자를 중심으로 하는 홀수 길이 회문들을 찾아서 개수를 더함
            count += self.expandAroundCenter(s, i, i)
            # i와 i+1 사이를 중심으로 하는 짝수 길이 회문들을 찾아서 개수를 더함
            count += self.expandAroundCenter(s, i, i + 1)
        
        return count  # 총 회문 개수 반환
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        palindrome_count = 0  # 이 중심에서 찾은 회문 개수를 0으로 초기화
        
        # 조건: 왼쪽 인덱스가 0 이상이고, 오른쪽 인덱스가 문자열 길이 미만이고, 
        # 왼쪽과 오른쪽 문자가 같을 때
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome_count += 1  # 회문을 하나 찾았으므로 개수 증가
            left -= 1   # 다음 확장을 위해 왼쪽 인덱스를 1 감소
            right += 1  # 다음 확장을 위해 오른쪽 인덱스를 1 증가
        
        return palindrome_count  # 이 중심에서 찾은 총 회문 개수 반환



