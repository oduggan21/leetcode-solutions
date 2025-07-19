impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let n = s.len();
        let m = t.len();

        let mut dp = vec![0; m+1];
        dp[0] = 1;

        for &ch in s.as_bytes(){
            for i in (0..m).rev(){
                if ch == t.as_bytes()[i]{
                    dp[i+1] += dp[i];
                }
            }
        }
        return dp[m]
        
    }
}
