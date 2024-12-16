from functools import reduce
from typing import List
from unittest import TestCase, main


class Solution:
    def encode(self, strs):
        return self.encode_with_base64(strs)

    def decode(self, str):
        return self.decode_with_base64(str)

    CSV_DELIMITER = ','

    # solve_1. ASCII
    """
    Runtime: -
    Time Complexity: O(n * m), n은 strs 배열의 길이, m은 strs 배열의 각 문자열들의 평균 길이
    Space Complexity: O(n * m), n은 strs 배열의 길이, m은 encode/decode된 문자열의 평균 길이
    Memory: -
    """
    def encode_with_ascii(self, strs: List[str]) -> str:
        result = []
        for str in strs:
            encoded_str = reduce(
                lambda acc, cur: acc + cur,
                map(lambda char: f'{ord(char)}'.zfill(3), str)
            )
            result.append(encoded_str)

        return Solution.CSV_DELIMITER.join(result)

    def decode_with_ascii(self, str: str) -> List[str]:
        encoded_strs = str.split(Solution.CSV_DELIMITER)
        result = []
        for encoded_str in encoded_strs:
            decoded_str = ''
            for i in range(0, len(encoded_str), 3):
                chunk = encoded_str[i: i + 3]
                decoded_str += chr(int(chunk))
            result.append(decoded_str)

        return result

    # solve_2. Base64
    """
    Runtime: -
    Time Complexity: O(n * m), n은 strs 배열의 길이, m은 strs 배열의 각 문자열들의 평균 길이
    Space Complexity: O(n * m), n은 strs 배열의 길이, m은 encode/decode된 문자열의 평균 길이
    Memory: -
    """
    BASE64_CHAR_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def encode_with_base64(self, strs: List[str]) -> str:
        result = []

        for str in strs:
            bin_converted_str = reduce(
                lambda acc, cur: acc + cur,
                map(lambda char: bin(ord(char))[2:].zfill(8), str)
            )

            encoded_str = ''
            for i in range(0, len(bin_converted_str), 6):
                chunk = bin_converted_str[i: i + 6].ljust(6, '0')
                base64_char = Solution.BASE64_CHAR_TABLE[int(chunk, 2)]
                encoded_str += base64_char
            encoded_str.ljust(4 - (len(encoded_str) % 4), '=')

            result.append(encoded_str)

        return Solution.CSV_DELIMITER.join(result)

    def decode_with_base64(self, str: str) -> List[str]:
        result = []

        encoded_strs = str.split(Solution.CSV_DELIMITER)
        for encoded_str in encoded_strs:
            encoded_str = encoded_str.rstrip('=')
            bin_converted_str = reduce(
                lambda acc, cur: acc + cur,
                map(lambda char: bin(Solution.BASE64_CHAR_TABLE.index(char))[2:].zfill(6), encoded_str)
            )

            decoded_str = ''
            for i in range(0, len(bin_converted_str), 8):
                chunk = bin_converted_str[i: i + 8].rjust(8, '0')
                decimal_value = int(chunk, 2)
                if decimal_value != 0:
                    decoded_str += chr(decimal_value)

            result.append(decoded_str)

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        input = ["lint", "code", "love", "you"]
        output = ["lint", "code", "love", "you"]
        solution = Solution()
        encoded = Solution.encode(solution, input)
        decoded = Solution.decode(solution, encoded)
        self.assertEqual(decoded, output)

    def test_2(self):
        input = ["we", "say", ":", "yes"]
        output = ["we", "say", ":", "yes"]
        solution = Solution()
        encoded = Solution.encode(solution, input)
        decoded = Solution.decode(solution, encoded)
        self.assertEqual(decoded, output)


if __name__ == '__main__':
    main()
