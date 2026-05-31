/*

1. 문제 이해

모든 조합 (중복 허용) 을 통해 target 숫자를 찾는다.

2
2, 2
2, 2, 2
2, 2, 2, 2 - 초과
2, 2, 3 - 타겟
2, 2, 6 - 초과
2, 3
2, 3, 3
...
6, 
6, 6



2. 알고리즘

dfs ?

3. 예외 케이스
일치 케이스 없는 경우 ?
다 돌면 예외가 있을까 ?

4. 구현

종료 트리거는 일치할 경우
target 숫자보다 높은 경우는 뒤로 감
뒤로 가서 다음 숫자를 넣어 보자

candidates 정렬
dfs 로 진행, 입력 파라미터는 더할 숫자 ?
대소 비교해서 만약 더 작으면 같은 숫자 넣고 더 크면 뒤로 이동

dfs 함수

새로운 Num 입력받음
입력받은 숫자를 tmp 리스트에 더하고
전체 합이 target 에 대해 대소 관계 비교

1. 크다면 뒤로 이동하고 다음 숫자 입력
2. 같다면 result에 넣고 뒤로 이동
3. 작다면 동일한 숫자 넣기

이상하게 dfs 를 구현했다. 순서도 맞지 않고
for문 구현, 인자, 접근 방법 모두 틀렸다.
기억하자
1. 호출은 main 에서 dfs() 한다
2. 백트래킹 for 문은 dfs() 내에서 구현한다.

답변을 보고 오니 백트래킹을 어떻게 해야겠다는 감이 왔다.

뒤로 가는걸 어떻게 구현할까 생각했는데 For 문에서 tmp에 새로운 숫자를 넣고 제거하면서 그 사이에 dfs 를 넣으면 되는거였다.

즉
for loop
tmp.add num
dfs()
tmp.remove num

식으로 말이다.

*/

import java.util.*;

class Solution {
    private int t;
    private List<List<Integer>> result;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        t = target;
        result = new ArrayList<>();
        Arrays.sort(candidates);
        List<Integer> nums = new ArrayList<>();

        dfs(candidates, 0, nums, 0);

        return result;
    }

    public void dfs(int[] candidates, int total, List<Integer> nums, int start) {
        if (total > t) return; // total이 target 보다 크다면 이전으로 돌아가기 위해 return
        if (total == t) { // 정답일 경우 해당 값 추가 및 return
            result.add(new ArrayList<>(nums)); // nums 와 new ArrayList<>(nums) 차이 이해하기
            // 빈 배열로 저장되길래 왜 저때의 값이 저장안되지 ? 라고 생각했지만
            // 당연히 안됨. ref 주소값을 저장했으므로 나중에는 이 Nums가 모두 빈배열이 되므로
            return;
        }

        for (int i=start; i < candidates.length; i++) { // start 부터 시작하는것 포인트!
            int num = candidates[i];
            nums.add(num);
            dfs(candidates, total + num, nums, i);
            nums.remove(nums.size() - 1); // 다음에는 stack 사용하자
        }
    }
}
