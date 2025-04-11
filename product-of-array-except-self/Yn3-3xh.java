/*
[문제풀이]
- 본인 index를 제외한 모든 index의 수를 곱하자.
- O(N)으로 풀자.
- 나눗셈은 사용하지 말자.

index  0 1 2 3
num    1 2 3 4
prefix 1 1 2 6

index  0  1  2 3
num    1  2  3 4
suffix 24 12 4 1

answer = prefix * suffix
24 12 8 6

- 풀이 1
time: O(N), space: O(N)
    class Solution {
        public int[] productExceptSelf(int[] nums) {
            int len = nums.length;
            int[] answer = new int[len];
            int[] prefix = new int[len];
            int[] suffix = new int[len];

            prefix[0] = 1;
            suffix[len - 1] = 1;
            for (int i = 1; i < len; i++) {
                prefix[i] = prefix[i - 1] * nums[i - 1];
            }
            for (int i = len - 2; i >= 0; i--) {
                suffix[i] = suffix[i + 1] * nums[i + 1];
            }

            for (int i = 0; i < len; i++) {
                answer[i] = prefix[i] * suffix[i];
            }
            return answer;
        }
    }

- 풀이 2
time: O(N), space: O(1)


[회고]
본인 index가 아닌 "앞의 수들의 곱"과 "뒤의 수들의 곱" 을 어떻게 구할 수 있을까?
의 고민에서 방법을 찾지 못했다.

풀이방법을 보고 변수와 반복문을 더 쓰기 싫어하는 부분에서 아이디어가 닫힌 것 같다..
우선 많이 써보고 줄이는 방법으로 풀어보자.
*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;

        int[] answer = new int[len];
        answer[0] = 1;
        for (int i = 1; i < len; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        int suffixMul = 1;
        for (int i = len - 2; i >= 0; i--) {
            suffixMul *= nums[i + 1];
            answer[i] *= suffixMul;
        }
        return answer;
    }
}
