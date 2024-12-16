/*
sol 1. 재귀 호출

알고리즘 문제를 오랜만에 풀어서... union-find를 떠올리긴 했으나, 구현 방법이 가물가물해서 원하는 솔루션으로 풀지 못한 것 같습니다.
일단 vis, cnt 와 재귀 호출을 사용해서 union-find와 유사하게 구현하긴 했는데요 (해설을 달면서 다시 보니 이것도 union-find를 구현하는 한 방법이라고 할 수 있을듯...?),
시간이 된다면 좀 더 최적화한 솔루션을 제출해보겠습니다.

Runtime: 98 ms(Beats: 35.68 %)
Time Complexity: O(n)
- set, vis, cnt 생성 : O(n)
- set의 모든 원소를 순회하면서 checkAbove 수행 : O(n)
    - checkAbove(x)는 x를 1번째 원소로 하는, 증가하는 연속 수열의 길이를 반환함
    - checkAbove(x)는 재귀적으로 checkAbove(x + 1)을 호출함.
    - checkAbove(x)는 이미 x를 방문한 적이 있거나, set 안에 x가 존재하지 않는 경우가 base case
    - 따라서 set의 모든 원소를 순회하는 iteration에서, n + a번 호출되므로, 시간 복잡도는 O(n)
        - (a는 consecutive chunk의 개수이고 n보다 작거나 같음)


Memory: 118.04 MB(Beats: 5.60 %)
Space Complexity: O(n)
- set, vis, cnt : O(n)
 */

class Solution {
    Set<Integer> set = new HashSet<>();
    Map<Integer, Boolean> vis = new HashMap<>();
    Map<Integer, Integer> cnt = new HashMap<>(); // key를 1번째 원소로 하는 연속한 증가 수열의 크기

    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        for (int num : nums) {
            if (set.contains(num)) {
                continue;
            }

            set.add(num);
            vis.put(num, false);
            cnt.put(num, 1);
        }

        int max = 0;
        for (int num : set) {
            int cnt = checkAbove(num);
            if (max < cnt) {
                max = cnt;
            }
        }

        return max;
    }

    public Integer checkAbove(Integer num) {
        if (null == vis.get(num)) {
            return 0;
        } else if (vis.get(num)) {
            return cnt.get(num);
        }

        vis.put(num, true);
        int cntAbove = checkAbove(num + 1);
        if (cntAbove > 0) {
            cnt.put(num, cntAbove + 1);
        }

        return cntAbove + 1;
    }
}
