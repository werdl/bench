module main

fn fib(n int) int {
	if n==0 || n==1 {
		return n
	} else {
		return fib(n-1) + fib(n-2)
	}
}

fn main() {
	println(fib(15))
}