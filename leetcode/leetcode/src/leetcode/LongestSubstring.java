package leetcode;

import java.util.ArrayList;
import java.util.List;

public class LongestSubstring {
	public static void main(String [] args) {
		LongestSubstring ls = new LongestSubstring();
		String s = "a";
		System.out.println(ls.lengthOfLongestSubstring(s));
	}
	
    public int lengthOfLongestSubstring(String s) {
    	if(s.length() == 0) return 0;
    	char[] array = s.toCharArray();
    	List<Character> list = new ArrayList<>();
    	int max = 1;
    	
    	for(int i =0; i<array.length-1; i++) {
    		list.add(array[i]);
    		for(int j=i+1; j<array.length; j++) {
    			if(!list.contains(array[j])) {
    				list.add(array[j]);
    			} else {
    				break;
    			}
    		}
    		max = Math.max(max, list.size());
    		list.clear();
    	}
    	
    	return max;
    }
}
