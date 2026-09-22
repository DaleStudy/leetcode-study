use std::collections::HashMap;

#[derive(Default)]
struct TrieNode {
    children: HashMap<u8, TrieNode>,
    is_word: bool,
}

struct WordDictionary {
    root: TrieNode,
}

impl WordDictionary {
    fn new() -> Self {
        Self {
            root: TrieNode::default(),
        }
    }

    // TC: O(n)
    // SC: O(n)
    fn add_word(&mut self, word: String) {
        let mut node = &mut self.root;
        for &byte in word.as_bytes() {
            node = node.children.entry(byte).or_default();
        }
        node.is_word = true;
    }

    // TC: O(n) without wildcards, O(26^n) in the worst case
    // SC: O(n)
    fn search(&self, word: String) -> bool {
        Self::search_from(&self.root, word.as_bytes())
    }

    fn search_from(node: &TrieNode, word: &[u8]) -> bool {
        match word.split_first() {
            None => node.is_word,
            Some((b'.', rest)) => node
                .children
                .values()
                .any(|child| Self::search_from(child, rest)),
            Some((byte, rest)) => node
                .children
                .get(byte)
                .is_some_and(|child| Self::search_from(child, rest)),
        }
    }
}
