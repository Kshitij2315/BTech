/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;

class student
{
      private:
        int rollno;
        string name;
        float marks;
        
      public:
      
         student()                                 // Default Constructor 
        {
            name="Kshitij";
            rollno=10;
            marks= 89.4758;
            
            cout<<"I am Constructor\n";
        }
        
        student(int rn, string nm, float mks)     // Parameterised Constructor
        {
            rollno = rn;
            name = nm;
            marks = mks;
        }
        
        student(int rollno) : student()           // Parameterised Constructor
        {
            this->rollno = rollno;
        }
        
        student(int rn, string nm);               // Parameterised Constructor But Outside The Class
        
        student(student &ob)                      // Copy Constructor
        {
            rollno = ob.rollno;
            name = ob.name;
            marks = ob.marks;
        }
        
        void printdata()
        {
            cout<<"Name: "<<name<<"\n";
            cout<<"Roll Number: "<<rollno<<"\n";
            cout<<"Marks: "<<marks<<"\n";
        }
        
        ~student()
        {
            cout<<"I am Destructor\n";
        }

};

student :: student(int rn, string nm) : student()
{
    rollno = rn;
    name = nm;
}

int main()
{
    student obj1, obj2, obj3(11, "Ram", 82.6578);
    student obj4(12), obj5(13, "Shyam");
    
    student obj6(obj3); //Copy Constructor
    
    cout<<"\nobj1\n";
    obj1.printdata();
    cout<<"\nobj2\n";
    obj2.printdata();
    cout<<"\nobj3\n";
    obj3.printdata();
    cout<<"\nobj4\n";
    obj4.printdata();
    cout<<"\nobj5\n";
    obj5.printdata();
    cout<<"\nobj6\n";
    obj6.printdata();
    
    return 0;
}