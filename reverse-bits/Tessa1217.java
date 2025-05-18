public class Solution {

    // 비트 연산자 사용
    public int reverseBits(int n) {
        int answer = 0;
        for (int i = 0; i < 32; i++) {
            answer <<= 1;
            answer |= (n & 1);
            n >>>= 1;
        }

        return answer;
    }

    // you need treat n as an unsigned value
    // O(1)
    // public int reverseBits(int n) {

    //     int answer = 0;

    //     String binary = Integer.toBinaryString(n);

    //     StringBuilder padded = new StringBuilder();
    //     for (int i = 0; i < 32 - binary.length(); i++) {
    //         padded.append('0');
    //     }
    //     padded.append(binary);

    //     return (int) Long.parseLong(padded.reverse().toString(), 2);

    // }
}

