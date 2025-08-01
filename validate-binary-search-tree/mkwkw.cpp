//Optimize complexity
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> answer(nums.size(), 1);
        //production before nums[i] from index 0
        int before = 1;

        for(int i=0; i<nums.size()-1; i++)
        {
            before *= nums[i];
            answer[i+1] *= before;
        }

        //nums[i] 기준 앞에서 production 해놓은 것에 nums[i] 기준 뒤에 것들을 production from index n-1
        //production after nums[i] to answer[i-1]
        // answer[i-1] * after
        int after = 1;
        for(int i=nums.size()-1; i>0; i--)
        {
            after *= nums[i];
            answer[i-1] *= after;
        }

        return answer;
    }
};



//using division operation
/*
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zeroCnt = 0;
        int allProduct = 1;
        vector<int> answer(nums.size());

        for(int i=0; i<nums.size(); i++)
        {
            allProduct *= nums[i];
            if(nums[i]==0)
            {
                zeroCnt++;
            }
        }

        if(zeroCnt == 0)
        {
            for(int i=0; i<nums.size(); i++)
            {
                answer[i] = allProduct/nums[i];
            }
        }
        else if(zeroCnt == 1)
        {
            int zeroIdx = 0;
            int allProductWithoutZero = 1;

            for(int i=0; i<nums.size(); i++)
            {
                if(nums[i]==0)
                {
                    zeroIdx = i;
                }
                else
                {
                    allProductWithoutZero *=nums[i];
                    answer[i] = 0;
                 }
            }

            answer[zeroIdx] = allProductWithoutZero;
        }
        
        return answer;
    }
};
*/
