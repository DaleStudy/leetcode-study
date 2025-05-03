class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        answer = ""

        # 문자열 앞에 "문자열길이 + :" 붙여서 인코딩 
        for i in strs:
            answer += str(len(i)) + ":" + i
        
        return answer

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s):    # 변수명str을 s로 수정
        # write your code here
        answer = []
        i = 0

        # ":"를 기준으로 앞에 숫자(문자열길이)만큼 끊어서 디코딩
        while i < len(s):
            j = i

            # 문자열길이가 한자리 이상일 수 있으니까 ":"를 기준으로 함
            while s[j] != ":":
                j += 1
                
            length = int(s[i:j])    # 문자열의 길이 추출
            answer.append(s[j+1:j+1+length])    # 길이만큼 문자열 추출해서 answer에 넣기
            i = j + 1 + length  # 잘라진 문자열 뒤로 이동

        return answer
