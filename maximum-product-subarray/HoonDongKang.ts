/**
 * [Problem]: [152] Maximum Product Subarray
 * (https://leetcode.com/problems/maximum-product-subarray/description/)
 */
function maxProduct(nums: number[]): number {
    // 시간복잡도 O(n^2)
    // 공간복잡도 O(1)
    function bruteForce(nums: number[]): number {
        let maxProduct = nums[0];

        for (let i = 0; i < nums.length; i++) {
            let product = 1;
            for (let j = i; j < nums.length; j++) {
                product *= nums[j];
                maxProduct = Math.max(maxProduct, product);
            }
        }

        return maxProduct;
    }

    // 시간복잡도 O(n)
    // 공간복잡도 O(1)
    function optimizedFunc(nums: number[]): number {
        let maxResult = nums[0];
        let minResult = nums[0];
        let result = nums[0];

        for (let i = 1; i < nums.length; i++) {
            const num = nums[i];

            if (num < 0) {
                [maxResult, minResult] = [minResult, maxResult];
            }

            maxResult = Math.max(num, num * maxResult);
            minResult = Math.min(num, num * minResult);
            result = Math.max(result, maxResult);
        }

        return result;
    }
}
