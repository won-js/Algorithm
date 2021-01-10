package codility;

import java.util.HashMap;
import java.util.Map;

public class Solution {
	public static void main(String [] args) {
		Solution s = new Solution();
		String str1 = "handshake";
		String str2 = "shake hands";
		System.out.println(s.solution(str1, str2));
	}
	
	
	public int solution(String str1, String str2) {
    	Map<String, Integer> map1 = new HashMap<>();
    	Map<String, Integer> map2 = new HashMap<>();
    	
    	for(int i=0; i < str1.length()-1 ; i++) {
    		char first = str1.charAt(i);
    		char second = str1.charAt(i+1);
    		if('A' <= first && first <= 'Z' || 'a' <= first && first <= 'z') {
    			if('A' <= second && second <= 'Z' || 'a' <= second && second <= 'z') {
    				String str = (first +""+ second).toUpperCase();
    				if(map1.containsKey(str)) {
    					map1.replace(str, map1.get(str)+1);
    				}else {
    					map1.put(str, 1);
    				}
    			}
    		}
    	}
    	
    	for(int i=0; i < str2.length()-1 ; i++) {
    		char first = str2.charAt(i);
    		char second = str2.charAt(i+1);
    		if('A' <= first && first <= 'Z' || 'a' <= first && first <= 'z') {
    			if('A' <= second && second <= 'Z' || 'a' <= second && second <= 'z') {
    				String str = (first +""+ second).toUpperCase();
    				if(map2.containsKey(str)) {
    					map2.replace(str, map2.get(str)+1);
    				}else {
    					map2.put(str, 1);
    				}
    			}
    		}
    	}
    	
    	int sum = 0;
    	int div = 0;
    	
    	for(String key : map1.keySet()) {
    		int num1 = map1.get(key);
    		int num2 = 0;
    		if(map2.get(key) != null) {
    			num2 = map2.get(key);
    		}
    		if(num2 != 0) {
    			sum += Math.max(num1, num2);
    			div += Math.min(num1, num2);
    		}else {
    			sum += num1;
    		}
    		map2.remove(key);
    	}
    	
    	for(String str : map2.keySet()) {
    		sum += map2.get(str);
    	}
    	if(sum == 0) return 65536;
    	return 65536*div/sum;
    }
}
