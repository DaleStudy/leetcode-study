// 가장 먼저 떠오른 방법이지만 권장되지 않는 방법일 것 같음
// 변환된 이진 문자열을 치환하는 방식은 O(K + logN)이다.
class Solution {
    public int hammingWeight(int n) {
        return Integer.toBinaryString(n).replace("0", "").length();
    }
}

// 그냥 비트 연산자로 푸는게 최고인것 같다.
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count += (n & 1); // 마지막 숫자가 1인지 확인
            n >>>= 1; // n을 1칸 오른쪽 이동
        }
        return count;
    }
}
