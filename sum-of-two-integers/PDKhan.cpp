class Solution {
    public:
        int getSum(int a, int b) {
            unsigned int result = 0;
            int carry = 0;
    
            for(int i = 0; i < 32; i++){
                unsigned int aa = a & (1U << i);
                unsigned int bb = b & (1U << i);
    
                if(aa && bb){
                    if(carry)
                        result |= (1U << i);
                    
                    carry = 1;
                }else if(aa == 0 && bb == 0){
                    if(carry)
                        result |= (1U << i);
                    
                    carry = 0;
                }else{
                    if(carry == 0)
                        result |= (1U << i);
                }
            }
    
            return result;
        }
    };
