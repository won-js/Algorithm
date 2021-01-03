package codility;

import java.util.HashMap;
import java.util.Map;

public class MaxCounters {
	public static void main(String [] args) {
		MaxCounters mc = new MaxCounters();
		int[] A = {3,4,4,6,1,4,4};
		
		for(int a : mc.solution(5, A )) { 
			System.out.println(a);
		}
	}
	
	public int[] solution(int N, int[] A) {
		int[] result = new int[N];
		Map<Integer, Integer> map = new HashMap<>();
		int max = 0;
		int currMax = 0;
		
		for(int a : A) {
			if(a == N+1) {
				map.clear();
				max += currMax;
				currMax=0;
			} else {
				if(map.containsKey(a)) {
					int temp = map.get(a)+1;
					map.replace(a, temp);
					if(currMax < temp) currMax = temp;
				} else {
					map.put(a, 1);
					if(currMax < 1) currMax=1;
				}
			}
		}
		
		for(int i=0; i<result.length; i++) {
			result[i] = max;
		}
		for(int a : map.keySet()) {
			result[a-1] += map.get(a);
		}
		
		
		return result;
    }
	
}
