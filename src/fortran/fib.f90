program fibonacci
  integer :: n, result

  ! Set the value of n
  n = 15 

  ! Calculate Fibonacci
  result = fibonacci_recursive(n)

  ! Display the result
  print *, result

contains

  recursive function fibonacci_recursive(m) result(fib)
    integer, intent(in) :: m
    integer :: fib

    if (m <= 0) then
      fib = 0
    else if (m == 1) then
      fib = 1
    else
      fib = fibonacci_recursive(m - 1) + fibonacci_recursive(m - 2)
    end if
  end function fibonacci_recursive

end program fibonacci