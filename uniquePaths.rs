impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {

        if n == 1 || m == 1{
            return 1;
        }
        let mut dp = vec![vec![1;n as usize];m as usize];

        for i in (1..m as usize){
            for j in (1..n as usize){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[(m-1) as usize][(n-1) as usize]

    }
}
