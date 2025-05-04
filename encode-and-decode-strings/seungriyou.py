# https://leetcode.com/problems/encode-and-decode-strings/

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        [Approach]
            (length + delimiter + string)의 형태로 str를 구성하면 length 만큼 포인터를 건너뛰며 확인할 수 있게 된다.
            delimiter는 숫자(length) 바로 뒤에 처음으로 나오는 문자여야 하므로, 숫자가 아닌 값으로 해야 한다. (나는 "."으로)
        """
        # length + delimiter + string
        return f"".join(str(len(s)) + "." + s for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []

        start = 0
        while start < len(s):
            # 1. start 이후에 나오는 첫 delimiter 위치 찾기
            # for delim in range(start, len(s)):
            #     if s[delim] == ".":
            #         break
            delim = s.find(".", start)

            # 2. 보고 있는 str의 length 구하기
            length = int(s[start:delim])

            # 3. 보고 있는 str의 다음 위치 구하기
            end = delim + 1 + length

            # 4. 현재 str 모으기
            strs.append(s[delim + 1:end])

            # 5. start를 end로 이동
            start = end

        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
