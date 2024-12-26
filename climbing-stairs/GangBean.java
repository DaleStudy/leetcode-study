class Solution {
    public int climbStairs(int n) {
        /**
            1. Understanding
            - return the count of ways to climb up to top
            - way means the sequence of step count
            - each state, there can be 2 ways. first climb 1 step, second climb 2 step
            2. solve strategy
            - assume the count of ways to climb up to K th stairs is C[K].
            - then, C[0] = 1, C[1] = 1, C[2] = 2(because, you can up to 2nd stair from 0th stair and also from 1st stair.)
            - and C[3] = C[2] + C[1], C[4] = C[3] + C[2], ... etc...
            - so we can fomulate C[k] = C[k-1] + C[k-2]
            - iterate over 0 to n, you can caculate C[k].
            - and finally return C[n] is the answer.

            3. complexity
            - I answer to this part, along with coding upon each line description.
        */
        
        // 1. create array to demonstrate each stairs way count to reach that position.
        // the maximun step count is 45, so maybe there is over 2^32(approximately 2 billion; so i worry about the overflow), I assign long type array. Oh.. but i catch that return type of this method is integer, so i can assume that maximum value is under integer range. So, assign as integer.
        int[] c = new int[n + 1]; // the extra plus 1 means 0th stair state
        // space complexity: O(n)
        for (int stair = 0; stair <= n; stair++) { // time complexity O(n)
            if (stair <= 1) {
                c[stair] = 1; // O(1)
                continue;
            }
            c[stair] = c[stair-1] + c[stair-2]; // O(1)
        }

        return c[n];
    }
}

