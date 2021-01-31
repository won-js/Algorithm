package leetcode;

public class MinSubArrayLen {
    public int minSubArrayLen(int s, int[] nums) {
        
        int ans = Integer.MAX_VALUE;
        int n=nums.length;
        int p=0;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=nums[i];
            while(sum>=s){
                ans=Math.min(ans,i-p+1);
                sum-=nums[p];
                p++;
            }
            
        }
        if(ans==Integer.MAX_VALUE)
            return 0;
        return ans;
        
    }
}
