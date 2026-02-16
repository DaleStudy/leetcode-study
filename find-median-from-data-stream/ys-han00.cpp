class MedianFinder {
public:
    priority_queue<int> lower;
    priority_queue<int, vector<int>, greater<int>> upper;
    
    MedianFinder() {    
    }
    
    void addNum(int num) {
        if(upper.empty() || upper.top() < num)
            upper.push(num);
        else
            lower.push(num);

        if(lower.size() > upper.size()) {
            upper.push(lower.top());
            lower.pop();
        }
        else if(lower.size() + 1 < upper.size()) {
            lower.push(upper.top());
            upper.pop();
        }
    }
    
    double findMedian() {
        if(lower.size() < upper.size())
            return upper.top();
        else
            return (lower.top() + upper.top()) / 2.;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

