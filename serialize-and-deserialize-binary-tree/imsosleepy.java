// 문제 해석 부터 안되서 GPT에게 도움을 요청
// Serialize (직렬화): 트리를 문자열로 변환하는 과정.
// Deserialize (역직렬화): 문자열을 다시 트리로 변환하는 과정.
// 트리를 저장하고 복원할 수 있는 형식이라면 어떤 방법이든 가능.
// 🔹 해결 방법
// 우리는 BFS(너비 우선 탐색)와 큐(Queue)를 활용한 방식을 사용할 거야.
// 이 방식을 선택한 이유는:

// 트리의 구조를 유지하면서도 직렬화하기 쉽다.
// 문자열이 순차적으로 만들어져 역직렬화할 때도 다시 순차적으로 트리를 복원하기 편하다.
public class Codec {
    
    // 직렬화 (Serialize)
    public String serialize(TreeNode root) {
        if (root == null) return "null";  // 빈 트리 처리
        
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            
            if (node == null) {
                sb.append("null,");
            } else {
                sb.append(node.val).append(",");
                queue.offer(node.left);
                queue.offer(node.right);
            }
        }
        return sb.toString();
    }

    // 역직렬화 (Deserialize)
    public TreeNode deserialize(String data) {
        if (data.equals("null")) return null; // 빈 트리 처리

        String[] values = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        int i = 1;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            
            if (!values[i].equals("null")) {
                node.left = new TreeNode(Integer.parseInt(values[i]));
                queue.offer(node.left);
            }
            i++;

            if (!values[i].equals("null")) {
                node.right = new TreeNode(Integer.parseInt(values[i]));
                queue.offer(node.right);
            }
            i++;
        }
        return root;
    }
}

// 트리는 대부분 DFS로 해결했어서 비슷한 방식을 생각했으나 구현 실패
// GPT에게 이어서 작업을 했고 O(N)의 시간복잡도를 얻음. 그러나 위의 BFS보다 속도가 느림
class Codec {
    // 🔹 DFS 기반 직렬화 (Serialize)
    public String serialize(TreeNode root) {
        if (root == null) return "null";
        return root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }

    // 🔹 DFS 기반 역직렬화 (Deserialize)
    public TreeNode deserialize(String data) {
        Queue<String> nodes = new LinkedList<>(Arrays.asList(data.split(",")));
        return buildTree(nodes);
    }

    private TreeNode buildTree(Queue<String> nodes) {
        String val = nodes.poll();
        if (val.equals("null")) return null;

        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = buildTree(nodes);
        node.right = buildTree(nodes);
        return node;
    }
}
