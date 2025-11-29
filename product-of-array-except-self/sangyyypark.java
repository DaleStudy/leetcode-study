/**
 1. 문제 이해
 answer[i] 에는 nums[i]를 제외한 나머지 수들을 모두 곱셈 했을때의 결과값이 들어가는 배열을 반환하는 문제

 2. naive algorithm도출

 가장 간단한 방법은 answer[i]에 값을 넣을때 nums배열을 탐색해서 nums[i]를 제외한 수를 곱셈해서 넣으면 끝이다.
 하지만, nums의 길이가 길면 시간복잡도가 O(N^2)이다.

 answer[i]에는 nums[i]의 왼쪼까지의 곱과 오른쪽 까지의 곱을 곱하면 끝이므로
 answer[i]에 nums[i]의 왼쪽까지 합을 넣어놓고 answer[i]에 nums[i]의 오른쪽가지의 곱을 곱한다.

 3. 시간복잡도 분석

 4. 코드구현
 */
class sangyyypark {
    public int[] productExceptSelf(int[] nums) {
        int [] answer = new int[nums.length];

        int left = 1;
        for(int i = 0; i < nums.length; i++) {
            answer[i] = left;
            left = nums[i] * left;
        }

        int right = 1;
        for(int i = nums.length - 1; i >= 0; i--) {
            answer[i] = answer[i] * right;
            right = nums[i] * right;
        }
        return answer;
    }

}

