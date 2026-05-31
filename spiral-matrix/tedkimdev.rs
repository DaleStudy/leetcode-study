// TC: O(m * n)
// SC: O(m * n)
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();

        let mut left = 0i32;
        let mut right = matrix[0].len() as i32;
        let mut top = 0i32;
        let mut bottom = matrix.len() as i32;

        while left < right && top < bottom {
            for i in left..right {
                result.push(matrix[top as usize][i as usize]);
            }
            top += 1;
            for i in top..bottom {
                result.push(matrix[i as usize][(right - 1) as usize]);
            }
            right -= 1;

            if !(left < right && top < bottom) {
                break;
            }

            for i in (left..right).rev() {
                result.push(matrix[(bottom - 1) as usize][i as usize]);
            }
            bottom -= 1;
            for i in (top..bottom).rev() {
                result.push(matrix[i as usize][left as usize]);
            }
            left += 1;
        }

        result
    }
}
