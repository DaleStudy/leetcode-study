- 문제
  - 유료: https://leetcode.com/problems/graph-valid-tree/
  - 무료: https://www.lintcode.com/problem/178/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/02/leetcode-261

## 내가 작성한 풀이

```java
public class Solution {
    public boolean validTree(int n, int[][] edges) {
        int[] degrees = new int[n];

        for (int[] edge : edges) {
            int largeOne = Math.max(edge[0], edge[1]);
            if (degrees[largeOne] == 0) {
                degrees[largeOne] += 1;
            } else {
                return false;
            }
        }

        int zeroCount = 0;
        for (int degree : degrees) {
            if (degree == 0) {
                zeroCount++;
            }

            if (zeroCount > 1) {
                return false;
            }
        }

        return zeroCount == 1;
    }
}
```

다음과 같이 가정을 하고 풀었다.

- 루트를 제외한 모든 노드는 1개의 부모를 가진다.
- 루트는 부모를 가지지 않는다.

따라서 각 노드로 들어오는 수를 세어봤을 때 루트에는 들어오는 간선이 없어야 하며, 나머지 노드는 1개의 간선이 있어야 한다.

### TC, SC

시간 복잡도는 O(n)이다. 공간 복잡도는 O(n)이다. 시간 복잡도를 조금 더 디테일 하게 보자면 간선 의 수도 포함을 시킬 수 있을 것이다.
