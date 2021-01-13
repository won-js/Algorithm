package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
    	List<List<Integer>> result = new ArrayList<>();
    	if(nums.length < 3) return result;
    	Arrays.sort(nums);
    	
    	for(int i=0; i<nums.length; i++) {
    		if(nums[i] >0) return result;
    		int left = i+1 ,right =  nums.length - 1;
    		if(i != 0 && nums[i] == nums[i-1]) continue;
    		
    		while(left < right) {
    			int sum = nums[left] + nums[right] + nums[i];
    			if(sum == 0) {
    				result.add(Arrays.asList(nums[i], nums[left], nums[right]));
    				left++;
    				while(left < right && nums[left] == nums[left-1]) left++;
    				right--;
    				while(left < right && nums[right] == nums[right+1]) right--;
    			}else if(sum < 0) {
    				left++;
    			}else {
    				right--;
    			}
    		}
    	}
    	return result;
    }
}
