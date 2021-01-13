package leetcode;

public class RichestCustomerWealth {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        
        for(int[] account : accounts) {
        	int sum = 0;
        	for(int num : account) {
        		sum += num;
        	}
        	max = Math.max(sum, max);
        }
        
        return max;
    }
}
