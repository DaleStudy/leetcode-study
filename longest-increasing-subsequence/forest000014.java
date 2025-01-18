/*
# Time Complexity: O(nlogn)
- tuples ArrayList 정렬: O(nlogn)
- 인덱스 트리 삽입: O(logn) * n times = O(nlogn)
- 인덱스 트리 조회: O(logn) * n times = O(nlogn)

# Space Complexity: O(nlogn)
- tuples ArrayList: O(n)
- 인덱스 트리: O(nlogn)

# solution
이 문제는 DP로 접근했습니다.

LIS(1, x)를 범위 [1, x] 내의 LIS(단, nums[x]를 반드시 포함)의 길이라고 정의하겠습니다. - (1)
1 <= j < i 인 모든 j에 한 LIS(1, j)를 알고 있다면, LIS(1, i)는 아래와 같이 구할 수 있습니다.
LIS(1, i) = max(LIS(1, j)) (단, j는 1 <= j < i 이고, nums[j] < nums[i]) - (2)

max(LIS(1, j))를 구할 때, 모든 j에 대해 탐색한다면, 전체 시간 복잡도는 O(n^2)가 되기 때문에, 시간 복잡도를 줄일 필요가 있습니다.
이 탐색 과정을 줄이기 위해, 아래의 사고 과정을 거쳤습니다.

어떤 범위 내의 가장 큰 값을 O(logn) 시간에 구하기 위한 자료구조로, 인덱스 트리(혹은 세그먼트 트리)를 사용합니다.
(이 인덱스 트리의 x번째 leaf 노드에는 LIS(1, x) 값을 저장하고, internal 노드에는 자식 노드들 중 가장 큰 값을 저장합니다.)

다만, 단순히 해당 범위 내의 가장 큰 값을 구하는 것만으로는 부족하고, nums[j] < nums[i]인 j만을 후보로 삼아야 할 텐데요,
그러기 위해서, 인덱스 트리에 모든 leaf 노드를 미리 삽입해두는 것이 아니라 아래처럼 순차적으로 max(LIS(1, i))의 계산과 삽입을 번갈아 수행합니다.
nums[i]의 크기가 작은 것부터 순서대로, "max(LIS(1, j))를 계산하고, leaf를 하나 삽입"하는 과정을 반복합니다.
nums[i]보다 더 큰 값은 아직 인덱스 트리에 삽입되지 않은 상태이기 때문에, 인덱스 트리에서 구간 [1, i-1]의 최대값을 조회하면 nums[j] < num[i]인 j에 대해서만 최대값을 찾게 되므로,
(2)번 과정을 O(logn) 시간에 구할 수 있습니다.
따라서 전체 시간 복잡도는 O(nlogn)이 됩니다.
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
