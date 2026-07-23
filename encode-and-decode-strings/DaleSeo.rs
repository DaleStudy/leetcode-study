// TC: O(n)
// SC: O(n)
impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        strs.iter()
            .map(|s| format!("{}#{}", s.len(), s))
            .collect()
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut strs = Vec::new();
        let bytes = s.as_bytes();
        let mut i = 0;
        while i < bytes.len() {
            let sep = s[i..].find('#').unwrap() + i;
            let len: usize = s[i..sep].parse().unwrap();
            strs.push(s[sep + 1..sep + 1 + len].to_string());
            i = sep + 1 + len;
        }
        strs
    }
}
