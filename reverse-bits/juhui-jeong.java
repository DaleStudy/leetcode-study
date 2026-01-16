/*
 * 시간 복잡도: O(1)
 * 공간 복잡도: O(1)
 */
class Solution {
    public int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>= 1;
        }
        return result;
    }
}

/*
 * 시간 복잡도: O(1)
 * 공간 복잡도: O(32)
 * 
 * 해당 코드로도 동작하지만 문자열 변환 -> 뒤집기 -> 다시 문자열 파싱의 과정을 거치지 않고
 * 비트를 조작하는 것이 문제의 의도에 더 부합함.
 *
class Solution {

    public static String toBinaryString(int value) {
        String str = Integer.toBinaryString(value);
        while (str.length() < 32) {
            str = "0" + str;
        }
        return str;
    }

    public int reverseBits(int n) {
        String binaryString = toBinaryString(n);
        String reversed = new StringBuilder(binaryString).reverse().toString();
        
        int result = Integer.parseUnsignedInt(reversed, 2);
        return result;
    }
}
 */
