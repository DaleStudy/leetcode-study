import java.util.ArrayList;
import java.util.List;

public class Solution {
    /*
     * @param strs: a list of strings
     * @return: encodes a list of strings to a single string.
     */
    public String encode(List<String> strs) {
        List<String> temp = new ArrayList<>();

        if(strs.size() == 0) return null;

        for(String s : strs) {
            if(":".equals(s)) {
                temp.add("::");
            } else {
                temp.add(s);
            }            
        }

        return String.join(":;", temp);
    }

    /*
     * @param str: A string
     * @return: decodes a single string to a list of strings
     */
    public List<String> decode(String str) {
        List<String> temp = new ArrayList<>();

        if(str == null) return new ArrayList<>();

        // if(str.length() == 0) return new ArrayList<>();
        
        for(String s : str.split(":;")) {
            if("::".equals(s)) {
                temp.add(":");
            } else {
                temp.add(s);
            }            
        }
        return temp;
    }
}
