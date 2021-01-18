package leetcode;

import java.util.PriorityQueue;

public class LastStone {
    public int lastStoneWeight(int[] stones) {
    	PriorityQueue<Integer> queue = new PriorityQueue<Integer>((a,b) -> b-a);
    	for(int stone : stones) {
    		queue.add(stone);
    	}
    	
    	int y,x;
    	while(queue.size() > 1)  {
    		y = queue.poll();
    		x = queue.poll();
    		if(y >= x) {
    			queue.add(y-x);
    		}
    	}
    	
    	return queue.size() == 0 ? 0 : queue.poll();
    }
}
