"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Example 1:
    Input: List[str] = ["Hello","World"]
    Output: ["Hello","World"]

Example 2:
    Input: List[str] = []
    Output: []

Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.
"""
from typing import Final, List
import ast

"""
접근법:
    encode: 각 단어 앞에 글자수 + 구분자를 붙여 하나의 문자열로 이어 붙입니다. (예: ["Hello", "World"] -> "5#Hello5#World")
    decode: 문자열을 앞에서부터 읽으면서 구분자를 찾고, 그 앞의 숫자로 '글자수'를 알아낸 뒤 정확히 그 길이만큼만 잘라내어 원래 리스트로 복원합니다.

복잡도:
    시간 복잡도: O(N)
    공간 복잡도: O(N)
"""
class Solution:
    # 구분자 심볼
    DELIMITER: Final[str] = '#'

    """
    `글자수 + 구분자 + 단어` 조합으로 인코딩한 후 이어붙여 반환합니다.

    Example:
        Input: ["Hello","World"]
        Return: "5#Hello5#World"

        Input: []
        Return: ""

        Input: [""]
        Return: "0#"
    """
    def encode(self, strs: List[str]) -> str:
        parts: List[str] = (f"{len(s)}{self.DELIMITER}{s}" for s in strs)
        
        return ''.join(parts)
        

    """
    1. idx 이후에 구분자가 등장하는 인덱스를 찾습니다.
    2. 구분자 바로 앞에 있는 문자의 길이를 추출합니다.
    3. 구분자 이후 ~ 문자의 길이 만큼 슬라이스해서 대상 단어를 추출합니다. 추출한 단어는 result에 담습니다.
    4. result를 반환합니다.
    """
    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0

        while idx < len(s):
            delimiter_idx = s.find(self.DELIMITER, idx)
            length = int(s[idx : delimiter_idx])

            idx = delimiter_idx + 1 + length
            result.append(s[delimiter_idx + 1 : idx])
        
        return result
