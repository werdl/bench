fn fib(n: i32) -> i32 {
    if n==0 || n==1 {
        n
    } else {
        fib(n-1) + fib(n-2)
    }
}

fn main() {
    println!("{}", fib(15));
}