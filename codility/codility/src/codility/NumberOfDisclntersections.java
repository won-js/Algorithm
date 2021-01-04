package codility;

import java.util.Arrays;

public class NumberOfDisclntersections {
	public static void main(String [] args ) {
		//아직 못품
		NumberOfDisclntersections nd = new NumberOfDisclntersections();
		int [] A = {1,5,2,1,4,0};
		
		System.out.println(nd.solution(A));
	}
	
    public int solution(int[] A) {
    	int n = A.length;
    	int[] lower = new int[n];
    	int[] upper = new int[n];
    	
    	for(int i=0; i<n; i++) {
    		lower[i] = i - A[i];
    		upper[i] = i + A[i];
    	}
    	
    	Arrays.sort(lower);
    	Arrays.sort(upper);
    	
    	int intersection = 0;
    	int j =0;
    	
    	for(int i=0; i<n; i++) {
    		while(j <n && upper[i] >= lower[i]) {
    			
    		}
    	}
    	
    	return 1;
    }
}
