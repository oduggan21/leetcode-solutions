impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![1; n+1];

        for i in (1..n){
            for j in (0..i).rev(){
                if nums[j] < nums[i]{
                    dp[i] = std::cmp::max(dp[i], dp[j]+1);
                }
            }
        }
        *dp.iter().max().unwrap() as i32
     
    }
}
