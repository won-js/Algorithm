package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int n, int s) {
    	List<Integer> list = new ArrayList<>();
    	if(s<n) return new int[] {-1};
    	for(int i = n; i>0; i--) {
    		int a = (int) Math.ceil(s/i);
    		list.add(a);
    		s -= a;
    	}
    	
    	list.sort((a,b) -> a-b);
    	int[] answer = new int[list.size()];
    	for(int i=0; i<list.size(); i++) {
    		answer[i] = list.get(i);
    	}
    	
        return answer;
    }
   
}