// link: https://leetcode.com/problems/product-of-array-except-self/submissions/1831301674/
// difficulty: Medium
class Solution1 {
    // Problem:
    // * return: array where answer[i] = product of all elements except nums[i]
    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity: O(N)
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        // prefixProds[i] = prod of all elements upto i (exclusive)
        int[] prefixProds = new int[n];
        for(int i = 0; i < n; i++) {
            if(i == 0) {
                prefixProds[i] = 1;
                continue;
            }

            prefixProds[i] = prefixProds[i-1] * nums[i-1];
        }

        // suffixProds[i] = prod of all elements from end to i (exclusive)
        int[] suffixProds = new int[n];
        for(int i = n - 1; i >= 0; i--) {
            if(i == n - 1) {
                suffixProds[i] = 1;
                continue;
            }

            suffixProds[i] = suffixProds[i+1] * nums[i+1];
        }

        // multiply prefix and suffix prods to find answers
        int[] answers = new int[n];
        for(int i = 0; i< n;i++) {
            answers[i] = prefixProds[i] * suffixProds[i];
        }

        return answers;
    }
}

// uses only 1 array whereas solution 1 uses 3
class Solution2 {
    // Problem:
    // * return: array where answer[i] = product of all elements except nums[i]
    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity: O(N)
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        // prefixProds[i] = prod of all elements upto i (exclusive)
        int[] answers = new int[n];
        for(int i = 0; i < n; i++) {
            if(i == 0) {
                answers[i] = 1;
                continue;
            }

            answers[i] = answers[i-1] * nums[i-1];
        }

        // use a single variable for suffix product
        int suffixProd = 1;
        for(int i = n - 2; i >= 0; i--) {
            suffixProd *= nums[i+1];
            answers[i] *= suffixProd;
        }

        return answers;
    }
}

