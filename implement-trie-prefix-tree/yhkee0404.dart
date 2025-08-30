class Trie {

  final int n;
  final children = <int, Trie>{};
  bool ended = false;

  Trie([this.n = 0]);
  
  void insert(String word) {
    Trie u = this;
    for (int rune in word.runes) {
        u = u.children
                .putIfAbsent(rune, () => Trie(rune));
    }
    u.ended = true;
  }
  
  bool search(String word) => _search(word)?.ended ?? false;
  
  bool startsWith(String prefix) => _search(prefix) != null;

  Trie? _search(String word) {
    Trie? u = this;
    for (int rune in word.runes) {
        u = u!.children[rune];
        if (u == null) {
            return null;
        }
    }
    return u;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = Trie();
 * obj.insert(word);
 * bool param2 = obj.search(word);
 * bool param3 = obj.startsWith(prefix);
 */
