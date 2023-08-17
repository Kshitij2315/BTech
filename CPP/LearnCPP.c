/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;

class factorial
{
    private:
    int num;
    int i;
    int ans;
    
    public:
    void getdata()
    {
        cout<<"Enter any Number to Factorize: ";
        cin>>num;
    }
    
    void calfact()
    {
        for(ans=1; num>=1; num--)
        {
            ans = ans * num;
        }
    }
    
    void printfact()
    {
        cout<<"Factorial= "<<ans;
    }
};

int main()
{
    factorial obj;
    
    obj.getdata();
    obj.calfact();
    obj.printfact();

    return 0;
}