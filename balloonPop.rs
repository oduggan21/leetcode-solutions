impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let mut balloons: Vec<i32> = Vec::with_capacity(nums.len()+2);
        balloons.push(1);
        balloons.extend(nums);
        balloons.push(1);

        let mut n = balloons.len();
        let mut dp = vec!(vec!(0;n);n);
        let mut coins: i32 = 0;
        
        for length in (2..n){
            for i in 0..(n-length){
                let mut j = i + length;
                for k in ((i+1)..j){
                    coins = balloons[i] * balloons[k] * balloons[j];
                    coins += dp[i][k] + dp[k][j];

                    dp[i][j] = std::cmp::max(dp[i][j], coins);
                }
            }
        }

        dp[0][n-1]

    }
}
