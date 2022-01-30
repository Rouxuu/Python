def Fibonacci(n):  # Definiuje funkcję Fibonacci dla zmiennej n
    if n == 0:  # Jeśli n jest równe 0
        return 0  # Funkcja zwraca wartość 0
    elif n == 1:  # Jeśli n jest równe 1
        return 1  # Funkcja zwraca wartość 1
    else:  # We wszystkich innych przypadach
        # Funkcja zwraca wartość działania (n-1) + (n-2)
        return (Fibonacci(n - 1) + Fibonacci(n - 2))


# Program prosi użytkownika o wprowadzenie zmiennej a
a = input("Podaj wyraz ciągu Fibonacciego, który chcesz obliczyć: ")
if int(a) >= 0:  # Jeśli zmienna a jest większa lub równa 0
    # Program zwraca komunikat "Element F(a) ciągu jest równy (wartość funkcji Fibonacci dla a)"
    print("Element F" + a + " ciągu jest równy " + str(Fibonacci(int(a))))
elif int(a) < 0:  # Jeśli zmienna a jest mniejsza od 0
    # Program zwraca komunikat "Nie da się obliczyć ujemnego elementu ciągu Fibonacciego"
    print("Nie da się obliczyć ujemnego elementu ciągu Fibonacciego")
