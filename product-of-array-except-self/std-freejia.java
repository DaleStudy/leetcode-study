class Solution {
    public int[] productExceptSelf(int[] nums) {
    int len = nums.length;
    int[] res = new int[len];
    int num = 1;

    for (int i = 0; i < len; i++) {
        res[i] = num;
        num *= nums[i];
    }
    num = 1;
    for (int i = len -1; i>=0; i--) {
        res[i] *= num;
        num *= nums[i];
    }

    for (int i = 0; i < len; i++) {
        System.out.print( res[i] + " ");
    }

    return res;
}
}
