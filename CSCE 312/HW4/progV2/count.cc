#include <iostream>
#include <fstream>
#include <filesystem> //to delete temp file
#include <string>

using namespace std;

int main(int argc, char **argv)
{
    // Open input file
    ifstream in(argv[1], ios::in);

    // Open output file
    ofstream f("temp.txt", ios::out);

    // Read input file completely using END OF FILE eof() method
    while (!in.eof())
    {
        // Extract line from input file
        string text;
        getline(in, text);

        if (text[0] == '.')
        {
            f << text << endl;
            f << "\n#Basic Block\n\n";
        }
        else if (text[0] == '\t' && text[1] == 'j')
        {
            string temp;
            getline(in, temp);
            if (temp[0] == '.')
            {
                f << text << endl
                  << temp << endl
                  << "\n#Basic Block\n\n";
            }
            else
            {
                f << text << endl
                  << "\n#Basic Block\n\n"
                  << temp << endl;
            }
        }
        else if (text == "\tcall\texit")
        {
            f << "\n#printing count\n\n"
              << "\tmovq\tinsn_count, %rax\n"
              << "\tmovq\t%rax, %rsi\n"
              << "\tleaq\tfmt_string(%rip), %rdi\n"
              << "\tmovl $0, %eax\n"
              << "\tcall printf @PLT\n"
              << text << endl;
        }
        else
        {
            f << text << endl;
        }
    }

    f << ".data\n"
      << "insn_count: .quad 0\n"
      << "fmt_string: .asciz \"%lld instructions executed\"";

    in.close();
    f.close();

    // Open input file
    ifstream tempSrc("temp.txt", ios::in);
    ofstream addq(argv[2], ios::out);

    while (!tempSrc.eof())
    {
        // Extract line from input file
        string text;
        getline(tempSrc, text);

        if (text == "#Basic Block")
        {

            addq << text << endl;
            getline(tempSrc, text);
            addq << text << endl;

            int n = 0;
            string tmp1;
            string tmp2 = "\ttest";
            getline(tempSrc, tmp1);

            if (tmp1[1] != '.')
            {
                n++;
            }

            while (tmp2[0] == '\t' && tmp2[1] != 'j')
            {
                tmp2 = "";
                getline(tempSrc, tmp2);
                if (tmp2[0] == '\t' && tmp2[1] != '.')
                {
                    n++;
                }
                tmp1 = tmp1 + "\n" + tmp2;
            }
            addq << "\taddq $" << n << ",insn_count(%rip)\n"
                 << tmp1 << endl;
        }
        else
        {
            addq << text << endl;
        }
    }

    tempSrc.close();
    addq.close();

    remove("temp.txt"); // delete temp file

    return 0;
}