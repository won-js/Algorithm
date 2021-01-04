package leetcode;

public class MaximumSubarray {
	public static void main(String [] args) {
		MaximumSubarray ms = new MaximumSubarray();
		int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
		
		System.out.println(ms.maxSubArray(nums));
	}
	
    public int maxSubArray(int[] nums) {
    	int newSum = nums[0];
    	int max = nums[0];
    	
        for(int i=1; i<nums.length; i++) {
        	newSum = Math.max(nums[i], newSum+nums[i]);
        	max = Math.max(newSum,max);
        }
        	
        return max;
    }
}
