package codility;

import java.util.HashSet;
import java.util.Set;

public class Distinct {
	public static void main(String [] args) {
		Distinct d = new Distinct();
		int [] A = {2,1,1,2,3,1};
		System.out.println(d.solution(A));
	}
	
    public int solution(int[] A) {
    	Set<Integer> set = new HashSet<>();
    	for(int a : A) {
    		set.add(a);
    	}
    	return set.size();
    }
}
