/* [5th/week02] 238. Product of Array Except Self

1. 문제 요약
링크: https://leetcode.com/problems/product-of-array-except-self/description/
각 인덱스 i에 대해, num[i]를 제외한 모든 값들을 곱해서 배열로 반환
(주의: 나누기 안됨, 시간 복잡도 O(n) 내로 동작해야 함)

2. 문제 풀이
풀이1: 인덱스 i를 기점으로, 이전 값들의 누적곱 배열 & 이후 값들의 누적곱 배열을 만들고 -> 각 인덱스 i에 대해, 두 배열 값 곱하기
성공: Time: 2 ms (87.36%), Space: 56.5 MB (10.9%)
=> 시간 복잡도: O(n), 공간 복잡도: O(n)

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] before = new int[n];
        int[] after = new int[n];
        int[] products = new int[n];
        
        before[0] = 1;
        for (int i = 0; i < n - 1; i++) {
            before[i + 1] = before[i] * nums[i];
        }
        
        after[n - 1] = 1;
        for (int i = n - 1; i > 0; i--) {
            after[i - 1] = after[i] * nums[i];
        }
        
        for (int i = 0; i < n; i++) {
            products[i] = before[i] * after[i];
        }
        
        return products;
    }
}

풀이2: 풀이1과 논리는 동일하지만, 누적곱을 배열을 사용해서 저장해두는 것이 아니라 변수 하나를 사용해서 저장하도록 변경
성공: Time: 3 ms (19.55%), Space: 55.4 MB (61.74%)
=> 시간 복잡도: 시간 복잡도: O(n), 공간 복잡도: 결과 배열 제외하면 O(1)

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] products = new int[n];
        Arrays.fill(products, 1);

        int leftProduct = 1;
        for (int i = 0; i < n - 1; i++) {
            leftProduct *= nums[i];
            products[i + 1] *= leftProduct;
        }

        int rightProduct = 1;
        for (int i = n - 1; i > 0; i--) {
            rightProduct *= nums[i];
            products[i - 1] *= rightProduct;
        }

        return products;
    }
}

3. TIL
동적 계획법(DP)이란?
큰 문제를 작은 부분 문제로 나누고, 그 부분 문제들의 해를 저장해 두었다가(메모이제이션/테이블), 필요할 때 재사용해서 전체 문제를 효율적으로 해결하는 기법이다.

*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] before = new int[n];
        int[] after = new int[n];
        int[] products = new int[n];
        
        before[0] = 1;
        for (int i = 0; i < n - 1; i++) {
            before[i + 1] = before[i] * nums[i];
        }
        
        after[n - 1] = 1;
        for (int i = n - 1; i > 0; i--) {
            after[i - 1] = after[i] * nums[i];
        }
        
        for (int i = 0; i < n; i++) {
            products[i] = before[i] * after[i];
        }
        
        return products;
    }
}
