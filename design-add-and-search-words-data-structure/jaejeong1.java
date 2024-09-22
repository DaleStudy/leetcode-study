import java.util.HashMap;
import java.util.Map;

class WordDictionary {
  // 시간복잡도: O(N), N(word의 길이)
  // 공간복잡도: O(N)
  Map<Character, WordDictionary> child;
  boolean isEnd;

  public WordDictionary() {
    child = new HashMap<>();
    isEnd = false;
  }

  public void addWord(String word) {
    var node = this;
    for (int i = 0; i < word.length(); i++) {
      char c = word.charAt(i);

      node.child.putIfAbsent(c, new WordDictionary());
      node = node.child.get(c);

      if (i == word.length() - 1) {
        node.isEnd = true;
        return;
      }
    }
  }

  public boolean search(String word) {
    return searchHelper(word, 0, this);
  }

  private boolean searchHelper(String word, int index, WordDictionary node) {
    if (index == word.length()) {
      return node.isEnd;
    }

    char c = word.charAt(index);
    // . 이 나오면 해당 노드의 자식 노드들에 대해 모두 재귀를 돌린다
    if (c == '.') {
      for (WordDictionary childNode : node.child.values()) {
        if (searchHelper(word, index + 1, childNode)) {
          return true;
        }
      }
      return false;
    } else {
      var childNode = node.child.get(c);
      if (childNode == null) {
        return false;
      }
      return searchHelper(word, index + 1, childNode);
    }
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
