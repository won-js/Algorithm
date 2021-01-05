package leetcode;

public class MaxAreaOfIsland {

	public static void main(String[] args) {
		int[][] grid = {{1,1,0,1,1},
						{0,1,1,0,0},
						{0,0,0,0,0},
						{1,1,0,1,1},
						{1,0,1,1,1},
						{1,0,1,1,1}};
		MaxAreaOfIsland ma = new MaxAreaOfIsland();
		System.out.println(ma.maxAreaOfIsland(grid));
	}
	
    public int maxAreaOfIsland(int[][] grid) {
        //1
    	if(grid == null || grid.length == 0)
    		return 0;
    	
    	m = grid.length;
    	n = grid[0].length;
    	int max = 0;
    	
    	for(int i =0; i<m; i++) {
    		for(int j=0; j<n; j++) {
    			if(grid[i][j] == 1) {
    				int area = dfs(grid, i , j, 0);
    				max = Math.max(area, max);
    			}
    		}
    	}
    	return max;
    }
    
    private static int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
    private static int m, n;
    
    private static int dfs(int[][] grid, int x , int y, int area) {
    	//1
    	if(x<0 || x >= m || y<0 || y>=n || grid[x][y]==0) 
    		return area;
    	
    	//2 1인 육지가 들어오는 경우
    	grid[x][y] = 0;
    	area++;
    	
    	for(int[] dir : dirs) {
    		area = dfs(grid, x+dir[0], y+dir[1], area);
    	}
    	return area;
    }
}
