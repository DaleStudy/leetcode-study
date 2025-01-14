/**
 design ds that supports add, find
 find if string matches any previously added string.
 >> some kind of dictionary

 example
 add bad
 add dad
 add mad
 search pad >> false
 search bad >> true
 search .ad >> true . can be 'b' or 'd' or 'm'
 search b.. >> true .. can be "ad"

 constraints:
 1) empty string can be valid input?
 nope. lenght of string is in range of [1, 25]
 2) string only contiains alphanumeric? or alphabet
 only lowercase English letters
 3) how many queries can be given as input?
 at most 10^4

 solution 1) brute force
 save to data structure. for add
 check every character for all the saved words
 O(kn) when k is the number of saved words,
 n is the length of input word token
 25 * 25 * 10^4
 tc : O(kn) + O(kn)
 add : O(1)
 search : O(kn)
 sc : O(kn)

 solution 2) trie?

 save words to trie.
 when searching
 do bfs or backtracking dfs
 if current charcter is . add all childs
 else add matching childs
 overall tc : O(sum(m)) + O(n),
 add : O(m), when m is the length of saved word
 search : O(n), when n is the length of searh word
 sc : O(sum(m))

 if volume of search query is much bigger than add query
 trie solution would be better
 O(n) search time vs O(mn) search time
 */
class WordDictionary {
  class TrieNode {
    TrieNode[] childs;
    boolean isEnd;
    TrieNode() {
      childs = new TrieNode[26];
      isEnd = false;
    }
  }
  TrieNode root;
  public WordDictionary() {
    root = new TrieNode();
  }

  public void addWord(String word) {
    TrieNode curNode = root;
    for(char c : word.toCharArray()) {
      if(curNode.childs[c-'a'] == null) {
        curNode.childs[c-'a'] = new TrieNode();
      }
      curNode = curNode.childs[c-'a'];
    }
    curNode.isEnd = true;
  }

  public boolean search(String word) {
    return dfsHelper(root, word, 0);
  }

  public boolean dfsHelper(TrieNode node, String word, int p) {
    //end clause
    if(p == word.length()) {
      return node.isEnd;
    }

    char curC = word.charAt(p);
    if(curC == '.') {
      for(TrieNode next : node.childs) {
        if(next != null) {
          if(dfsHelper(next, word, p + 1)) return true;
        }
      }
      return false;
    } else {
      if(node.childs[curC-'a'] != null) {
        if(dfsHelper(node.childs[curC - 'a'], word, p + 1)) return true;
      }
      return false;
    }


  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
