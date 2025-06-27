impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut current_product = nums[0];
        let mut current_product_min = nums[0];
        let mut max_product = nums[0];

        for &num in nums.iter().skip(1){
            if num < 0{
                std::mem::swap(&mut current_product, &mut current_product_min);
            }
            
            current_product = std::cmp::max(num, current_product * num);
            current_product_min = std::cmp::min(num, current_product_min * num);
            max_product = std::cmp::max(current_product, max_product);

        }
        max_product
    }
}
