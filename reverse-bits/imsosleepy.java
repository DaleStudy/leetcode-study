// 스택으로 풀기보다 비트연산자로 풀이
// 스택을 사용할 때는 32자리의 불필요한 공간이 생긴다.
public class Solution {
    public int reverseBits(int n) {
        // n 이 십진수로 들어온다.(중요)
        int result = 0;
        for (int i = 0; i < 32; i++) {
            // 마지막 비트 확인
            // 홀수: 마지막 비트가 1 (n & 1 == 1)
            // 짝수: 마지막 비트가 0 (n & 1 == 0)
            int bit = n & 1; 
            // result를 왼쪽으로 1비트 이동하고, 추출한 비트를 추가
            // - result의 마지막 비트를 비우고 (<< 1)
            // - OR 연산(|)으로 추출한 비트를 추가
            result = (result << 1) | bit;

            // n을 오른쪽으로 1비트 이동하여 다음 비트를 준비
            // - n의 마지막 비트를 버리고, 상위 비트를 아래로 이동
            n >>= 1; 
        }
        return result;
    }
}
