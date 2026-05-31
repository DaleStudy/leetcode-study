/*
1. 문제 이해

[-2,1,-3,4,-1,2,1,-5,4]
* 정답부분 참고
각 인덱스를 시작점으로 잡고 모든 부분에 대한 부분 배열의 합을 구한다
이전에 계산했던 내용을 저장해서 사용한다
-> 이렇게 계산해도 Time Limit Exceeded 발생하네 ..

결국엔 이렇게 해도 n^2 시간이 발생하므로 시간초과
포인트는 n^2 가 걸리는 시간을 어떻게 nlogn이나 n으로 줄일 수 있는지임

* 정답 부분 참고
누적합이 음수라면 시작 인덱스를 다음으로 과감하게 옮긴다


이 문제는 직관적으로 문제를 바라보는것이 중요했다.
아마도 이렇게 접근하는건 어떨까 ?
나는 최대합을 구하고싶었다. 부분 배열로!
부분배열이라는 것은 연속된다는 것이 특징이다.

즉, 연속되어야 하므로 이전의 합들이 만약 음수라면 ? 이 부분들은 필요가 없어지므로 과감히 버릴 수 있다는 것을 아는 것이 포인트였다.

버린다는 것의 의미는 ? -> 현재 인덱스의 값과 이전 전체의 값들의 합을 비교해서 현재 인덱스부터 다시 출발한다는 것이다. 그러므로 비교해서 더 큰값을 total로 가져가는 것이다.

만약 이걸 처음부터 알았다면 그리고 기존에 작성한 n^2 를 소요하면서 모든 합을 구하려 했을때 비효율적인것을 직감했다면 다른 방법으로 접근할 수 있었어야 했다.

그리고 처음 total, maxTotal을 첫번째 인덱스로 지정해줬기 때문에 i 인덱스는 1부터 시작해야한다


*/

import java.util.*;

class Solution {
    public int maxSubArray(int[] nums) {
        int total = nums[0];
        int maxTotal = nums[0];


        for (int i=1; i<nums.length; i++) {
            total = Math.max(nums[i], total + nums[i]);
            maxTotal = Math.max(total, maxTotal);
        }

        return maxTotal;

        // for (int i=0; i<nums.length; i++) {
        //     int total = 0;
        //     for (int j=i; j<nums.length; j++) {
        //         total += nums[j];
        //         max = Math.max(total, max);
        //         if (total < 0) {
        //             break;
        //         }
        //     }
        // }

        // return max;
    }

    private int sum(int[] arr, int start, int end) {
        int cnt = 0;
        for (int i=start; i<end + 1; i++) {
            cnt += arr[i];
        }
        return cnt;
    }
}
