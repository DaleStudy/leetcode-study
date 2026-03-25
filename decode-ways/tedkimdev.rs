// SC: O(t/m)   -> maximum recursion depth
// TC: O(2^(t/m))  
// t = target value
// m = smallest number in nums
// t/m = maximum number of elements in a combination
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        if s.starts_with('0') {
            return 0;
        }

        // dfs
        fn dfs(s: &str) -> i32 {
            if s.is_empty() {
                return 1;
            }

            let mut output = 0;
            if s[..1].parse::<i32>().unwrap() != 0 {
                output += dfs(&s[1..]);
            }
            if s.len() >= 2 && !s[..2].starts_with('0') {
                if s[..2].parse::<i32>().unwrap() > 26 {
                    return output;
                } else {
                    output += dfs(&s[2..]);
                }
            }            
            output
        }
        dfs(&s)
    }
    
}
