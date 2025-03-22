// 처음 봤을 때는 단순 노가다라 생각했는데, prefix 문제가 너무 까다로웠음
// 사이클 탐지도 마지막에 두면 더 편했는데 코드가 너무 길어지는거 같아서 GPT의 도움을 받았다.
// 다 정리하고 ㅂ니 코드 자체는 어렵지 않았음.
// 코치 여러분, 그리고 스터디 참여한 모두 수고하셨습니다.
public class AlienDictionary {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();

        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<>());
                inDegree.putIfAbsent(c, 0);
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String first = words[i];
            String second = words[i + 1];
            
            // invalid case: prefix 문제
            if (first.length() > second.length() && first.startsWith(second)) {
                return ""; 
            }

            for (int j = 0; j < Math.min(first.length(), second.length()); j++) {
                char c1 = first.charAt(j);
                char c2 = second.charAt(j);
                if (c1 != c2) {
                    if (!graph.get(c1).contains(c2)) {
                        graph.get(c1).add(c2);
                        inDegree.put(c2, inDegree.get(c2) + 1);
                    }
                    break;
                }
            }
        }

        PriorityQueue<Character> pq = new PriorityQueue<>();
        for (char c : inDegree.keySet()) {
            if (inDegree.get(c) == 0) {
                pq.offer(c);
            }
        }

        StringBuilder result = new StringBuilder();
        while (!pq.isEmpty()) {
            char current = pq.poll();
            result.append(current);
            for (char neighbor : graph.get(current)) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    pq.offer(neighbor);
                }
            }
        }

        // invalid case: 사이클 문제
        if (result.length() != inDegree.size()) {
            return "";
        }

        return result.toString();
    }
}
