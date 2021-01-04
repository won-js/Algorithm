package leetcode;

import java.util.Stack;

public class BaseballGame {
	public static void main(String [] args) {
		BaseballGame bg = new BaseballGame();
		String[] ops = {"5","2","C","D","+"};
		
		System.out.println(bg.calPoints(ops));
		
	}
	
	public int calPoints(String[] ops) {
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        
        for(String op : ops) {
            switch(op){
                case "C":
                    stack.pop();
                    break;
                case "D":
                    stack.push(stack.peek()*2);
                    break;
                case "+":
                    int a = stack.pop();
                    int b = stack.peek() + a;
                    stack.push(a);
                    stack.push(b);
                    break;
                default:
                    stack.push(Integer.valueOf(op));
            }
        }
        
        while(!stack.isEmpty()){
            result += stack.pop();
        }
        
        return result;
    }
}
