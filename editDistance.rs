use std::cmp::min;
impl Solution {


    pub fn min_distance(word1: String, word2: String) -> i32 {
        let n = word1.len();
        let m = word2.len();

        let mut dp = vec![vec![0;m+1]; n + 1];
       
        for i in (1..n+1){
            dp[i][0]= i;
        }
        for j in (1..m+1){
            dp[0][j] = j;
        }
        
        for i in (1..n+1){
            for j in (1..m+1){
                if word1.as_bytes()[i-1] == word2.as_bytes()[j-1]{
                    dp[i][j] = dp[i-1][j-1];
                }
                else{
                    dp[i][j] =  1+ min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]);
                }
            }
            
        }
        return dp[n][m] as i32;
    }
}
