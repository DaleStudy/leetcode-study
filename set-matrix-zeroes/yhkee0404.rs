impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let m = matrix.len();
        let n = matrix.first().unwrap().len();
        let erased_row_0 = (0..n).any(|i| matrix[0][i] == 0);
        let erased_col_0 = (0..m).any(|i| matrix[i][0] == 0);
        for i in 1..m {
            for j in 1..n {
                if matrix[i][j] == 0 {
                    *matrix[i].first_mut().unwrap() = 0;
                    matrix.first_mut().unwrap()[j] = 0;
                }
            }
        }
        for i in 1..m {
            if *matrix[i].first().unwrap() != 0 {
                continue;
            }
            for j in 0..n {
                matrix[i][j] = 0;
            }
        }
        for j in 1..n {
            if matrix.first().unwrap()[j] != 0 {
                continue;
            }
            for i in 0..m {
                matrix[i][j] = 0;
            }
        }
        if erased_row_0 {
            for j in 0..n {
                matrix[0][j] = 0;
            }
        }
        if erased_col_0 {
            for i in 0..m {
                matrix[i][0] = 0;
            }
        }
    }
}
