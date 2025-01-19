class Trie {

  class Node {
    boolean isEnd;
    Node[] childs = new Node[26];
    Node() {}
  }

  private Node root;

  public Trie() {
    this.root = new Node();
  }

  // O(m) when m is the length of word
  public void insert(String word) {
    Node curN = this.root;
    for(char c : word.toCharArray()) {
      if(curN.childs[c-'a'] == null) {
        curN.childs[c-'a'] = new Node();
      }
      curN = curN.childs[c-'a'];
    }
    //end
    curN.isEnd = true;
  }
  // O(k) when k is the length of searching word
  public boolean search(String word) {
    Node curN = this.root;
    for(char c : word.toCharArray()) {
      if(curN.childs[c-'a'] == null) return false;
      curN = curN.childs[c-'a'];
    }
    return curN.isEnd;
  }

  // O(k) when k is the length of prefix
  public boolean startsWith(String prefix) {
    Node curN = this.root;
    for(char c : prefix.toCharArray()) {
      if(curN.childs[c-'a'] == null) return false;
      curN = curN.childs[c-'a'];
    }
    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
