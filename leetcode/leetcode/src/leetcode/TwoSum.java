package leetcode;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
	
	public static void main(String [] args) {
		TwoSum ts = new TwoSum();
		int[] nums = {2,7,11,15};
		
		for(int a : ts.twoSum(nums, 9)) {
			System.out.println(a);
		}
	}
	
	public int [] twoSum(int[] nums, int target) {
		int[] result = new int [2];
		Map<Integer, Integer> map = new HashMap<>();
		
		for(int i =0 ; i<nums.length; i++) {
			if(map.containsKey(nums[i])) {
				result[0] = map.get(nums[i]);
				result[1] = i;
				return result;
			}else {
				map.put(target - nums[i], i);
			}
		}
		return result;
	}
}
