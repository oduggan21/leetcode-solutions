impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {

        if amount == 0{
            return 0;
        }
        
        if coins.is_empty(){
            return -1;
        }

        let amt = amount as usize;

        let mut dp = vec![amt as i32 + 1; amt+1];
        dp[0] = 0;

        for a in 1..=amt{
            for &c in &coins{
                let coin = c as usize;
                if coin <= a{
                    dp[a] = dp[a].min(dp[a-coin]+1);
                }
            }
        }
        if dp[amt] > amt as i32{
            return -1
        }
        else{
            return dp[amt]
        }
        
    }
}
