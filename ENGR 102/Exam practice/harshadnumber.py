n = int(input("Enter an integer: "))

nums = []

sum = 0

finValue = 0




nums.append(n // 100)

nums.append(n % 100 // 10)

nums.append(n % 100 % 10)




sum = nums[0] + nums[1] + nums[2]

finValue = n % sum




if int(finValue) != 0:
    print(f'{n} is not a harshad number.')
else:
    print(f'{n} is a harshad number.')