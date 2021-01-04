package leetcode;

import java.util.Stack;

public class ValidParentheses {
	public static void main(String [] args) {
		ValidParentheses vp = new ValidParentheses();
		String s = "([}}])";
		System.out.println(vp.isValid(s));
	}
	
    public boolean isValid(String s) {
    	if(s.length() % 2 != 0)
    		return false;
    	
    	Stack<Character> stack = new Stack<>();
    	boolean result = false;
    	
    	for(char c : s.toCharArray()) {
    		switch(c) {
    			case '}':
    				if(!stack.empty() && stack.peek() == '{') {
    					stack.pop();
    				}else {
    					stack.push(c);
    				}
    				break;
    			case ')':
    				if(!stack.empty() && stack.peek() == '(') {
    					stack.pop();
    				}else {
    					stack.push(c);
    				}
    				break;
    			case ']':
    				if(!stack.empty() && stack.peek() == '[') {
    					stack.pop();
    				} else {
    					stack.push(c);
    				}
    				break;
    			default:
    				stack.push(c);
    		}
    	}
    	
    	if(stack.isEmpty()) result = true;
    	return result;
    }
}
