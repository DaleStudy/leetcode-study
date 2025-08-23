class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for(String word : strs){
            int[] characters = new int[26];
            for(char c : word.toCharArray()){
                characters[c - 'a']++;
            }

            String countCode = Arrays.toString(characters);
            if(!groups.containsKey(countCode)){
                groups.put(countCode, new ArrayList<String>());
            }
            List<String> temp = groups.get(countCode);
            temp.add(word);
        }

        List<List<String>> answer = new ArrayList<>();
        for(List<String> g : groups.values()){
            answer.add(g);
        }

        return answer;
    }
}


