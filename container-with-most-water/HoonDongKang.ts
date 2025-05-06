/**
 * [Problem]: [11] Container With Most Water
 * (https://leetcode.com/problems/container-with-most-water/description/)
 */
function maxArea(height: number[]): number {
    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function twoPointerFunc(height: number[]): number {
        let left = 0;
        let right = height.length - 1;
        let result = 0;

        while (left < right) {
            const length = Math.min(height[left], height[right]);
            console.log(length);
            const area = (right - left) * length;

            result = Math.max(area, result);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return result;
    }

    return twoPointerFunc(height);
}
