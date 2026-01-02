class Solution {
    public int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; i++) {
            //1. result 새 비트 공간 확보
            result = result << 1;

            //2. n의 마지막 비트 추출
            int last = (n & 1);

            //3. 마지막 비트 result에 추가
            result = result | last;

            //4. n 계산한 비트 제거
            n = n >> 1;
        }

        return result;
    }
}
