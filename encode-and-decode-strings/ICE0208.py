from typing import List


class Solution:
    """
    각 문자열을 '문자열 길이#문자열' 형식으로 인코딩한다.

    예:
    ["Hello", "World", ""]
    -> "5#Hello5#World0#"

    시간 복잡도: O(n)
    공간 복잡도: O(n)

    n은 모든 문자열 길이의 합이다.
    """

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            encoded.append(f"{len(word)}#{word}")

        return "".join(encoded)

    def decode(self, encoded_string: str) -> List[str]:
        decoded = []
        index = 0

        while index < len(encoded_string):
            delimiter_index = index

            # 문자열 길이와 실제 문자열을 나누는 '#'을 찾는다.
            while encoded_string[delimiter_index] != "#":
                delimiter_index += 1

            word_length = int(
                encoded_string[index:delimiter_index]
            )

            word_start = delimiter_index + 1
            word_end = word_start + word_length

            decoded.append(encoded_string[word_start:word_end])

            # 다음 문자열의 길이가 시작되는 위치로 이동한다.
            index = word_end

        return decoded
