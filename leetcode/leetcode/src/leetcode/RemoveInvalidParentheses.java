package leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

public class RemoveInvalidParentheses {
	
	public List<String> removeInvalidParentheses(String s) {
        List<String> res = new ArrayList<>();
        if (s == null)
        	return res;
        
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer(s);
        visited.add(s);
        boolean found = false;
        
        while(!queue.isEmpty()) {
        	int size = queue.size();
        	for(int i=0; i<size; i++) {
        		String str = queue.poll();
        		if(isValid(str)) {
        			res.add(str);
        			found = true;
        		}
        		if(found) continue;
        		//0-7 -> 0-6
        		for(int j=0; j < str.length(); j++) {
        			//1
        			if(str.charAt(j) != '(' && str.charAt(j) != ')') continue;
        			
        			//2
        			String newStr = str.substring(0,j)+str.substring(j+1);
        			if(!visited.contains(newStr)) {
        				queue.offer(newStr);
        				visited.add(newStr);
        			}
        		}
        	}
        }
        return res;
    }
	
	private boolean isValid(String s) {
		int count = 0;
		for(char c : s.toCharArray()) {
			if(c == '(') {
				count++;
			}else if (c == ')') {
				count--;
				if(count < 0) return false;
			}
		}
		return count == 0 ? true : false;
	}
	
}
