package codility;

import java.util.HashMap;
import java.util.Map;

public class FrogRiverOne {
	public static void main(String [] args) {
		FrogRiverOne fro = new FrogRiverOne();
		int [] A = {1,3,1,4,2,3,5,4};
		System.out.println(fro.solution(5, A));
	}
	
	public int solution(int X, int[] A) {
		int result = -1;
		Map<Integer, Integer> map = new HashMap<>();
		
		for(int i=0; i<A.length ; i++) {
			if(!map.containsKey(A[i])) {
				map.put(A[i], 1);
				if(map.size() == X) {
					result = i;
					break;
				}
			}
		}
		
		return result;
    }
}
