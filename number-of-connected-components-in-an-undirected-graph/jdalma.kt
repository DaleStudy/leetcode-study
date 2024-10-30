import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class CountConnectedComponents {

    public int countComponents(int n, int[][] edges) {
        final int[] relation = new int[n];
        for (int i = 0; i < n ; i++) {
            relation[i] = i;
        }

        int result = n;
        for (int[] edge : edges) {
            if (union(relation, edge) == 1) {
                result--;
            }
        }

        return result;
    }

    private int union(int[] relation, int[] edge) {
        int parent1 = find(relation, edge[0]);
        int parent2 = find(relation, edge[1]);

        if (parent1 == parent2) {
            return 0;
        }

        if (parent1 < parent2) {
            relation[parent2] = parent1;
        } else {
            relation[parent1] = parent2;
        }
        return 1;
    }

    private int find(int[] relation, int node) {
        int result = node;
        while (relation[result] != result) {
            relation[result] = relation[relation[result]];
            result = relation[result];
        }
        return result;
    }

    @Test
    @DisplayName("입력받은 노드와 간선을 통해 그래프의 개수를 반환한다")
    void graphCount() {
        int actual = countComponents(3, new int[][]{ {0,1}, {0,2} });
        Assertions.assertThat(actual).isEqualTo(1);

        int actual1 = countComponents(6, new int[][]{ {0,1}, {1,2}, {2,3}, {4,5} });
        Assertions.assertThat(actual1).isEqualTo(2);

        int actual2 = countComponents(6, new int[][]{ {0,1}, {2,3}, {4,5}, {1,2}, {3,4} });
        Assertions.assertThat(actual2).isEqualTo(1);
    }
}
