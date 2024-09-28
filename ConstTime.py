def get_first_element(arr):
    return arr[0]

def main():
    numbers = [10, 20, 30, 40, 50]
    result = get_first_element(numbers)
    print("The first element is: ", result)

if __name__ == "__main__":
    main()


def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= n
    return product

print(factorial(9))