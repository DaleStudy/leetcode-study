class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        인코딩 함수
        방식: %를 사용해 문자열의 길이 + % + 문자열로 인코딩

        Args:
            strs (list[str]): 인코딩할 문자열 목록

        Returns:
            str: 인코딩된 문자열
        """
        return "".join(f"{len(s)}%{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        """
        디코딩 함수
        시간복잡도: O(N)

        Args:
            s (str): 디코딩할 문자열

        Returns:
            list[str]: 디코딩된 문자열 목록
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res
