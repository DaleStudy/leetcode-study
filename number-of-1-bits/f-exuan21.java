// time : O(1) 
// space : O(1)

class Solution {
    public int hammingWeight(int n) {
        int count = 0;

        while(n != 0) {
            if((n&1) == 1) count++;
            n = n >> 1;
        }

        return count;
    }
}

