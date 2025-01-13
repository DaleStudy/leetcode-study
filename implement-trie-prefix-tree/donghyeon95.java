import java.util.HashMap;

class Trie {
	HashMap<String, Boolean> trie;
	public Trie() {
		trie = new HashMap<>();
	}

	public void insert(String word) {
		StringBuilder sb = new StringBuilder();
		for (char c: word.toCharArray()) {
			sb.append(c);
			trie.putIfAbsent(sb.toString(), false);
		}
		trie.put(sb.toString(), true);
	}

	public boolean search(String word) {
		return trie.getOrDefault(word, false);
	}

	public boolean startsWith(String prefix) {
		return trie.containsKey(prefix);
	}
}




