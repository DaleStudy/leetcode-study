class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
         * 자기 자신을 제외한 모든 요소의 곱
         * = 왼쪽 요소들의 곱 * 오른쪽 요소들의 곱
         *
         * 왼쪽에서 오른쪽으로 순회하면서 누적 곱을 구하면
         * 각 요소 기준 왼쪽 요소들의 곱을 구할 수 있다.
         *
         * 반대로 오른쪽에서 왼쪽으로 순회하면서 누적 곱을 구하면
         * 각 요소 기준 오른쪽 요소들의 곱을 구할 수 있다.
         *
         * 왼쪽 요소들의 곱과 오른쪽 요소들의 곱을 곱하면 정답이 된다.
         *
         * 시간 복잡도: O(n)
         * 공간 복잡도: O(1)
         * 단, 반환 배열 result는 제외한다.
         */
        int n = nums.length;
        int[] result = new int[n];

        // 각 위치 기준 왼쪽 요소들의 곱을 result에 저장
        int prefixProduct = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefixProduct;
            prefixProduct *= nums[i];
        }

        // 각 위치 기준 오른쪽 요소들의 곱을 result에 반영
        int suffixProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }

        return result;
    }
}
