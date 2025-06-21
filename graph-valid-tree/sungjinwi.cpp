/*
    풀이 :
        graph가 tree가 되려면 모든 노드가 연결되어 있어야하고 순환이 없어야한다
        간선이 노드 개수 n - 1보다 작으면 모든 노드 연결 불가능, 크면 무조건 순환이 생긴다
        간선이 n - 1과 동일할 때 순환이 없으면 valid tree라고 판단 가능

        Union-find 사용
        - 시작할 때 각 노드는 자기 자신을 parent(root)로 가진다
        - 노드가 서로 연결되있으면 한 union으로 합친 뒤 하나의 parent로 업데이트한다
            - 이를 통해 한 parent를 가지는 한 그룹으로 묶이게 된다

        find 함수는 한 그룹 전체의 parent를 재귀적으로 한 노드로 업데이트한다 (트리 깊이가 깊어져도 한번에 parent를 찾을 수 있게끔 경로최적화)

        두 노드의 find()결과 값이 같으면 이미 한 그룹에 속하는 것이므로 이 두 노드에 간선을 잇는 것은 순환이 생기는 것이다
        이를 통해 순환 있는지 판단

    노드 개수 : V, 간선 개수 : E
    E = V - 1일 때만 유의미한 연산하므로 E ≈ V

    TC : O(V)
        반복문 2회, find 함수의 재귀는 이론적으로 상수에 수렴한다고 한다

    SC : O(V)
        parent 배열
*/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    public:
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    vector<int> parent;
    bool validTree(int n, vector<vector<int>> &edges) {
        if (edges.size() != n - 1)
            return false;

        parent.resize(n);
        for (int i = 0; i < n; i++)
            parent[i] = i;
        
        for (auto& edge : edges) {
            int a = edge[0], b = edge[1];
            int rootA = find(a), rootB = find(b);
            if (rootA == rootB)
                return false;
            parent[rootA] = rootB;
        }
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
};
