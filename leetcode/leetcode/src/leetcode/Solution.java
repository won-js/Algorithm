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
    	
    	prefix[0][0] = array[0]; // ���罺���������� �� �����
    	prefix[0][1] = array[0]/N; // ������
    	for(int i=1; i<prefix.length; i++) {
    		
    	}
    }
}