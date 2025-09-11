use std::sync::OnceLock;

static _TABLE: OnceLock<Vec<i32>> = OnceLock::new();

impl Solution {

    pub fn reverse_bits(mut n: i32) -> i32 {
        let mut x: u32 = 0;
        for i in 0..6 {
            let shift = if i == 5 {2} else {6} as u32;
            x = x << shift | Self::init_table()[(n & (1 << shift) - 1) as usize] as u32 >> 6 - shift;
            n >>= 6;
        }
        x as i32
    }
    
    fn init_table() -> &'static Vec<i32> {
        _TABLE.get_or_init(|| {
            let mut table: Vec<i32> = vec![0; 1 << 6];
            for (i, x) in table.iter_mut().enumerate() {
                let mut j = i as i32;
                for k in 0..6 {
                    *x = *x << 1 | j & 1;
                    j >>= 1;
                }
            }
            table
        })
    }

}
