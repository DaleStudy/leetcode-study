class Solution {
    public int hammingWeight(int n) {

        if (n == 1) {
            return 1;
        }

        int curr = n, result = 1;
        while (curr > 1) {
            if (curr % 2 == 1) {
                result++;
            }
            curr = curr / 2;
        }

        return result;
    }
}

