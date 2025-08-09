class Solution:
    """
    1. n이 11일때, 이진수로 변환해보면 1011이다. set bits는 1의 값을 찾는 것이기에 1을 카운트해준다.
    시간 복잡도 (Time Complexity):
        - bin(n): 정수를 이진 문자열로 변환 → O(log n)
            (n의 크기에 따라 필요한 비트 수만큼 연산함)
        - count('1'): 문자열에서 '1'의 개수를 세기 위해 전체 순회 → O(log n)
            (이진 문자열의 길이는 log₂(n)에 비례)
        최종 시간 복잡도: O(log n)

    공간 복잡도 (Space Complexity):
        - bin(n)의 결과로 생성된 이진 문자열을 저장 → O(log n)
        - 그 외 별도의 추가 공간 없음
        최종 공간 복잡도: O(log n)
    """
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
