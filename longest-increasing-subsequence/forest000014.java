/*
Time Complexity: O(nlogn)
Space Complexity: O(nlogn)
*/
class Solution {

    int[] tree;
    int L = 1;

    public int lengthOfLIS(int[] nums) {
        init(nums);
        ArrayList<Tuple> tuples = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            tuples.add(new Tuple(i, nums[i]));
        }

        Collections.sort(tuples, (a, b) -> {
            if (a.val == b.val) {
                return b.ref - a.ref; // 2순위 : ref 내림차순
            } else {
                return a.val - b.val; // 1순위 : val 오름차순
            }
        });

        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            int curr = getMax(0, tuples.get(i).ref - 1) + 1;
            ans = Math.max(ans, curr);
            insert(tuples.get(i).ref, curr);
        }

        return ans;
    }

    public class Tuple {
        public int ref;
        public int val;

        public Tuple(int ref, int val) {
            this.ref = ref;
            this.val = val;
        }
    }

    public void init(int[] nums) {
        while (L < nums.length) {
            L *= 2;
        }

        tree = new int[L * 2];

        for (int i = 1; i < L * 2; i++) {
            tree[i] = 0;
        }
    }

    public void insert(int idx, int v) {
        int i = idx + L;
        tree[i] = v;
        i /= 2;
        while (i >= 1) {
            tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
            i /= 2;
        }
    }

    public int getMax(int l, int r) {
        int i = l + L;
        int j = r + L;
        int ret = 0;
        while (i <= j) {
            if (i % 2 == 1) {
                ret = Math.max(ret, tree[i++]);
            }
            if (j % 2 == 0) {
                ret = Math.max(ret, tree[j--]);
            }
            i /= 2;
            j /= 2;
        }

        return ret;
    }
}
