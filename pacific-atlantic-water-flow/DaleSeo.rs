use std::collections::VecDeque;

impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n_rows = heights.len();
        let n_cols = heights[0].len();

        let mut pacific = vec![vec![false; n_cols]; n_rows];
        let mut atlantic = vec![vec![false; n_cols]; n_rows];

        let mut pacific_queue = VecDeque::new();
        let mut atlantic_queue = VecDeque::new();

        for i in 0..n_rows {
            pacific[i][0] = true;
            pacific_queue.push_back((i, 0));
        }
        for j in 0..n_cols {
            pacific[0][j] = true;
            pacific_queue.push_back((0, j));
        }

        for i in 0..n_rows {
            atlantic[i][n_cols - 1] = true;
            atlantic_queue.push_back((i, n_cols - 1));
        }
        for j in 0..n_cols {
            atlantic[n_rows - 1][j] = true;
            atlantic_queue.push_back((n_rows - 1, j));
        }

        Self::bfs(&heights, &mut pacific, pacific_queue);
        Self::bfs(&heights, &mut atlantic, atlantic_queue);

        let mut result = vec![];

        for i in 0..n_rows {
            for j in 0..n_cols {
                if pacific[i][j] && atlantic[i][j] {
                    result.push(vec![i as i32, j as i32]);
                }
            }
        }

        result
    }

    fn bfs(
        heights: &Vec<Vec<i32>>,
        visited: &mut Vec<Vec<bool>>,
        mut queue: VecDeque<(usize, usize)>,
    ) {
        let directions = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];
        let m = heights.len();
        let n = heights[0].len();

        while let Some((i, j)) = queue.pop_front() {
            for (dx, dy) in &directions {
                let ni = i as i32 + dx;
                let nj = j as i32 + dy;

                if ni < 0 || nj < 0 || ni >= m as i32 || nj >= n as i32 {
                    continue;
                }

                let ni = ni as usize;
                let nj = nj as usize;

                if visited[ni][nj] {
                    continue;
                }

                if heights[ni][nj] >= heights[i][j] {
                    visited[ni][nj] = true;
                    queue.push_back((ni, nj));
                }
            }
        }
    }
}
