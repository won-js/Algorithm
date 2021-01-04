package leetcode;

import java.util.PriorityQueue;
import java.util.Queue;

public class KClosestPointsToOrigin {
    public int[][] kClosest(int[][] points, int K) {
    	int[][] result = new int[K][2];
    	Queue<int[]> queue = new PriorityQueue<>(points.length, (a,b) -> (a[0]*a[0]+a[1]*a[1])-(b[0]*b[0]+b[1]*b[1]));
    	
    	for(int[] point : points) {
    		queue.offer(point);
    	}
    	for(int i=0; i<result.length; i++) {
    		result[i] = queue.poll();
    	}
    	return result;
    }
}
