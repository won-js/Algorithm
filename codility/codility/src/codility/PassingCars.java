package codility;

public class PassingCars {
	public static void main(String [] args) {
		PassingCars ps = new PassingCars();
		int[] A = {0,1,0,1,1};
		
		System.out.println(ps.solution(A));
	}
	
    public int solution(int[] A) {
    	int count = 0;
    	int result = 0;
    	
    	for(int i=0; i<A.length; i++) {
    		if(A[i] == 0) {
    			count++;
    		}else {
    			result += count;
    		}
    		if(result > 1000000000) return -1;
    	}
    	
    	return result;
    }
}
