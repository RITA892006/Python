
print("name:bindu shree")
def collatz_sequence(n):
    
   
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        result = collatz_sequence(num)
        print("Collatz Sequence:", result)
    except ValueError as e:
        print("Error:", e)