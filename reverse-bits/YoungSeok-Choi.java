
class Solution {
    public int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; i++) {
            // result변수 비트 왼쪽 한칸 시프트. LSB 는 0으로 초기화.
            result <<= 1;

            // n 변수의 가장 오른쪽 비트를(LSB) result 변수에 할당.
            result = result | (n & 1);

            // n 변수 오른쪽 시프트(넘어가는 비트는 무시)
            n >>>= 1;
        }

        return 0;
    }
}

class AnotherSolution {
    public int reverseBits(int n) {
        // NOTE: 이진 배열로변환 (음수의 경우 1로 비트가 표현되기 때문에 양수 경우만 처리.)
        String binary = String.format("%32s", Integer.toBinaryString(n)).replace(" ", "0");
        String reverse = new StringBuilder(binary).reverse().toString();

        // NOTE: int자료형으로 이진수 파싱을 할 때 표현범위 (+- 21억) 가 넘어서게 되면 오류 발생
        // java.lang.NumberFormatException: For input string:
        // "10111111111111111111111111111111" under radix 2
        // Long 자료형으로 안전하게 파싱해야함.
        return (int) Long.parseLong(reverse, 2);
    }

}