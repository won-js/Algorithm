package leetcode;

import java.util.Arrays;

public class coinChange {

	public static void main(String[] args) {
		int[] coins = { 1, 2, 5 };
		int amount = 11;
		coinChange cc = new coinChange();
		System.out.println(cc.coinChange(coins, amount));
	}

	public int coinChange(int[] coins, int amount) {
		
		// 1
		int max = amount + 1;
		int[] dp = new int[max];
		Arrays.fill(dp, max);
		dp[0] = 0;
		
		//2
		for(int i = 1; i <= amount; i++) {
			for(int coin : coins) {
				if(i >= coin) {
					dp[i] = Math.min(dp[i], dp[i -coin] +1);
				}
			}
		}
		
		return dp[amount]> amount ? -1 : dp[amount];
	}
}
