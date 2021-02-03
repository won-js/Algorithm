package codility;

import java.util.Stack;

public class Brackets {
    public int solution(String S) {
        // write your code in Java SE 8
    	Stack<Character> stack = new Stack<>();
    	
    	for(char c : S.toCharArray()) {
    		if(c == '(' || c == '[' || c == '{') {
    			stack.add(c);
    		} else {
    			if(c == ')' && stack.peek() == '(') {
    				stack.pop();
    			} else if(c == ']' && stack.peek() == '[') {
    				stack.pop();
    			} else if (c == '}' && stack.peek() == '{') {
    				stack.pop();
    			} else {
    				return 0;
    			}
    		}
    	}
    	
    	return stack.size() == 0 ? 1 : 0;
    }
}
