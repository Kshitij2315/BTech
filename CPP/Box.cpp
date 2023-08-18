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
    
    box(int l, int b):box(l)       //Calling Constructor from a Constructor
    {
        bre = b;
    }
    
    /*box(box &obj)                //Copy Constructor
    {
        height = obj.height;
        bre = obj.bre;
        len = obj.len;
    }*/
    
    box(box &obj);                //Prototype for Copy Constructor
    
    
    
    void display();               //Prototype declaration of a function
    
    box* operator++(int)
    {
        len = len + 1;
        bre = bre + 1;
        height = height + 1;
        
        return this;
    }
    
    /*box operator++(int)                         //Not Working
    {
        box temp;
        
        temp.len = len + 1;
        temp.bre = bre + 1;
        temp.height = height + 1;
        
        cout<<temp.len<<"\n";
        cout<<temp.bre<<"\n";
        cout<<temp.height<<"\n";
        
        return temp;
    }*/
    
    /*box operator--(int)                         //Not Working
    {
        box temp;
        
        cout<<"This is Operator--\n";
        
        temp.len = len - 1;
        temp.bre = bre - 1;
        temp.height = height - 1;
        
        cout<<temp.len<<"\n";
        cout<<temp.bre<<"\n";
        cout<<temp.height<<"\n";
        
        return temp;
    }*/
    
    box* operator--(int)
    {
        len = len - 1;
        bre = bre - 1;
        height = height - 1;
        
        return this;
    }
    
    void add(box obj)
    {
        len = len + obj.len;
        bre = bre + obj.bre;
        height = height + obj.height;
        
        cout<<"\nans.len: "<<len<<"\n";
        cout<<"ans.bre: "<<bre<<"\n";
        cout<<"ans.height: "<<height<<"\n";
    }
    
    void plus(box obj)
    {
       box obj4;
        
        obj4.len = len + obj.len;
        obj4.bre = bre + obj.bre;
        obj4.height = height + obj.height;
    
        cout<<"\nOutput of plus():- ";
        obj4.display();   
    }
};

void box :: display()             //Scope resolution operator(::) to declare function outside the class
    {
       cout<<"\nThe length is: "<<len<<"\n"
           <<"The breadth is: "<<bre<<"\n"
           <<"The height is: "<<height<<"\n";
    }
    
box::box(box &obj)
{
    height = obj.height;
    bre = obj.bre;
    len = obj.len;
}

int main()
{
    box obj;
    box obj1(42);    
    box obj2(40,10);
    box obj3(obj1);             //Calling Copy Contructor
    
    obj2++;                     //Operator Overloading
    obj2--;                     //Operator Overloading
    
    obj.display();
    obj1.display();
    obj2.display();
    obj3.display();
    
    obj1.add(obj2);
    obj1.plus(obj2);
    
    return 0;
}