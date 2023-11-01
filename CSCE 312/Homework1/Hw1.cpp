#include <iostream>
#include <string>

using namespace std;

void printUsage()
{
    cout << "Usage: ./hex [h | d | b] [h | d | b]" << endl;
}

string toBinary(int n)
{
    string result;

    while (n > 0)
    {
        result = (n % 2 == 0 ? "0" : "1") + result;
        n /= 2;
    }
    return result;
}

int toDecimal(string num, int base)
{
    int result = 0, power = 1;

    for (int i = num.length() - 1; i >= 0; i--)
    {
        if (num[i] == '1')
        {
            result += power;
        }
        power *= base;
    }
    return result;
}

string toHex(int n)
{
    string hexChars = "0123456789ABCDEF", result;

    while (n > 0)
    {
        result = hexChars[n % 16] + result;
        n /= 16;
    }
    return result;
}

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printUsage();
        return 1;
    }

    char from = argv[1][0];
    char to = argv[2][0];
    string num = argv[3];

    if (from == 'h')
    {
        int dec = toDecimal(num, 16);
        if (to == 'd')
        {
            cout << "hexadecimal " << num << " is decimal " << dec << endl;
        }
        else if (to == 'b')
        {
            cout << "hexadecimal " << num << " is binary " << toBinary(dec) << endl;
        }
    }
    else if (from == 'd')
    {
        int dec = stoi(num);
        if (to == 'h')
        {
            cout << "decimal " << dec << " is hexadecimal " << toHex(dec) << endl;
        }
        else if (to == 'b')
        {
            cout << "decimal " << dec << " is binary " << toBinary(dec) << endl;
        }
    }
    else if (from == 'b')
    {
        int dec = toDecimal(num, 2);
        if (to == 'd')
        {
            cout << "binary " << num << " is decimal " << dec << endl;
        }
        else if (to == 'h')
        {
            cout << "binary " << num << " is hexadecimal " << toHex(dec) << endl;
        }
    }
    else
    {
        printUsage();
    }

    return 0;
}