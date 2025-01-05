class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /**
        1. understanding
        - grouping the anagrams together, and return groups
        2. strategy
        - anagram group's identity: same characters with same counts
        - so, transform each strs to character and count hashtable, called 'id'.
        - if groups contains strs's 'id', then append
        - return values list
        3. complexity
        - time: O(N * L) where, N is the length of array strs, and L is the max length of each str
        - space: O(N * L)
        */
        Map<Map<Character, Integer>, List<String>> groups = new HashMap<>();
        for (String word: strs) {
            Map<Character, Integer> id = idOf(word);
            List<String> group = groups.getOrDefault(id, new ArrayList<>());
            group.add(word);
            groups.put(id, group);
        }

        // System.out.println(groups);
        List<List<String>> ret = new ArrayList<>();
        ret.addAll(groups.values());
        return ret;
    }

    private Map<Character, Integer> idOf(String word) {
        Map<Character, Integer> id = new HashMap<>();
        for (char c: word.toCharArray()) {
            id.put(c, id.getOrDefault(c, 0) + 1);
        }
        return id;
    }
}

