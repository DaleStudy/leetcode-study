#이 문제를 해결하기 위해선 1)두 문자열의 길이가 같은지 확인(길이가 다르면 아나그램이 될 수 없음), 2)char_count딕셔너리를 사용하여 첫번째 문자열의 문자별 개수를 확인, 3)두번째 문자열을 순회하면서 각 문자의 개수를 하나씩 감소시킴, 4)만약 두번째 문자열에 첫번째 문자열에 없는 문자가 있거나, 어떤 문자의 개수가 음수가 되면(첫번째 문자열에 있는 문자가 두번째 문자열에 없다는 의미) 아나그램이 아님
class Solution:
    def isAnagram(self, s: str, t: str):
        # 두 문자열의 길이가 다르면 아나그램이 될 수 없음
        if len(s) != len(t):
            return False
        
        # 각 문자의 개수를 저장할 빈 딕셔너리
        char_count = {}
        
        # 첫 번째 문자열의 각 문자를 순회
        for i in s:
            #해당 문자가 없으면 0, 있으면 현재값 i를 반환하고, 각 문자의 개수 1을 더함
            char_count[i] = char_count.get(i, 0) + 1
        
        # 두 번째 문자열의 문자별 개수만큼 char_count딕셔너리에서 빼기
        for i in t:
            #첫번째 문자열에 없는 문자가 있는 경우
            if i not in char_count:
                return False

            char_count[i] -= 1
            #char_count가 음수이므로 첫번째 문자열에 있는 문자가 두번째 문자열에 없다는 의미
            if char_count[i] < 0:
                return False
        
        return True


        #시간 복잡도: O(n), n= 문자열의 길이
        #공간 복잡도: O(1), 입력 크기(n)가 아무리 커져도 사용하는 공간이 일정함(영어 소문자만 사용하므로 최대 26개의 키만 저장하면 됨)
