/*
runtime 23 ms, beats 50.28%
memory 45.12 MB, beats 20.14%

time complexity: O(nlogn)
- numsArray 정렬: O(nlogn)
- binary search: O(nlogn)
  - i iteration: O(n)
  - i번째 binary search: O(logn)

space complexity: O(n)
- numsArray: O(n)
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        ArrayList<Tuple> numsArray = IntStream.range(0, nums.length)
                .mapToObj(i -> new Tuple(i, nums[i]))
                .collect(Collectors.toCollection(ArrayList::new));

        numsArray.sort(Comparator.comparing(tuple -> tuple.val));

        int n = numsArray.size();

        for (int i = 0; i < n; i++) {
            int x = target - numsArray.get(i).val;
            int j = -1;
            int l = i + 1;
            int r = n - 1;
            boolean found = false;
            while (l <= r) {
                int m = (r - l) / 2 + l;
                if (numsArray.get(m).val == x) {
                    j = m;
                    found = true;
                    break;
                } else if (numsArray.get(m).val < x) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            if (found) {
                int[] ans = new int[2];
                ans[0] = numsArray.get(i).ref;
                ans[1] = numsArray.get(j).ref;
                return ans;
            }
        }

        return null;
    }

    public class Tuple {
        public final Integer ref;
        public final Integer val;

        public Tuple(Integer ref, Integer val) {
            this.ref = ref;
            this.val = val;
        }
    }
}
