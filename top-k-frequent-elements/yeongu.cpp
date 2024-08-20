// TC: O(n logn)
// SC: O(n)

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> frequency;
    for (int n : nums) {
        frequency[n] += 1;
    }
    auto comparator = [&frequency](int n1, int n2) {
        return frequency[n1] > frequency[n2];
    };

    priority_queue<int, vector<int>, decltype(comparator)> min_heap(
        comparator);

    for (auto& entry : frequency) {
        min_heap.push(entry.first);
        if (min_heap.size() > k) {
            min_heap.pop();
        }
    }

    vector<int> output;

    for (int i = 0; i < k; i++) {
        output.push_back(min_heap.top());
        min_heap.pop();
    }
    return output;
}
