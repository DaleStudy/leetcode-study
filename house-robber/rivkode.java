/*
1. 문제 이해
집털기 문제는 작은 문제가 큰 문제를 해결할 수 있는 지점이 있다. 피보나치를 생각해보자.

이 포인트는 문제를 다시 생각해보면

1번째를 턴다고 선택했을 경우 2번째 뒤인 3번째부터 마지막까지 털었을때의 최대값과 더하게 되면 그게 정답이 된다.
만약 2번째부터 턴다고 선택하면 4번째부터 마지막까지 털었을때의 최대값을 더하게 되면 그게 정답이 된다.
그래서 점화식을 아래와 같이 구할 수 있다.

result = MAX(nums[start], + dfs(start + 2), dfs(start + 1))

이 말의 의미는 start가 어디던 
그 지점의 값과 2번째 뒤부터 마지막까지 털었을때의 최대값
vs
그 지점의 1번째 뒤부터 마지막까지 털었을때의 최대값
중 더 큰 값이 정답이 된다는 의미이다.

그래서 이 점화식을 잘 세워야 하고 종료지점을 잘 설정해야한다.

종료시점은 여기서 더이상 털 집이 없을 경우이므로 nums의 길이를 초과한 인덱스가 들어왔을때가 종료지점이 된다.


2. 예외 상황
없음 -> 틀림 저렇게만 푸니 Time Limit Exceeded 발생
여기서 메모이제이션을 이용해야함
피보나치풀때도 메모이제이션을 이용해서 이전의 결과값을 저장하고 그걸 그대로 사용했었음
이 문제도 동일하게 이전 결과값을 그대로 사용하면 다시 똑같은 내용을 계산하지 않고 사용할 수 있음

모든 값이 0일 수 있음 그러면 memo에서 초기화 값인 0을 체킹해도 값 자체가 0이므로 계속 계산을 하게 됨

3. 알고리즘 선택
다이나믹 프로그래밍

4. 구현
*/

import java.util.*;

class Solution {
    static int[] memo;

    public int rob(int[] nums) {
        memo = new int[nums.length];

        // memo 체크시 집값이 0인 예외 케이스에 대비하여 -1로 세팅
        for (int i=0; i<nums.length; i++) {
            memo[i] = -1;
        }

        return dfs(0, nums, memo);
    }

    public int dfs(int start, int[] nums, int[] memo) {
        // start가 nums.length보다 크거나 같다는 것은 nums의 최대 크기를 넘었다는 의미로 종료
        if (start >= nums.length) {
            return 0;
        }
        
        // -1 값으로 memo 체크
        if (memo[start] != -1) {
            return memo[start];
        }

        // start 인덱스를 기준으로 start를 선택하는게 더 큰값인지 그 다음 인덱스를 선택하는게 큰 값인지를 비교
        // memo에 저장
        memo[start] = Math.max(nums[start] + dfs(start + 2, nums, memo), dfs(start + 1, nums, memo));

        return memo[start];
    }
}

