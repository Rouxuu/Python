def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        print("Nie da się obliczyć ujemnego elementu ciągu Fibonacciego")
        return
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))


a = input("Podaj wyraz ciągu Fibonacciego, który chcesz obliczyć: ")
print("Element F" + a + " ciagu jest rowny " + str(Fibonacci(int(a))))
