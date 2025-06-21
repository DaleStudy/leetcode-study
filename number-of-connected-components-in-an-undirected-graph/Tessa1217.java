import java.util.*;

public class Solution {

    // Union Find
    public int countComponents(int n, int[][] edges) {

        List<Integer> parent = clearGraph(n);

        for (int[] edge : edges) {
            union(parent, edge[0], edge[1]);
        }

        Set<Integer> componentRoots = new HashSet<>();
        for (int i = 0; i < n; i++) {
            componentRoots.add(find(parent, i));
        }

        return componentRoots.size();
    }

    private void union(List<Integer> parent, int x, int y) {
        int px = find(parent, x);
        int py = find(parent, y);
        if (px > py) {
            parent.set(py, px);
        } else {
            parent.set(px, py);
        }
    }

    private int find(List<Integer> parent, int x) {
        if (parent.get(x) == x) {
            return x;
        }
        parent.set(x, find(parent, parent.get(x)));
        return parent.get(x);
    }

    private List<Integer> clearGraph(int n) {
        List<Integer> parent = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            parent.add(i);
        }
        return parent;
    }
}


