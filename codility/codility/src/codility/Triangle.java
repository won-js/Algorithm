package codility;

import java.util.Arrays;

public class Triangle {
	public static void main(String [] args) {
		Triangle t = new Triangle();
		int[] A = {10,2,5,1,8,20};
		
		System.out.println(t.solution(A));
	}
	
    public int solution(int[] A) {    	
    	int result =0;
    	
    	if(A.length < 3) return result;
    	
    	Arrays.sort(A);
    	for(int i=0; i<A.length-2; i++) {
    		if(A[i] < 0) continue;
    		if((long) A[i]+ (long) A[i+1] > (long) A[i+2]) {
    			result =1;
    			break;
    		}
    	}
    	
    	return result;
    }
}
