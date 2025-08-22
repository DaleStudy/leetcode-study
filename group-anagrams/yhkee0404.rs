use itertools::Itertools;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let sorted_strings: Vec<String> = strs
                .iter()
                .map(|s| {
                    s.chars()
                            .sorted()
                            .collect()
                }).collect();
        let inverted_sorted_strings: Vec<usize> = (0..sorted_strings.len())
                .sorted_by_key(|&i| &sorted_strings[i])
                .collect();
        let mut ans: Vec<Vec<String>> = vec![];
        let mut i = 0;
        let mut j;
        while i != sorted_strings.len() {
            let mut u: Vec<String> = vec![];
            j = i;
            while j == i || j != inverted_sorted_strings.len() && sorted_strings[inverted_sorted_strings[i]] == sorted_strings[inverted_sorted_strings[j]] {
                u.push(strs[inverted_sorted_strings[j]].clone());
                j += 1;
            }
            ans.push(u);
            i = j
        }
        ans
    }
}
