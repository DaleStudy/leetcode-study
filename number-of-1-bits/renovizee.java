

// tag renovizee 3week
// https://github.com/DaleStudy/leetcode-study/issues/232
// https://leetcode.com/problems/number-of-1-bits #191 #Easy
class Solution {
    // Solv2 :
    // 시간복잡도 : O(1)
    // 공간복잡도 : O(1)
    public int hammingWeight(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1) {
                result++;
            }
        }
        return result;

    }
//    // Solv1 :
//    // 시간복잡도 : O(log n)
//    // 공간복잡도 : O(1)
//    public int hammingWeight(int n) {
//        int result = 0;
//        int current = n;
//        while (current >= 2) {
//            if ((current % 2) == 1) {
//                result++;
//            }
//            current = current / 2;
//        }
//        if (current == 1) {
//            result++;
//        }
//        return result;
//
//    }
}

//-------------------------------------------------------------------------------------------------------------
// Java 문법 피드백
// 1) String s=Integer.toBinaryString(n); 숫자를 이진수 string으로 변환하는 방법
// 2) 숫자를 비트 연산하는 방법 n >> i 는 정수 n을 i 만큼 오른쪽으로 shift 함, ex) 1011 -> 0101
// 3) & 은 비트에서 and 연산이고 & 1은 마지막 비트 검사로 특수하게 사용됨, 둘다 1인 경우만 1
//-------------------------------------------------------------------------------------------------------------
