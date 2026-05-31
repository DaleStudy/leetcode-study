'''
문제: 유효한 팰린드롬, 해당 문자열이 팰린드롬인지 확인하는 문제
풀이: 대소문자 구분 없이 알파벳과 숫자만을 고려하여 팰린드롬인지 확인
시간복잡도: O(n)
    문자열을 한 번 순회하며 유효한 문자만 추출하고, 다시 한번 순회하며 팰린드롬 여부를 확인하므로 전체 시간복잡도는 O(n)이다.
공간복잡도: O(n)
    유효한 문자를 저장하기 위한 추가 리스트를 사용하므로 전체 공간복잡도는 O(n)이다.
사용한 자료구조: 리스트
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in s:
            if 65 <= ord(i) <= 90:
                string.append(i)
            elif 97 <= ord(i) <= 122:
                string.append(chr(ord(i)-32))
            elif 48 <= ord(i) <= 57:
                string.append(i)
            
        
        for i in range(len(string)):
            if string[i] != string[len(string)-1-i]:
                return False
        return True


