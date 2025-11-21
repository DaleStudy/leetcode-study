import java.util.Set;
import java.util.stream.Collectors;

class Solution {
    public boolean isAnagram(String s, String t) {
        Set<Character> characterS = s.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet());
        Set<Character> characterT = t.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet());
        return characterS.equals(characterT);
    }
}
