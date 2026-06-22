class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        int components = n;
        vector<int> p(n, -1);
        for (auto& e : edges)
        {
            if (uni(p, e[0], e[1])) // 이 엣지를 통해 합쳐지면
            {
               components--; // 컴포넌트 수는 하나 감소
            }
        }

        return components;
    }

    // union-find
    int find(vector<int>&p, int x)
    {
        if(p[x] < 0)
        {
            return x;
        }

        return p[x] = find(p, p[x]);
    }

    bool uni(vector<int>&p, int u, int v)
    {
        u = find(p, u);
        v = find(p, v);

        if (u == v)
        {
            return false;
        }

        if (p[v] < p[u])
        {
            swap(u, v);
        }

        if (p[u] == p[v])
        {
            p[u]--;
        }

        p[v] = u;
        return true;
    }
};
