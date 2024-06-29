- 문제: https://leetcode.com/problems/pacific-atlantic-water-flow/
- 풀이: https://algorithm.jonghoonpark.com/2024/03/03/leetcode-417

```java
public class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < heights.length; i++) {
            for (int j = 0; j < heights[0].length; j++) {
                System.out.printf("\n\ninit Flow : %d, %d\n", i, j);
                Flow flow = new Flow();
                dfs(flow, heights, Integer.MAX_VALUE, i, j);
                if (flow.flowToAtlanticOcean && flow.flowToPacificOcean) {
                    result.add(List.of(i, j));
                }
            }
        }

        return result;
    }

    private void dfs(Flow flow, int[][] heights, int prev, int i, int j) {
        if (i == -1 || j == -1) {
            flow.flowToPacificOcean = true;
            return;
        }

        if (i == heights.length || j == heights[0].length) {
            flow.flowToAtlanticOcean = true;
            return;
        }

        if (heights[i][j] == -1 || heights[i][j] > prev || flow.flowToAtlanticOcean && flow.flowToPacificOcean) {
            return;
        }

        int currentHeight = heights[i][j];
        heights[i][j] = -1;

        dfs(flow, heights, currentHeight, i + 1, j);
        dfs(flow, heights, currentHeight, i - 1, j);
        dfs(flow, heights, currentHeight, i, j + 1);
        dfs(flow, heights, currentHeight, i, j - 1);

        heights[i][j] = currentHeight;
    }
}

class Flow {
    boolean flowToPacificOcean;
    boolean flowToAtlanticOcean;
}
```

## TC, SC

heights의 길이를 `w`, heights[0]의 길이를 `h`로 정의했을 때,
이 코드의 시간 복잡도는 `O((w \* h)^2)`, 공간 복잡도는 `O(w \* h)` 이다.
시간 복잡도가 저렇게 나온 이유는 모든 좌표에 대해서 dfs를 진행하기 때문이다.
