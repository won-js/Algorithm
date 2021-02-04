package codility;

import java.util.Stack;

public class StoneWall {
    public int solution(int[] H) {
        // write your code in Java SE 8
    	Stack<Integer> stack = new Stack<>();
    	int answer = 1;
    	stack.add(H[0]);
    	
    	for(int i = 1; i<H.length; i++) {
    		if(stack.peek() < H[i]) {
    			answer++;
    		} else if(stack.peek() > H[i]) {
    			while(!stack.isEmpty()) {
    				if(stack.peek() > H[i]) {
    					stack.pop();
    				}else if(stack.peek() == H[i]){
    					break;
    				}else {
    					answer++;
    				}
    			}
    			if(stack.isEmpty()) answer++;
    			stack.add(H[i]);
    		}
    	}
    	
    	return answer;
    }
}
