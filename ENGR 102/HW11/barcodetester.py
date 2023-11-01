def barcode():
    file = input("Enter the name of the file: ")
    with open(file) as file:
        barcodes = file.read().strip().split('\n')  # strips the file of whitespace and splits it with newline
    return barcodes


def valid(code):
    sum1 = 0
    sum2 = 0
    for i in range(len(code) - 1):
        if i % 2 == 0:
            sum1 += int(code[i])
        else:
            sum2 += int(code[i])

    last_dig = ((sum2 % 10) * 3)
    x = ((sum1 % 10) + last_dig) % 10
    last_sub = 10 - x  # takes the last digit and subtracts it from 10
    if int(code[-1]) == last_sub:
        return True
    return False


def newfile(barcodes):
    barcodes = '\n'.join(barcodes)
    with open('valid_barcodes.txt', 'w') as validfile:
        validfile.write(barcodes)
    return


barcodes = barcode()
iterations = 0
valid_barcodes = []
for code in barcodes:
    if valid(code):
        iterations += 1
        valid_barcodes.append(code)
newfile(valid_barcodes)
print(f'There are {iterations} valid barcodes')
