//Store the number and the index.
//There can be only 2 same numbers. <- there is exactly one solution

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, vector<int>> numAndIndex;
        vector<int> answer;

        //map: key:nums[i], value:{indexs}
        for(int i=0; i<nums.size(); i++)
        {
            numAndIndex[nums[i]].push_back(i);
        }

        for(int i=0; i<nums.size()-1; i++)
        {
            if(numAndIndex.contains(target-nums[i]))
            {
                //To pick another number, not own number
                if(target-nums[i]==nums[i]&&numAndIndex[nums[i]].size()==2)
                {
                    answer.push_back(numAndIndex[nums[i]][0]);
                    answer.push_back(numAndIndex[nums[i]][1]);
                }
                else if(target-nums[i]!=nums[i])
                {
                    answer.push_back(numAndIndex[nums[i]][0]);
                    answer.push_back(numAndIndex[target-nums[i]][0]);
                }
            }

            if(answer.size()==2)
            {
                break;
            }
        }
        
        return answer;

    }
};
