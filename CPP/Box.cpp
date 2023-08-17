/******************************************************************************

box.cpp

*******************************************************************************/
#include <iostream>

using namespace std;

class box
{
  private:
    int len;
    int bre;
    int height;
    
  public:
    box()
    {
        len=0;
        bre=0;
        height=0;
    }
    
    box(int l)
    {
        len = l;
    }
    
    box(int l, int b):box(l)      //Calling Constructor from a Constructor
    {
        bre = b;
    }
    
    void display();   //Prototype declaration of a function
};

void box :: display()   //Scope resolution operator(::) to declare function outside the class
    {
       cout<<"\nThe length is: "<<len<<"\n"
           <<"The breadth is: "<<bre<<"\n"
           <<"The height is: "<<height<<"\n";
    }

int main()
{
    box obj;
    box obj1(42);    
    box obj2(40,10);
    
    obj.display();
    obj1.display();
    obj2.display();

    return 0;
}