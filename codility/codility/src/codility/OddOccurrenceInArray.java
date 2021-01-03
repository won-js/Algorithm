package codility;

import java.util.HashMap;
import java.util.Map;

public class OddOccurrenceInArray {
	public static void main(String [] args) {
		OddOccurrenceInArray oo = new OddOccurrenceInArray();
		int [] A = {9,3,9,3,9,7,9};
		System.out.println(oo.solution(A));
	}
	
	 public int solution(int[] A) {
		 Map<Integer, Integer> map = new HashMap<>();
		 int result = 0;
		 
		 for(int a : A) {
			 if(map.containsKey(a)) {
				 map.remove(a);
			 }else {
				 map.put(a, a);
			 }
		 }
		 
		 for(int a : map.keySet()) {
			 result = a;
		 }
		 
		 return result;
	 }
}
