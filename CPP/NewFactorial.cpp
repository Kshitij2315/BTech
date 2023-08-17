/******************************************************************************



*******************************************************************************/
#include <iostream>

using namespace std;

class factorial
{
    private:
    int num;
    int ans;
    
    void calfact()
    {
        int i;
        
        for(ans=1; num>=1; num--)
        {
            ans = ans * num;
        }
        
        printfact();
    }
    
    void privatefunc()
    {
        cout<<"This is Private Function and cannot be accesed outside the class\n";
    }
    
    public:
    void getdata()
    {
        privatefunc();
        cout<<"\nEnter any Number to Factorize: ";
        cin>>num;
        calfact();
    }
    
    /*void calfact()
    {
        int i;
        
        for(ans=1; num>=1; num--)
        {
            ans = ans * num;
        }
    }*/
    
    void printfact()
    {
        cout<<"Factorial= "<<ans;
    }
};

int main()
{
    factorial obj;
    
    obj.getdata();
    //obj.calfact();
    //obj.printfact();

    return 0;
}