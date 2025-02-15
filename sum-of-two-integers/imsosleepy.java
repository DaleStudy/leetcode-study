// 비트 연산자를 이용한 문제가 접하기 어렵긴한데 자주 나오는 것 같다
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) { 
            int carry = (a & b) << 1; // AND 연산 후 왼쪽 쉬프트하여 자리 올림 계산
            a = a ^ b;  // XOR 연산으로 자리 올림 없는 덧셈 수행
            b = carry;  // 자리 올림을 다음 연산에 사용
        }
        return a;
    }
}

// 이런식으로도 풀리지만 이런 결과는 원하지 않을지 도..
class Solution {
    public int getSum(int a, int b) {
        return Math.addExact(a, b);
    }
}
