/*
    풀이 :
        BFS를 이용한 진입차수 기반 위상정렬
        
        prerequisite에서 course로 방향 간선이 생기는 그래프 문제
        그래프는 이중벡터로 만들고 선수과목 관계에 따라 초기화 (graph[선수과목]에 상위과목들을 담는다)
        과목을 들으려면 필요한 선수과목 수 -> inDgree에 배열로 저장

        선수과목이 필요없는 (inDgree에서 성분이 0인) 과목 먼저 큐에 넣는다
        과목을 수강하면 finished++로 수강완료 표시, 해당 과목을 선수과목으로 가지는 과목들에서 진입차수를 1씩 뺸다
        진입차수가 0이 되는 과목을 큐에 넣어서 반복

        큐가 완전히 빌 떄까지 반복했을 떄 모든 과목을 이수 가능하면(finished == numCourses) true 아니면 false

    수강과목 수 : V(Vertex), 선수과목 관계 수 : E(Edge)

    TC : O (V + E)
        prerequisites(E)과 numCourses(V)만큼에 대해 각각 반복문

    SC : O (V + E)
        기본적으로 V만큼의 빈 벡터를 가지고 있고 추가적으로 E만큼 성분이 push된다
*/

#include <vector>
#include <queue>

using namespace std;

class Solution {
    public:
        bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
            vector<vector<int>> graph(numCourses);
            vector<int>         inDgree(numCourses, 0);
    
            for (auto& prerequisite : prerequisites) {
                int crs = prerequisite[0];
                int pre = prerequisite[1];
                graph[pre].push_back(crs);
                inDgree[crs]++;
            }
    
            queue<int>  q;
            int finished = 0;
    
            for (int i = 0; i < numCourses; i++) {
                if (inDgree[i] == 0)
                    q.push(i);
            }
    
            while (!q.empty()) {
                int cur = q.front();
                q.pop();
    
                for (auto& next : graph[cur]) {
                    if (--inDgree[next] == 0)
                        q.push(next);
                }
                finished++;
            }
            
            return finished == numCourses;
        }
    };
