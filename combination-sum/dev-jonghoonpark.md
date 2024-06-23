- https://leetcode.com/problems/combination-sum/
- time complexity : O(2^n)
- space complexity : O(2^n)
- https://algorithm.jonghoonpark.com/2024/06/23/leetcode-39

## bfs 로 풀기

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();

        Queue<Holder> queue = new LinkedList<>();
        queue.offer(new Holder(target));

        while (!queue.isEmpty()) {
            Holder holder = queue.poll();
            int lastInput = !holder.combination.isEmpty() ? holder.combination.get(holder.combination.size() - 1) : 0;
            int left = holder.left;
            if (left == 0) {
                result.add(holder.combination);
                continue;
            }

            for (int candidate : candidates) {
                if (candidate < lastInput) {
                    continue;
                }

                if (left - candidate >= 0) {
                    queue.add(holder.next(candidate));
                } else {
                    break;
                }
            }
        }

        return result;
    }
}

class Holder {
    int left;
    List<Integer> combination;

    public Holder(int left) {
        this.left = left;
        this.combination = new ArrayList<>();
    }

    private Holder(int left, List<Integer> combination) {
        this.left = left;
        this.combination = combination;
    }

    public Holder next(int minus) {
        List<Integer> combinedList = new ArrayList<>(this.combination.size() + 1);
        combinedList.addAll(this.combination);
        combinedList.add(minus);
        return new Holder(this.left - minus, combinedList);
    }

    @Override
    public String toString() {
        return "{" +
                "left=" + left +
                ", combination=" + combination +
                '}';
    }
}
```

## backtracking 으로 풀기

```java
// TODO
```
