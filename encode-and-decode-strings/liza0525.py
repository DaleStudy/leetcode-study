# 7기 풀이
# 시간 복잡도: O(n)
#  - 인코딩 디코딩 모두 문자열 리스트의 길이에 따라 시간 복잡도가 결정됨
# 공간 복잡도: O(1)
#  - 정답 변수인 res를 제외하고는 변수만 쓰임


DELIMITER = "^"


class Solution:
    def encode(self, strs):
        # DELIMITER를 사이에 두고 단어의 글자 수와 단어를 concat해서 저장한다.
        # 예) ["cat", "is", "cute"] -> "3^cat2^is4^cute"
        # 이렇게 해야 글자 수를 예측하고 split하기 쉬워진다. 
        return "".join(map(lambda x: f"{len(x)}{DELIMITER}{x}", strs))

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            # i번째 글자로부터 첫번째 DELIMITER가 나오는 인덱스를 j라고 칭함
            j = s.index(DELIMITER, i)
            word_len = int(s[i:j])  # DELIMITER 앞의 글자는 '글자 수'이므로 int로 변환
            word = s[j + 1:j + word_len + 1]  # i번째부터 글자 수 만큼 잘라서 word를 찾음
            res.append(word)
            i = j + word_len + 1  # 자른 이후의 index를 새로운 i로 설정하여 다음 글자 찾음
        return res
