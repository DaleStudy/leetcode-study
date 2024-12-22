// Space complexity: O(2n) - 주어진 한 단어안의 각 문자가 서로 다 다를 경우 생성한 맵들의 최대 길이는 주어진 단어만큼이므로 2n
// Time complexity: O(3n) - 각 맵을 생성하고 추가로 각 아이템을 비교하는 루프가 필요하므로 3n

use std::collections::HashMap;

pub fn is_anagram(s: String, t: String) -> bool {
    // Check if the lengh of the 2 words are same.
    // Otherwise return false.
    let len01 = s.len();
    let len02 = t.len();
    if len01 != len02 {
        return false;
    }

    // Prepare and fill a new map for s
    let mut s_map = HashMap::new();
    for s_char in s.chars() {
        let n = s_map.get(&s_char).copied().unwrap_or(0);
        s_map.insert(s_char, n + 1);
    }

    // Prepare and fill a new map for t
    let mut t_map = HashMap::new();
    for t_char in t.chars() {
        let n = t_map.get(&t_char).copied().unwrap_or(0);
        t_map.insert(t_char, n + 1);
    }

    // Iterate over the map s, so compare with the map t
    // to see if both have same number for the same character respectively
    for (s_char, num) in s_map.iter() {
        if t_map.get(s_char).copied().unwrap_or(0) != *num {
            return false;
        }
    }

    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_good() {
        let result = is_anagram("ana".to_owned(), "aan".to_owned());
        assert!(result);
    }

    #[test]
    fn test_bad() {
        let result = is_anagram("aaa".to_owned(), "aan".to_owned());
        assert!(!result);
    }
}

