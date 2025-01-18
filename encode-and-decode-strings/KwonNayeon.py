"""
Constraints:
1. 0 <= strs.length <= 200
2. 0 <= strs[i].length <= 200
3. strs[i]는 유니코드 문자들로만 구성됨
4. encode된 string은 반드시 decode 가능해야 함

Time Complexity: O(n)

Space Complexity: O(n)

풀이방법: 
- encode: 각 문자열 뒤에 '#' 추가하여 하나로 합침
- decode: '#'을 기준으로 문자열 분할

Further consideration:
- 현재 방식은 입력 문자열에 '#'이 포함된 경우 문제 발생 가능
- 개선 방법: 문자열 길이 + 구분자 + 문자열 형식 사용
 예: ["Hello", "World"] -> "5#Hello5#World"
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    Examples:
        input: ["Hello", "World"]
        output: "Hello#World"
    """
    def encode(self, strs):
        result = ""
        for s in strs:
            result = result + s + "#"
        return result[:-1]

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    Examples:
        input: "Hello#World"
        output: ["Hello", "World"]
    """
    def decode(self, str):
        return str.split("#")
