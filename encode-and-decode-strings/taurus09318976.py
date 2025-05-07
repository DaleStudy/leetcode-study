'''
목표 : 문자열 리스트를 하나의 문자열로 인코딩하고, 다시 원래 리스트로 디코딩하는 알고리듬을 만드는 문제임
핵심 : 문자열에 어떤 문자가 들어 있더라도 정확히 인코딩/디코딩할 수 있어야 함
해결법 : 각 문자열 앞에 길이를 붙여서 인코딩 함 

Example 1. 단계별 설명
입력: ["lint","code","love","you"]

인코딩 과정:
"lint" → 4:lint
"code" → 4:code
"love" → 4:love
"you" → 3:you

최종 인코딩 문자열: 4:lint4:code4:love3:you

디코딩 과정:
i=0 → : 위치 1, 길이 4 → 문자열 lint (i=5)
i=5 → : 위치 6, 길이 4 → 문자열 code (i=10)
i=10 → : 위치 11, 길이 4 → 문자열 love (i=15)
i=15 → : 위치 16, 길이 3 → 문자열 you (i=19)

최종 결과: ["lint","code","love","you"]

동작 원리 요약 
인코딩: 각 문자열 앞에 길이를 붙여서 혼동 없이 디코딩 가능함
디코딩: 길이 정보를 이용해 정확히 문자열을 추출함
'''


class Solution:
    def encode(self, strs):
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}:{s}")  # 각 문자열 앞에 길이 + ":"을 붙임
        return "".join(encoded)              # 모든 문자열을 하나로 합침

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            colon = s.find(":", i)         # s.find(":", i) : 현재 위치(i)부터 처음 나오는 :의 위치를 찾기
            length = int(s[i:colon])       # int(s[i:colon]) : 앞의 숫자를 문자열 길이로 변환
            i = colon + 1                  # 문자열 시작 위치로 이동
            decoded.append(s[i:i+length])  # s[i:i+length : 길이만큼 문자열을 잘라서 저장함.
            i += length                    # 다음 문자열의 시작 위치로 이동
        return decoded
