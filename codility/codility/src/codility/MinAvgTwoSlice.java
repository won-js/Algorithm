package codility;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinAvgTwoSlice {
	public static void main(String [] args) {
		MinAvgTwoSlice mats = new MinAvgTwoSlice();
		int[] A = {4,2,2,5,1,5,8};
		System.out.println(mats.solution(A));
	}
	
    public int solution(int[] A) {
    	Map<Integer, List<Integer>> map = new HashMap<>();
    	int min = 999999;
    	int result = 0;
    	
    	for(int i=0; i<A.length-1; i++) {
    		int sum = A[i];
    		List<Integer> list = new ArrayList<>();
    		for(int j=i+1;j < A.length; j++) {
    			sum += A[j];
    			list.add(sum);
    		}
    		map.put(i, list);
    	}
    	
    	for(int i=0; i<A.length-1; i++) {
    		List<Integer> list = map.get(i);
    		int k = 2;
    		for(int j=0; j<list.size(); j++) {
    			if(min > list.get(j)/k) {
    				min = list.get(j)/k;
    				result = i;
    			}
    			j++;
    		}
    	}
    	return result;
    }
	
}
