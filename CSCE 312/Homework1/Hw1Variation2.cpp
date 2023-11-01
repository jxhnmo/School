#include <cstdlib>
#include <stdio.h>

using namespace std;

// Hexadecimal to integer
int hexToInt(char *hex)
{
    int val = 0;
    while (*hex)
    {

        val *= 16;

        if (*hex >= '0' && *hex <= '9')
        {
            val += (*hex - '0');
        }
        else if (*hex >= 'a' && *hex <= 'f')
        {
            val += (*hex - 'a' + 10);
        }

        hex++;
    }
    return val;
}

// Binary to integer
int binToInt(char *bin)
{

    int val = 0, power = 1;

    while (*bin)
    {

        power *= 2;

        if (*bin++ == '1')
        {
            val += power;
        }
    }

    return val;
}

// Decimal to integer
int decToInt(char *dec)
{
    int val = 0;
    while (*dec)
    {
        val = 10 * val + (*dec++ - '0');
    }
    return val;
}

// Integer to hexadecimal
void intToHex(int n)
{
    if (n > 0)
    {
        intToHex(n / 16);
        putchar("0123456789abcdef"[n % 16]);
    }
}

// Integer to binary
void intToBin(int n)
{
    if (n > 0)
    {
        intToBin(n / 2);
        putchar('0' + (n % 2));
    }
}

// Integer to decimal
void intToDec(int n)
{
    if (n > 0)
    {
        intToDec(n / 10);
        putchar('0' + (n % 10));
    }
}

void printUsage()
{
    putchar('U'), putchar('s'), putchar('a'), putchar('g'), putchar('e'), putchar(':');
    putchar(' '), putchar('.'), putchar('/'), putchar('h'), putchar('e'), putchar('x'), putchar(' ');
    putchar('['), putchar('h'), putchar('|'), putchar('d'), putchar('|'), putchar('b'), putchar(']'), putchar(' ');
    putchar('['), putchar('h'), putchar('|'), putchar('d'), putchar('|'), putchar('b'), putchar(']');

    putchar('\n');
    exit(1);
}

void printInput(char *input)
{
    if (*input == '\0')
        return;
    putchar(*input);
    printInput(input + 1);
}

// Main function
int main(int argc, char *argv[])
{

    // Validate input
    if (argc != 4)
    {
        printUsage();
    }

    int n;
    // Convert input to int
    if (*argv[1] == 'h' && (*argv[2] == 'b' || *argv[2] == 'd'))
    {
        n = hexToInt(argv[3]);

        putchar('h'), putchar('e'), putchar('x'), putchar('a'), putchar('d'), putchar('e'), putchar('c'), putchar('i'), putchar('m'), putchar('a'), putchar('l');
    }
    else if (*argv[1] == 'b' && (*argv[2] == 'h' || *argv[2] == 'd'))
    {
        n = binToInt(argv[3]);

        putchar('b'), putchar('i'), putchar('n'), putchar('a'), putchar('r'), putchar('y');
    }
    else if (*argv[1] == 'd' && (*argv[2] == 'h' || *argv[2] == 'b'))
    {
        n = decToInt(argv[3]);

        putchar('d'), putchar('e'), putchar('c'), putchar('i'), putchar('m'), putchar('a'), putchar('l');
    }
    else
    {
        printUsage();
    }

    // output input value
    putchar(' ');
    printInput(argv[3]);
    putchar(' '), putchar('i'), putchar('s'), putchar(' ');

    // Convert int to output

    if (*argv[2] == 'h')
    {
        putchar('h'), putchar('e'), putchar('x'), putchar('a'), putchar('d'), putchar('e'), putchar('c'), putchar('i'), putchar('m'), putchar('a'), putchar('l'), putchar(' ');
        intToHex(n);
    }
    else if (*argv[2] == 'b')
    {
        putchar('b'), putchar('i'), putchar('n'), putchar('a'), putchar('r'), putchar('y'), putchar(' ');
        intToBin(n);
    }
    else if (*argv[2] == 'd')
    {
        putchar('d'), putchar('e'), putchar('c'), putchar('i'), putchar('m'), putchar('a'), putchar('l'), putchar(' ');
        intToDec(n);
    }

    putchar('\n');
    return 0;
}