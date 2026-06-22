class Solution {

  
   


    //O(n)에 증가 한 경우 profitMax를 갱신시키며 판단 -> time limit
    public int maxProfit(int[] prices) {
        int profitMax = 0;
        /*
        for(int i=0; i< prices.length - 1; i++){
            int buy= prices[i];
        

            for(int d =i+1; d < prices.length; d++){
                int sellCandid = prices[d];
                if (sellCandid - buy > profitMax){
                    profitMax = sellCandid - buy;
                }

            }
        }//end of for

        */

        int priceMin = Integer.MAX_VALUE;
        for(int i =0; i < prices.length; i++){
            if (prices[i] < priceMin){
                priceMin = prices[i];
            }
            else{
                profitMax = Math.max(profitMax, prices[i] - priceMin);
            }
        }

        return profitMax; 
        
    }
    
}

