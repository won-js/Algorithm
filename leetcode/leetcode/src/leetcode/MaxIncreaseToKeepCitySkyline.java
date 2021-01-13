package leetcode;

public class MaxIncreaseToKeepCitySkyline {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
    	int[] top = new int[grid.length], left = new int[grid.length];
    	
    	for(int i =0; i<grid.length; i++) {
    		int max1=0, max2=0;
    		for(int j=0; j<grid[0].length; j++) {
    			max1 = Math.max(max1, grid[j][i]);
    			max2 = Math.max(max2, grid[i][j]);
    		}
    		top[i] = max1;
    		left[i] = max2;
    	}
    	
    	int result = 0;
    	for(int i=0; i<grid.length; i++) {
    		for(int j=0; j<grid.length; j++) {
    			int now = Math.min(top[i], left[j]);
    			result += now - grid[i][j];
    		}
    	}
    	
    	return result;
    }
}
