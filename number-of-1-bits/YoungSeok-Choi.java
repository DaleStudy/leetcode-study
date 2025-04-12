// NOTE: 10진수를 2 진수로 변환
// O(logN)
class Solution {
    public int hammingWeight(int n) {
        int oneCnt = 0;

        while(n >= 1) {
            if((n % 2) == 1) {
                oneCnt++;
            }
            n = n / 2;
        }
        
        return oneCnt;
    }
}