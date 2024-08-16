class Solution {
    public int hammingWeight(int n) {
        /*
        Time complexity: O(n)
        Space complexity: O(1)
         */
        return Integer.bitCount(n);

        /*
        Time complexity: O(n)
        Space complexity: O(1)

        int output = 0;
        while (n > 0) {
            if ((n & 1) == 1) output += 1;
            n >>= 1;
        }
        return output;
        */
    }
}