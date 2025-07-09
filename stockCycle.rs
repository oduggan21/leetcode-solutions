impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len() <= 0{
            return 0;
        }

        let mut hold = -prices[0];
        let mut buy = 0;
        let mut rest = 0;

        for &p in &prices[1..]{
            hold = std::cmp::max(hold, rest - p);
            rest = std::cmp::max(rest, buy);
            buy = hold + p;
        }
        std::cmp::max(rest, buy)
    }
}
