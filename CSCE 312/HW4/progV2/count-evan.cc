#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace std;

int main(int argc, char **argv)
{
    // Open input file
    ifstream in(argv[1], ios::in);

    // Open output file
    ofstream f(argv[2], ios::out);

    //# instructions
    int n = 0;

    //checks if it is the first block
    bool first = true;

    //vector full of instructions
    vector<string> instr;

    // Read input file completely using END OF FILE eof() method
    while (!in.eof())
    {
        // Extract line from input file
        string text;
        if (first) {
            getline(in, text);
            instr.push_back(text);
            f << instr[instr.size()-1] << endl;
        }else{
            text = instr[instr.size()-1];
            instr.clear();
            instr.push_back(text);
        }

        if (instr[instr.size()-1][0] == '.')
        {
            if (!first){
                f << instr[instr.size()-1] << endl;
            }

            first = false;

            f << "\n#Basic Block\n\n";
            instr.clear();
            getline(in, text);
            instr.push_back(text);

            while ((instr[instr.size()-1][0] != '.') && !(instr[instr.size()-1][0] == '\t' && instr[instr.size()-1][1] == 'j') && !in.eof()){
                getline(in, text);
                instr.push_back(text);

                if (!(instr[instr.size()-1][1] == '.' && instr[instr.size()-1][0] == '\t')){
                    n++;
                }
            }

            f << "\taddq $"<< n <<",insn_count(%rip)" << endl;

            for (int i = 0; i < instr.size()-1; i++){
                if (instr[i] == "\tcall\texit")
                {
                    f << "\n#printing count\n\n"
                    << "\tmovq\tinsn_count, %rax\n"
                    << "\tmovq\t%rax, %rsi\n"
                    << "\tleaq\tfmt_string(%rip), %rdi\n"
                    << "\tmovl $0, %eax\n"
                    << "\tcall printf @PLT\n";
                }
                f << instr[i] << endl;
            }

            n = 0;

        }
        else if ((instr[instr.size()-1][0] == '\t' && instr[instr.size()-1][1] == 'j'))
        {
            first = false;
            getline(in, text);
            instr.push_back(text);
            if (instr[1][0] == '.')
            {
                  n = 0;
            }
            else
            {
                f << instr[0] << endl
                  << "\n#Basic Block\n\n";
                n = 1;
                while (!(instr[instr.size()-1][0] == '\t' && instr[instr.size()-1][1] == 'j')){
                    getline(in, text);
                    instr.push_back(text);

                    if (!(instr[instr.size()-1][1] == '.' && instr[instr.size()-1][0] == '\t')){
                        n++;
                    }
                }

                f << "\taddq $"<< n <<",insn_count(%rip)" << endl;

                for (int i = 1; i < instr.size()-1; i++){
                    f << instr[i] << endl;
                }

                  n = 0;
            }
        }
    }

    f << ".data\n"
      << "insn_count: .quad 0\n"
      << "fmt_string: .asciz \"%lld instructions executed\"";

    return 0;
}
