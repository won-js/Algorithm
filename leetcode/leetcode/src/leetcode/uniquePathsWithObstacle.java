package leetcode;

public class uniquePathsWithObstacle {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    	int m = obstacleGrid.length;
    	int n = obstacleGrid[0].length;
    	
    	if(obstacleGrid[m-1][n-1] == 1) return 0;
    	
    	// route
    	int[][] route = new int[m][n];
    	
    	for(int i=0; i<m; i++) {
    		if(obstacleGrid[i][0] == 1) break;
    		route[i][0]++;
    	}
 
    	for(int i =0; i<n; i++) {
    		if(obstacleGrid[0][i] == 1) break;
    		route[0][i]++;
    	}
    	
    	//go
    	for(int i=1; i<m; i++) {
    		for(int j=1; j<n; j++) {
    			if(obstacleGrid[i][j] == 1) continue;
    			route[i][j] = route[i-1][j] + route[i][j-1];
    		}
    	}
    	
    	return route[m-1][n-1];
    }
}
