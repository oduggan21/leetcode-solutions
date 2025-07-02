impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let total: i32 = nums.iter().sum();
        if total % 2 != 0 {
            return false;
        }
        let target = total / 2;
        let mut dp = vec![false; (target+1) as usize];
        dp[0]= true;

        for &num in &nums{
            for i in (num as usize ..=target as usize).rev(){
                dp[i] = dp[i] || dp[i-num as usize];
            }
        }
        return dp[target as usize]
    }
}
