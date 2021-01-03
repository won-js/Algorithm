package leetcode;

import java.util.HashMap;
import java.util.Map;

public class Solution {
	public int solution(int[] A) {
		Map<Integer, Integer> map = new HashMap<>();
		int result = 0;
		
		for(int a : A) {
			if(map.containsKey(a)) {
				map.remove(a);
			}else {
				map.put(a, a);
			}
		}
		
		for(int a : map.keySet()) {
			result = a;
		}
		
		return result;
	}
}
