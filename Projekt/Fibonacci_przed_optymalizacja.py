def Fibonacci(n):
    # Pierwszy element ciagu to 0
    if n == 0:
        return 0
    # Drugi element ciagu to 1
    elif n == 1:
        return 1
    # Kazdy kolejny to suma dwoch poprzednich, wiec
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))


a = input("Podaj wyraz ciągu Fibonacciego, który chcesz obliczyć: ")

if int(a) == 0:
    print("Wartość F0 jest równa 0")
elif int(a) == 1 or int(a) == 2:
    print("Wartość F1 jest równa 1")
elif int(a) < 0:
    print("Nie da się obliczyć wartośći ujemnego elementu ciągu Fibonacciego")
else:
    print("Wartość F" + a + " jest równa " + str((Fibonacci(int(a)))))
