'''
# 비트 연산 Bit Manipulation

## 이진수 덧셈 binary addition

이진수에서 두 비트를 더하기

1. XOR: 올림수를 제외한 합
2. AND << 1: 올림수를 계산
3. 1~2를 carry가 0일 때까지 반복

```
while b:
    carry = (a & b) << 1 # 올림수를 계산
    a = (a ^ b) # 합
    b = carry # 캐리가 남아있다면 계속 계산
```

## 32비트 오버플로우 제거

- 0xFFFFFFFF는 모든 비트가 1입니다.

Python의 int는 크기 제한이 없어서 연산 중 비트 수가 자동 확장됩니다.
MASK(0xFFFFFFFF)와 and 연산을 사용해 32비트 오버플로우를 방지합니다.

```
MASK = 0xFFFFFFFF
a = (a ^ b) & MASK # 32비트가 넘어가면 초과 비트가 제거됨
b = carry & MASK
```

## 음수 처리

- 0x7FFFFFFF(2147483647) 이하는 양수(Positive Number).
- 0x80000000(2147483648) 이상이면 음수(Negative Number)

`a > MAX_INT(0x7FFFFFFF)`인 경우, 32비트 환경에서 음수 값임을 의미합니다.

```
~(a ^ MASK)  # 32비트 음수 변환
```
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF 
        MAX_INT = 0x7FFFFFFF 
        
        while b:
            carry = (a & b) << 1 
            a = (a ^ b) & MASK  
            b = carry & MASK
        
        return a if a <= MAX_INT else ~(a ^ MASK) # a가 MAX_INT보다 크면 32비트 환경에서 음수이므로 변환
