package codility;

public class GenomicrangeQuery {
	public static void main(String [] args) {
		GenomicrangeQuery gq = new GenomicrangeQuery();
		int[] P = {2,5,0};
		int[] Q = {4,5,6};
		
		for(int num : gq.solution("CAGCCTA", P, Q)) {		
			System.out.println(num);
		}
	}
	
    public int[] solution(String S, int[] P, int[] Q) {
    	int[] result = new int[P.length];
    	char[] array = S.toCharArray();
    	int[] A = new int[array.length+1];
    	int[] C = new int[array.length+1];
    	int[] G = new int[array.length+1];
    	
    	for(int i=0; i<array.length; i++) {
    		if(array[i] == 'A') {
    			A[i+1]++;
    		}else if(array[i] == 'C') {
    			C[i+1]++;
    		}else if(array[i] == 'G') {
    			G[i+1]++;
    		}
    		A[i+1] += A[i];
    		C[i+1] += C[i];
    		G[i+1] += G[i];
    	}
    	
    	for(int i=0; i<P.length; i++) {
    		if(A[P[i]] != A[Q[i]+1]) {
    			result[i] = 1;
    		}else if(C[P[i]] != C[Q[i]+1]) {
    			result[i] = 2;
    		}else if(G[P[i]] != G[Q[i]+1]) {
    			result[i] = 3;
    		}else {
    			result[i] = 4;
    		}
    	}
    	return result;
    }
}
