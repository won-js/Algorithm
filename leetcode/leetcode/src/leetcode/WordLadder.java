package leetcode;

import java.util.Arrays;
import java.util.List;

public class WordLadder {
	public static void main(String [] args ) {
		String[] words = {"hot","dot","lot","log","cog"};
		List<String> wordList = Arrays.asList(words);
		WordLadder wl = new WordLadder();
		System.out.println(wl.ladderLength("hit", "cog", wordList));
	}
	
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
    	if(wordList == null || !wordList.contains(endWord))
    		return 0;
    }
}
