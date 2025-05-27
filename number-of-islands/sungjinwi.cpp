/*
    풀이 :
        grid를 순회하면서 '1'을 만나면 상하좌우를 dfs를 통해 이미 탐색한 땅이라는 뜻으로 '$'로 변경하고
        새로운 땅을 만날때마다 cnt 증가

    grid 크기 M * N

    TC : O(M * N)
        dfs 호출은 grid의 크기에 비례

    SC : O(M * N)
        dfs 호출 스택도 grid의 크기에 비례례
*/

#include <vector>
using namesapce std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int cnt = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j, grid);
                    cnt++;
                }
            }
        }
        return (cnt);
    }

    void    dfs(int row, int col, vector<vector<char>>& grid) {
        if (row < 0 || row >= grid.size() || col < 0 || col >= grid[0].size() || grid[row][col] != '1')
            return ;
        grid[row][col] = '$';
        dfs(row + 1, col, grid);
        dfs(row - 1, col, grid);
        dfs(row, col + 1, grid);
        dfs(row, col - 1, grid);
    }
};
