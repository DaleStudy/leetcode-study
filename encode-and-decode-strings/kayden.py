class Solution:

    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def encode(self, strs):
        res = ""
        for s in strs:
            size = len(s)
            res += str(size) + "#" + s  # 문자열 크기와 실제 문자열 사이에 구분자 '#'를 추가

        return res

    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    def decode(self, s):
        idx = 0
        limit = len(s)
        res = []

        while idx < limit:
            # 문자열 길이 파싱
            j = idx
            while s[j] != '#':  # 구분자 '#'를 찾아 문자열 길이를 추출
                j += 1
            num = int(s[idx:j])
            idx = j + 1  # '#' 다음부터 실제 문자열 시작

            # 실제 문자열 추출
            text = s[idx:idx + num]
            res.append(text)
            idx += num

        return res
    