// T: O(n log n)
// S: O(n)

pub fn count_bits(n: i32) -> Vec<i32> {
    // Prepare a vector.
    // The first item can just be 0
    let mut vec = Vec::from([0]);

    // Iterate as many as the given number + 1 
    for num in 1..n + 1 {
        // Get a binary string from the number (ex: 2 => 10)
        let num_str = format!("{num:b}");
        // Count '1' from the given binary string
        let cnt = num_str.chars().filter(|c| *c == '1').count();
        // Store the number in the vector
        vec.push(cnt as i32);
    }

    vec
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = count_bits(2);
        assert_eq!(result, Vec::from([0, 1, 1]));

        let result2 = count_bits(5);
        assert_eq!(result2, Vec::from([0, 1, 1, 2, 1, 2]));
    }
}
