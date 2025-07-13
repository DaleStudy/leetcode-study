import java.util.*;

public class Solution {

    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    // 라틴 알파벳을 쓰는 새로운 외계 문자가 있다. 하지만 문자의 순서는 알지 못한다.
    // 새로운 언어의 규칙에 맞는 사전식 순서(알파벳 순서)로 정의된 non-empty(비지 않은 상태인) 단어 목록을 받았다.
    // 이 언어의 순서를 찾으시오.
    public String alienOrder(String[] words) {

        // wrt wrf => wr은 공통 t가 f보다 먼저 나왔으므로 t < f
        // wrt er => w보다 e가 뒤에 나왔으므로 w < e
        // er ett => r이 t보다 뒤에 나왔으므로 r < t
        // ett rftt => r이 e보다 뒤에 나왔으므로 e < r

        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> char_order = new HashMap<>();

        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<>());
                char_order.putIfAbsent(c, 0);
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String cur_word = words[i];
            String next_word = words[i + 1];

            if (cur_word.length() > next_word.length() && cur_word.startsWith(next_word)) {
                return "";
            }

            // 비교: (wrt, wrf) => t와 f 비교
            // 비교: (wrf, er) => w와 e 비교
            for (int j = 0; j < Math.min(cur_word.length(), next_word.length()); j++) {
                char c1 = cur_word.charAt(j);
                char c2 = next_word.charAt(j);

                // from "wrt"and"wrf" ,we can get 't'<'f'
                // from "wrt"and"er" ,we can get 'w'<'e'
                // from "er"and"ett" ,we can get 'r'<'t'
                // from "ett"and"rftt" ,we can get 'e'<'r'
                // 순서 저장
                if (c1 != c2) {
                    if (!graph.get(c1).contains(c2)) {
                        graph.get(c1).add(c2);
                        char_order.put(c2, char_order.get(c2) + 1);
                    }
                    break;
                }
            }
        }

        Queue<Character> queue = new LinkedList<>();
        for (char c : char_order.keySet()) {
            // 최상위 부터 queue에 삽입 => w
            if (char_order.get(c) == 0) {
                queue.offer(c);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!queue.isEmpty()) {
            char cur = queue.poll();
            sb.append(cur);

            // 연관 글자들의 순서 조정 => w의 연관 글자들 => e, e와 연관 글자들 => t, t와 연관 글자들 => f ...
            for (char linked_char : graph.get(cur)) {
                char_order.put(linked_char, char_order.get(linked_char) - 1);
                if (char_order.get(linked_char) == 0) {
                    queue.offer(linked_char);
                }
            }
        }

        if (sb.length() != char_order.size()) {
            return "";
        }

        return sb.toString();

    }

}



