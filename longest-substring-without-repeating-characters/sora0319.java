class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> characters = new HashMap<>();
        int maxLength = 0;
        int length = 0;
        int start = 0;

        for(int i = 0; i < s.length(); i++){
            if(!characters.containsKey(s.charAt(i))){
                characters.put(s.charAt(i), i);
                length++;
            }
            else{
                maxLength = Math.max(length, maxLength);

                int place = characters.get(s.charAt(i));
                if(place < start){
                    characters.put(s.charAt(i), i);
                    length++;
                    continue;
                }

                length = i - place;
                start = place + 1;
                characters.put(s.charAt(i), i);
            }
        }
        maxLength = Math.max(length, maxLength);

        return maxLength;
    }
}

