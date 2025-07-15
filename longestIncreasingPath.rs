impl Solution {
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        let rows = matrix.len();
        if rows == 0 || matrix[0].is_empty() {
            return 0;
        }
        let cols = matrix[0].len();
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)];
        let mut dp = vec![vec![0; cols]; rows];

        fn dfs(
            i: usize,
            j: usize,
            matrix: &Vec<Vec<i32>>,
            dp: &mut Vec<Vec<i32>>,
            dirs: &[(i32, i32)],
        ) -> i32 {
            if dp[i][j] != 0 {
                return dp[i][j];
            }
            let mut best = 1;
            let rows_i32 = matrix.len() as i32;
            let cols_i32 = matrix[0].len() as i32;

            for &(di, dj) in dirs {
                let ni = i as i32 + di;
                let nj = j as i32 + dj;
                if (0..rows_i32).contains(&ni)
                    && (0..cols_i32).contains(&nj)
                    && matrix[ni as usize][nj as usize] > matrix[i][j]
                {
                    best = std::cmp::max(
                        best,
                        1 + dfs(ni as usize, nj as usize, matrix, dp, dirs),
                    );
                }
            }

            dp[i][j] = best;
            best
        }

        let mut ans = 0;
        for i in 0..rows {
            for j in 0..cols {
                ans = std::cmp::max(ans, dfs(i, j, &matrix, &mut dp, &dirs));
            }
        }
        ans
    }
}

