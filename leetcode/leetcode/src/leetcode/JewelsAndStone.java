package leetcode;

import java.util.HashSet;
import java.util.Set;

public class JewelsAndStone {
	public static void main(String [] args) {
		JewelsAndStone jas = new JewelsAndStone();
		System.out.println(jas.numJewelsInStones("aA", "aAAbbbb"));
	}
	
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> set = new HashSet<>();
        int result = 0;
        
        for(char jewel : jewels.toCharArray()) {
        	set.add(jewel);
        }
        
        for(char stone : stones.toCharArray()) {
        	if(set.contains(stone)) result++;
        }
        
        return result;
    }
}
