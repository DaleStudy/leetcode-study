class Solution:
    def reverseBits(self, n: int) -> int:
        # 이진수로 변환한 후 '0b' 제거
        binary = bin(n)[2:]
        # 32비트 길이에 맞게 앞쪽에 0을 채움
        binary = binary.zfill(32)
        # 이진수를 뒤집음
        reversed_binary = binary[::-1]
        # 뒤집힌 이진수를 정수로 변환하여 반환
        return int(reversed_binary, 2)


# 시간 복잡도: O(32)
# - bin(): O(32)
# - zfill(32): O(32)
# - 문자열 뒤집기 [::-1]: O(32)
# - int(문자열, 2): O(32)
# 총합: O(32) (상수 시간으로 간주 가능)

# 공간 복잡도: O(32)
# - 이진 문자열(binary)와 뒤집힌 문자열(reversed_binary)을 저장하므로 O(32).


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            # result를 왼쪽으로 1비트 이동하고 n의 마지막 비트를 추가
            result = (result << 1) | n & 1
            # n을 오른쪽으로 1비트 이동
            n >>= 1

        return result
    

# 시간 복잡도: O(32)
# - 반복문이 32번 실행되며 각 작업(비트 이동 및 OR 연산)은 O(1).
# 총합: O(32) (상수 시간으로 간주 가능)

# 공간 복잡도: O(1)
# - 추가로 사용하는 변수 result와 n만 저장하므로 상수 공간.
