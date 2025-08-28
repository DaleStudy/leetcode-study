class Solution {
  int lengthOfLIS(List<int> nums) {
    final stack = []; // S(n) = O(n)
    nums.forEach((x) { // T(n) = O(nlgn)
                int i = -1, j = stack.length - 1;
                while (i != j) { // O(lgn)
                    final int mid = j - ((j - i) >> 1);
                    if (stack[mid] < x) {
                        i = mid;
                    } else {
                        j = mid - 1;
                    }
                }
                if (++i == stack.length) {
                    stack.add(x);
                } else {
                    stack[i] = x;
                }
            });
    return stack.length;
  }
}