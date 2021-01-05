package leetcode;

class Solution {
	public static void main(String [] args) {
		
	}
	
    public int[] solution(int N, int[] stages) {
    	double [] array = new double[N];
    	double[][] prefix = new double[N][1];
    	int complete = 0;
    	
    	for(int stage : stages) {
    		if(stage>N) {
    			complete++;
    		}else {
    			array[stage-1]++;
    		}
    	}
    	
    	prefix[0][0] = array[0]; // 현재스테이지까지 온 사람들
    	prefix[0][1] = array[0]/N; // 실패율
    	for(int i=1; i<prefix.length; i++) {
    		
    	}
    }
}