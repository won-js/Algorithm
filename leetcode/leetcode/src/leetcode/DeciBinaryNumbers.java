package leetcode;

public class DeciBinaryNumbers {
    public int minPartitions(String n) {
        int max = 0;
        for(char c : n.toCharArray()) {
        	max = Math.max(max, Character.getNumericValue(c));
        }
        return max;
    }
}
