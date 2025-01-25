class Solution {

	int[][] moves = {{1,0}, {-1,0}, {0,1}, {0,-1}};
	boolean[][] visited;
	public int numIslands(char[][] grid) {
		// 섬의 갯수 => 0혹은 경계선으로 둘러싸인 것의 갯수
		// dfs로 탐색
		int result = 0;
		visited = new boolean[grid.length][grid[0].length];

		for (int i=0; i<grid.length; i++) {
			for (int j=0; j<grid[0].length; j++) {
				if (grid[i][j] == '1' && !visited[i][j]) {
					dfs(i, j, grid);
					result++;
				}
			}
		}

		return result;
	}

	public void dfs(int y, int x, char[][] grid) {
		visited[y][x] = true;

		for (int[] move: moves) {
			int newX = x + move[0];
			int newY = y + move[1];

			if (newX<0 || newX >= grid[0].length || newY<0 || newY >= grid.length || visited[newY][newX] || grid[newY][newX]=='0') continue;
			dfs(newY, newX, grid);
		}
	}
}


