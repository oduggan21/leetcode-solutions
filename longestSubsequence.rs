impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let mut n1 = text1.chars().count();
        let mut n2 = text2.chars().count();

        let mut dp = vec![vec![0;(n2+1) as usize];(n1+1) as usize];

        for i in (0..n1 as usize).rev(){
            for j in (0..n2 as usize).rev(){
                    if text1[i] == text2[j]{
                        dp[i][j] = 1 + dp[i+1][j+1];
                    }
                    else{
                        dp[i][j] = std::cmp::max(dp[i+1][j], dp[i][j+1]);
                    }
            }
        }
        return dp[0][0]
    }
}
