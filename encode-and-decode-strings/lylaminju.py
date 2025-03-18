# encode 메서드:
# 시간 복잡도: O(N)
#   - 각 문자열을 한 번씩 순회하며 길이와 내용을 처리하므로, 모든 문자열 길이의 합에 비례.
# 공간 복잡도: O(N)
#   - 인코딩된 결과 문자열을 저장하기 위해 추가 공간 사용.

# decode 메서드:
# 시간 복잡도: O(N)
#   - 인코딩된 문자열을 처음부터 끝까지 한 번 순회하며 파싱하므로, 입력 문자열 길이에 비례.
#   - s.find('#', i)는 인덱스 i부터 다음 #를 찾음.
#   - 여러 번의 find 호출이 있더라도 각 호출마다 전체 문자열을 다시 탐색하지 않고 이전 탐색 이후의 부분만 탐색하게 되어, 모든 find 호출을 합한 전체 탐색 거리는 인코딩된 문자열의 전체 길이 n에 해당함. 전체 시간은 O(n)에 수렴.
# 공간 복잡도: O(N)
#   - 디코딩된 문자열 리스트를 구성하기 위해 추가 공간 사용.


class Solution:
    """
    @param strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded_str = ""

        for s in strs:
            encoded_str += (str(len(s)) + "#" + s)
        
        return encoded_str

    """
    @param s: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s):
        decoded_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1
            decoded_list.append(s[i:i + length])
            i += length

        return decoded_list


def main():
    sol = Solution()

    # 테스트 예시 1
    input_strings1 = ["lint", "code", "love", "you"]
    print("===== Example 1 =====")
    print("Original: ", input_strings1)
    encoded_str1 = sol.encode(input_strings1)
    print("Encoded: ", encoded_str1)
    decoded_list1 = sol.decode(encoded_str1)
    print("Decoded: ", decoded_list1)
    print()

    # 테스트 예시 2
    input_strings2 = ["1234567890a", "we", "say", "#", "yes"]
    print("===== Example 2 =====")
    print("Original: ", input_strings2)
    encoded_str2 = sol.encode(input_strings2)
    print("Encoded: ", encoded_str2)
    decoded_list2 = sol.decode(encoded_str2)
    print("Decoded: ", decoded_list2)
    print()


if __name__ == "__main__":
    main()
