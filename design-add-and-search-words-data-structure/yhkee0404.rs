use std::collections::HashMap;

struct WordDictionary {
    trie: Box<Trie>,
}

struct Trie {
    ended: bool,
    children: HashMap<char, Box<Trie>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {

    fn new() -> Self {
        WordDictionary {
            trie: Box::new(Trie::new()),
        }
    }
    
    // T(n) = S(n) = O(26n) = O(n)
    fn add_word(&mut self, word: String) {
        let mut t = &mut self.trie;
        for c in word.chars() {
            t = t.children
                    .entry(c)
                    .or_insert(Box::new(Trie::new()))
        }
        t.ended = true
    }
    
    fn search(&self, word: String) -> bool {
        return Self::search_from_index(&self.trie, &word)
    }

    // T(n) = S(n) = ((26^2)n) = O(n)
    fn search_from_index(trie: &Trie, word: &str) -> bool {
        return match word.chars()
                .next() {
                    None => trie.ended,
                    Some(c) => if c == '.' {
                                trie.children
                                .values()
                                .any(|x| Self::search_from_index(&x, &word[1..])) // Slice O(1)
                            } else {
                                match trie.children
                                        .get(&c) {
                                            None => false,
                                            Some(x) => Self::search_from_index(&x, &word[1..]), // Slice O(1)
                                        }
                            },
                }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */

impl Trie {
    fn new() -> Self {
        Trie {
            ended: false,
            children: HashMap::new(),
        }
    }
}
