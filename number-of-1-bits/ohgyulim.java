class Solution {
    /* 시간 복잡도: O(1)
    * 
    * 공간 복잡도: O(1)
    */ 
    public int hammingWeight(int n) {
        return Integer.bitCount(n);
    }
}

