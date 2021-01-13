package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupThePeople {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
    	List<List<Integer>> result = new ArrayList<>();
    	Map<Integer, List<Integer>> map = new HashMap<>();
    	
    	for(int i=0; i<groupSizes.length; i++) {
    		if(!map.containsKey(groupSizes[i])) {
    			List<Integer> temp = new ArrayList<>();
    			temp.add(i);
    			map.put(groupSizes[i], temp);
    		}else {
    			map.get(groupSizes[i]).add(i);
    		}
    		
    		if(map.get(groupSizes[i]).size() == groupSizes[i]) {
    			result.add(map.get(groupSizes[i]));
    			map.remove(groupSizes[i]);
    		}
    	}
    	return result;
    }
}