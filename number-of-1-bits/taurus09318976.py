#이 문제는 1) 주어진 정수를 이진수로 변환, 2) 변환된 이진수에서 1의 개수를 세기 순서로 해결해야 함 

class Solution:
    def hammingWeight(self, n: int):
        count = 0
        while n:
            #n의 가장 오른쪽 비트가 1인지 확인, 1이면 count를 증가시킴
            if n & 1 == 1 :
                count += 1
            #다음 비트를 검사하기 위해 n을 오른쪽으로 1비트씩 시프트함
            n = n >> 1
        return count



# 테스트 케이스
solution = Solution()

# 테스트 1
test1 = 11
print(f"Expected: 3")
print(f"Result: {solution.hammingWeight(test1)}")

# 테스트 2
test2 = 128
print(f"Expected: 1")
print(f"Result: {solution.hammingWeight(test2)}")

# 테스트 3
test3 = 2147483645
print(f"Expected: 30")
print(f"Result: {solution.hammingWeight(test3)}") 


#cf. n & 0일 때 예: n = 1011
#  1011
#& 0000
#-----------
#  0000 -> 0과 AND 연산을 하면 어떤 수든지 결과가 항상 0이 됨
#반면에 n & 1을 사용하는 경우 1의 이진수 표현이 0001이기 때문에
#이 연산으로 n의 가장 오른쪽 비트만 확인할 수 있음.

#시간 복잡도 분석: O(log n)
    #while n 루프는 1의 개수와는 무관하게, n의 이진수 자릿수만큼 반복됨.
    #예: n = 128 (10000000)일 때 8번 반복
    #일반적으로 n의 이진수 자릿수는 log₂n
    #n & 1: O(1), n >> 1: O(1)의 경우 상수 시간만큼 걸림

#공간 복잡도 분석: O(1)
    #count 변수의 공간복잡도는 O(1)이며, n을 수정하면서 사용하므로 추가적인 배열이나 리스트가 필요하지 않음
