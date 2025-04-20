import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

// 시간복잡도: O(n ^ target)
class Solution {

    public List<Integer> tArr = new ArrayList<>();
    public Set<List<Integer>> s = new HashSet<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if(target == 1) {
            return new ArrayList<>();
        }

        Arrays.sort(candidates);
        dfs(candidates, target, 0);

        return new ArrayList<>(s);
    }

    public void dfs(int[] candi, int target, int now) {

        if(target < now) {
            return;
        }

        // 정답 배열에 추가.
        if(target == now) {
            List<Integer> temp = new ArrayList<>(tArr);
            Collections.sort(temp);
            s.add(temp);
            return;
        }

        for(int i = 0; i < candi.length; i++) {
            tArr.add(candi[i]);
            dfs(candi, target, (now + candi[i]));
            tArr.remove(tArr.size() - 1); // 가장 마지막 배열의 원소를 제거.
        }
    }
}


// NOTE: 세 수 이상의 조합의 합을 구하지 못하는 알고리즘.
class WrongSolution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
         List<List<Integer>> res = new ArrayList<>();
         List<List<Integer>> result = new ArrayList<>();

        if(target == 1) {
            return new ArrayList<>();
        }

        Arrays.sort(candidates);

        // i번째 값의 메모 구하기
        for(int i = 0; i < candidates.length; i++) {
            
            // 0 ~ i - 1까지만 의 값으로 i번째 값끼리 답이 나는지 확인.
            for(int j = 0; j < i; j++) {
                int current = candidates[i];
                int before = candidates[j];

                int start = 1;
                while(true) {

                    int startValue = current * start;
                    if(startValue >= target) {
                        break;
                    }

                    List<Integer> ans = new ArrayList<>();

                    int diff = target - startValue;

                    if(diff % before == 0) {

                        for(int k = 0; k < start; k++) {
                            ans.add(current);
                        }

                        int temp = diff / before;
                        for(int k = temp; k > 0; k--) {
                            ans.add(before);
                        }

                        res.add(ans);
                    }

                    start++;
                }
            }

            // i로만 답을 구하는 경우.
           int copy = target;
            List<Integer> ans = new ArrayList<>();
            if(target % candidates[i] == 0) {
                int mok = copy /= candidates[i];
                while(mok > 0) {
                    ans.add(candidates[i]);
                    mok--;
                }
                res.add(ans);
            }
        }

        
         for (int i = res.size() - 1; i >= 0; i--) {
            List<Integer> inner = new ArrayList<>(res.get(i));
            result.add(inner);
        }

        return result;
    }
}
