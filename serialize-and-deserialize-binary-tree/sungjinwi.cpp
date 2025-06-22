/*
    풀이 :
        - serialize
            - BFS로 트리->val을 큐에 넣으면서 string (ex. [1,2,3,null,null,null,null])으로 합친다
            - 노드가 없을 때는 null을 string에 넣어서 어떤 부분이 비어있는지를 표시한다

        - deserialize
            - string을 split 시켜서 문자열 배열로 만들고 
            - 원래 트리와 순서를 맞추기위해 serialize와 마찬가지로 BFS를 통해 tree를 재구성
            - 문자열이 null이 아니면 해당 val을 가지는 노드를 만들어 연결

    노드 개수 : N

    serialize
    TC : O(N)
        전체 노드 순회
    SC : O(N)
        큐 크기는 노드 개수에 비례

    deserialize
    TC : O(N)
        노드 단위로 다시 쪼개서 전체 노드 순회
    SC : O(N)
        큐 및 split된 문자열 배열 크기는 노드 개수 비례
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <string>
#include <queue>
#include <iostream>
#include <sstream>
using namespace std;
class Codec {
    public:
    
        // Encodes a tree to a single string.
        string serialize(TreeNode* root) {
            queue<TreeNode*>    q;
            ostringstream out;
    
            out << "[";
            if (root)
                q.push(root);
            while (!q.empty()) {
                TreeNode*   node = q.front();
                if (node == nullptr) {
                    out << "null";
                }
                else {
                    out << node->val;
                    q.push(node->left);
                    q.push(node->right);
                }
                q.pop();
                out << ",";
            }
    
            string result = out.str();
            if (result.back() == ',')
                result.pop_back();
            result += "]";
    
            return result;
        }
    
        // Decodes your encoded data to tree.
        TreeNode* deserialize(string data) {
            if (data == "[]")
                return nullptr;
            string  s = data.substr(1, data.size() - 2);
            vector<string> tokens;
            string  token;
            stringstream ss(s);
    
            while (getline(ss, token, ','))
                tokens.push_back(token);
            
            TreeNode*   root = new TreeNode(stoi(tokens[0]));
            queue<TreeNode*>    q;
            q.push(root);
    
            int index = 1;
    
            while (!q.empty() && index < tokens.size()) {
                TreeNode* node = q.front();
                q.pop();
    
                if (tokens[index] != "null") {
                    node->left = new TreeNode(stoi(tokens[index]));
                    q.push(node->left);
                }
                index++;
    
                if (index < tokens.size() && tokens[index] != "null") {
                    node->right = new TreeNode(stoi(tokens[index]));
                    q.push(node->right);
                }
                index++;
            }
            return root;
        }
    };
    
    // Your Codec object will be instantiated and called as such:
    // Codec ser, deser;
    // TreeNode* ans = deser.deserialize(ser.serialize(root));
