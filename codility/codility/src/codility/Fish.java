package codility;

import java.util.Stack;

public class Fish {
    public int solution(int[] A, int[] B) {
        // write your code in Java SE 8
    	/*
    	 *	1. stack�� ����
    	 *	2. ù��° ����⸦ ���
    	 *	3. ���� ���� ����⸦ �����ų�
    	 */
    	Stack<Integer> stack = new Stack<>();
    	int answer = 0;
    	int a = 0;
    	int b = A.length-1;
    	
    	while(true) {
    		if(B[a] == 0) {
    			a++;
    			answer++;
    		}else {
    			break;
    		}
    	}
    	
    	while(true) {
    		if(B[b] == 1) {
    			b--;
    			answer++;
    		} else {
    			break;
    		}
    	}
    	
    	int now = 1;
    	stack.add(A[a+1]);
    	for(int i = a+2; i < b-1; i++) {
    		if(now == B[i]) {
    			stack.add(A[i]);
    		} else {
    			while(stack.size() != 0) {
    				if(stack.peek() > A[i]) {
    					break;
    				} else {
    					stack.pop();
    				}
    			}
    			if(stack.size() == 0) {
    				stack.add(A[i]);
    				now = B[i];
    			}
    		}
    	}
    		
    	return answer + stack.size();
    	
    }
}
