package leetcode;

import java.util.Deque;
import java.util.LinkedList;

public class DailyTemperatures {
	public static void main(String [] args) {
		DailyTemperatures dt = new DailyTemperatures();
		int[] T = {73, 74, 75, 71, 69, 72, 76, 73};
		
		for(int a : dt.dailyTemperatures(T)) {
			System.out.println(a);
		}
	}

	// stack을 이용한 방법
//	public int[] dailyTemperatures(int [] T) {
//		if(T == null || T.length == 0) return null;
//		
//		int[] result = new int[T.length];
//		Stack<Integer> stack = new Stack<>();
//		
//		for(int i=0; i<T.length; i++) {
//			while(!stack.isEmpty() && T[stack.peek()] < T[i]) {
//				result[stack.peek()] = i - stack.pop();
//			}
//			stack.push(i);
//		}
//		return result;
//	}
	
	public int[] dailyTemperatures(int[] T) {
		if(T == null || T.length == 0) return null;
		
		int[] result = new int[T.length];
		Deque<Integer> queue = new LinkedList<>();
		
		for(int i =0; i<T.length; i++) {
			while(!queue.isEmpty() && T[queue.peekLast()] < T[i]) {
				result[queue.peekLast()] = i - queue.pollLast();
			}
			queue.offer(i);
		}
		return result;
	}
}
