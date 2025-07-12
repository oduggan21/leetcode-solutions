impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let n = s1.len();
        let s = s2.len();

        if n + s != s3.len(){
            return false
        }

        let n = n as usize;
        let s = s as usize;

        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let s3 = s3.as_bytes();

        let mut dp = vec!(vec!(false;s+1); n+1);
        dp[0][0] = true;

        for i in 0..=n{
            for j in 0..=s{
                if i > 0 && s1[i-1] == s3[i+j-1]{
                    dp[i][j] |= dp[i-1][j];
                }
                if j > 0 && s2[j-1] == s3[i+j-1]{
                    dp[i][j] |= dp[i][j-1];
                }
            }
        }
        dp[n][s]
    }
}
