package leetcode;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
    	
    	//puddle map
    	int [][] puddleMap = new int[m][n];
    	for(int [] puddle : puddles) {
    		puddleMap[puddle[0]-1][puddle[1]-1]++;
    	}
    	
    	// route
    	int[][] route = new int[m][n];
    	
    	for(int i =0; i < m; i++) {
    		if(puddleMap[i][0] == 1) break;
    		route[i][0]++;
    	}
    	
    	for(int i = 0; i < n; i++) {
    		if(puddleMap[0][i] == 1) break;
    		route[0][i]++;
    	}
    	
    	//go
    	for(int i =1; i < m; i++) {
    		for(int j=1; j < n ; j++) {
    			if(puddleMap[i][j] == 1) continue;
    			route[i][j] = (route[i-1][j] + route[i][j-1])%1000000007;
    		}
    	}
    	
    	return route[m-1][n-1];
    }
   
}