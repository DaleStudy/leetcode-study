/*
    풀이 :
        maxHeap과 minHeap 사용

        heap에 담긴 총 수 : N

        addNum()
            작은 수 집합은 maxHeap, 큰 수 집합은 minHeap에 담는다
            minHeap과 maxHeap의 개수차이를 1로 유지하면서 addNum

            TC : O (log N)
                힙에 넣고 뺄 때 O (logN) 의 시간 소요

            SC : O (N)
                총 힙 크기는 N에 비례

        findMedian()
            더 크게 유지되는 것은 minHeap이므로 둘 의 개수가 같지 않을경우(총 홀수개) minHeap.top() 리턴
            같을 경우 총개수가 짝수개이므로 두 힙.top()의 평균을 리턴

            TC : O (1)
                각 힙에서 root값 확인은 O(1)의 시간 소요
            SC : O (1)
*/

#include <queue>
#include <vector>
using namespace std;

class MedianFinder {
    public:
        priority_queue<int> maxHeap;
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        MedianFinder() {
            
        }
        
        void addNum(int num) {
            if (minHeap.empty() || num >= minHeap.top())
                minHeap.push(num);
            else
                maxHeap.push(num);
            
            if (minHeap.size() > maxHeap.size() + 1) {
                maxHeap.push(minHeap.top());
                minHeap.pop();
            }
            else if (maxHeap.size() > minHeap.size()) {
                minHeap.push(maxHeap.top());
                maxHeap.pop();
            }
        }
        
        double findMedian() {
            if (maxHeap.size() == minHeap.size())
                return static_cast<double>(maxHeap.top() + minHeap.top()) / 2;
            else
                return minHeap.top();
        }
    };
    
    /**
     * Your MedianFinder object will be instantiated and called as such:
     * MedianFinder* obj = new MedianFinder();
     * obj->addNum(num);
     * double param_2 = obj->findMedian();
     */
