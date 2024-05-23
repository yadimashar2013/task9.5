def is_prime(func):
    def wrapper(*args, **kwargs):

        for i in range(2, int(func(*args, **kwargs) % 2) + 1):
            if func(*args, **kwargs) % i == 0:
                print('Составное')
                break
        else:
            print('Простое')

            return func(*args, **kwargs)

    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    result = num1 + num2 + num3
    return result


result = sum_three(2, 3, 6)
print(result)
