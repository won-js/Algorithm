package leetcode;

import java.util.ArrayList;
import java.util.List;

public class Permutation {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        if(nums == null || nums.length == 0)
        	return result;
        
        dfs(nums, result, list);
        
        return result;
    }
    
    private void dfs(int [] nums ,List<List<Integer>> lists, List<Integer> cur) {
    	// 1 담는거
    	if(cur.size() == nums.length) {
    		List<Integer> list = new ArrayList<>(cur);
    		lists.add(list);
    	}
    	
    	// 2 for 저장, 탈출
    	for(int i =0; i < nums.length; i++) {
    		
//    		if(cur.size() == nums.length)
//    			continue;
    		if(cur.contains(nums[i]))
    			continue;
    		cur.add(nums[i]);
    		dfs(nums, lists, cur);
    		cur.remove(cur.size()-1);
    	}
    }
}
