/*
dp를 사용 dp를 사용하는 이유는 dfs를 할 경우 시간초과가 나므로
그리고 i번째의 최대값을 찾는 문제는 점화식으로 표현이 가능하므로 점화식으로 나타낼 수 있으면 dp도 활용이 가능하다.
앞으로 반복되는 문제가 있으면 dp를 적극 활용해보자.

각 dp 배열들의 1번째 집에 대해 초기화를 해주고 for 루프의 i=2부터 시작하는게 포인트였다.
nums[i]로 접근했을때 IndexOutOfRange에러가 발생하는게 아닌가 싶었지만 2부터 시작해서 최대값이 i는 배열-1 까지다.

dp1은 첫번째집을 방문했을때, dp2는 두번째집을 방문했을때이며 dp1은 마지막집을 방문하지 못한다.
이 조건을 i가 nums.length보다 작을 경우로 판단한다.

최종 최댓값은 각 dp 배열의 마지막 그리고 마지막에서 2번째에 저장되어있으므로 nums배열 크기 - 1, -2 한 값으로 조회한다.
*/


import java.util.*;

class Solution {
    public int rob(int[] nums) {
        int[] dp1 = new int[nums.length];
        int[] dp2 = new int[nums.length];

        if (nums.length == 1) {
            return nums[0];
        }

        dp1[0] = dp1[1] = nums[0];
        dp2[1] = nums[1];

        for (int i=2; i<nums.length; i++) {
            if (i < nums.length) {
                dp1[i] = Math.max((nums[i] + dp1[i-2]), dp1[i-1]);
            }
            dp2[i] = Math.max((nums[i] + dp2[i-2]), dp2[i-1]);
        }

        return Math.max(dp1[nums.length -2], dp2[nums.length -1]);
    }
}




// 아래는 dfs 로 푼 방식
// import java.util.*;

// class Solution {
//     public int rob(int[] nums) {
//         if (nums == null || nums.length == 0) {
//             return 0;
//         }

//         if (nums.length == 1) {
//             return nums[0];
//         }

//         return Math.max(
//             nums[0] + dfs(nums, 2, true), dfs(nums,1,false)
//         );
        
//     }

//     public int dfs(int[] nums, int idx, boolean first) {
//         // idx가 nums의 길이와 같거나 크다는 것은 범위를 초과했다는 의미이므로 0 return
//         if (idx >= nums.length) {
//             return 0;
//         }

//         // idx가 nums의 끝에 도달했을 경우 first의 여부에 따라 결과값이 바뀐다.
//         if (idx == nums.length - 1) {
//             // 첫번째를 방문시 마지막은 사용불가
//             if (first) {
//                 return 0;
//             } else {
//                 return nums[nums.length - 1];
//             }
//         }

//         // 현재 집을 털었을때 현재 idx의 값과 다음 집을 턴 최대값
//         int curRob = nums[idx] + dfs(nums, idx + 2, first);
//         // 현재 집을 건너뛸때 다음 idx의 값으로 다음 집을 턴 최대값
//         int nextRob = dfs(nums, idx + 1, first);

//         return Math.max(curRob, nextRob);
//     }
// }

