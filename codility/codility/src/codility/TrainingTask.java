package codility;

import java.util.Stack;

public class TrainingTask {
	
    public int solution(String S) {
    	Stack<Character> stack = new Stack<>();
    	
    	for(char c : S.toCharArray()) {
    		if(c == '(') {
    			stack.add(c);
    		} else {
    			if(stack.size() == 0) return 0;
    			if(stack.peek() == '(') {
    				stack.pop();
    			}
    		}
    	}
    	
    	return stack.size() == 0 ? 1 : 0;
    }
}
