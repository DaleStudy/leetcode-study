// TC: O(m * n)
// SC: O(m * n)
impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let mut cnt = 0;
        for r in 0..grid.len() {
            for c in 0..grid[r].len() {
                if grid[r][c] == '1' {
                    cnt += 1;
                    Self::sink(&mut grid, r, c);
                }
            }
        }
        cnt
    }

    fn sink(grid: &mut Vec<Vec<char>>, row: usize, col: usize) {
        grid[row][col] = '0';
        let mut stack = vec![(row, col)];
        while let Some((row, col)) = stack.pop() {
            for (r, c) in [
                (row, col.wrapping_sub(1)),
                (row, col + 1),
                (row.wrapping_sub(1), col),
                (row + 1, col),
            ] {
                if r < grid.len() && c < grid[r].len() && grid[r][c] == '1' {
                    grid[r][c] = '0';
                    stack.push((r, c));
                }
            }
        }
    }
}
