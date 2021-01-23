package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class CourseSchedule {
	public static void main(String [] args) {
		int course = 4;
		int[][] nums = {{1,0},{2,1},{3,2}};
		int[][] nums2 = {{1,0},{0,1}};
		
		CourseSchedule cs = new CourseSchedule();
		System.out.println(cs.canFinish(course, nums2));
	}
	
    public boolean canFinish(int numCourses, int[][] prerequisites) {
    	if(numCourses <= 0) return false;
    	
    	//1. inDegree 배열, Queue
    	Queue<Integer> queue = new LinkedList<>();
    	int[] inDegree = new int[numCourses];
    	
    	// 1-1 inDegree
    	int numsLength = prerequisites.length;
    	for(int i =0; i<numsLength; i++) {
    		inDegree[prerequisites[i][1]]++;
    	}
    	
    	//1-2 큐에 넣는다, 3을 찾는다
    	int inDegreeLength = inDegree.length;
    	for(int i = 0; i<inDegreeLength; i++) {
    		if(inDegree[i] == 0)
    			queue.offer(i);
    	}
    	
    	//
    	while(!queue.isEmpty()) {
    		int firstZeroVal = queue.poll();
    		
    		for(int i=0; i<numsLength; i++) {
    			if(firstZeroVal == prerequisites[i][0]) {
    				inDegree[prerequisites[i][1]]--;
    				if(inDegree[prerequisites[i][0]] == 0)
    					queue.offer(prerequisites[i][1]);
    			}
    		}
    	}
    	
    	// 4
    	for(int i =0; i < inDegreeLength; i++) {
    		if(inDegree[i] != 0)
    			return false;
    	}
    	
    	return true;
    }
}
