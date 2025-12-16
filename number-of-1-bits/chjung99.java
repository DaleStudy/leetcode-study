/**
 * time: O(log n)
 * space: O(1)
 */
class Solution {
    public int hammingWeight(int n) {
        int cnt = 0;
        while (n != 0){
            if (n % 2 == 1) cnt ++;
            n = (int) (n/2);
        }
        return cnt;
    }
}

