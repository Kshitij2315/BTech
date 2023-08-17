/******************************************************************************

Write a time class

*******************************************************************************/
#include <iostream>

using namespace std;

class times
{
  private:
    int hh;
    int mm;
    int ss;
    
  public:
    times()
    {
        hh=0;
        mm=0;
        ss=0;
    }   
    
    ~times()
    {
        cout<<"\nThis is destructor\n";
    }   
    
    void sethh(string s)
    {
        cout<<"Another method overloading for testing\n";
    }
    
    void sethh()
    {
        cout<<"Set hh: ";
        cin>>hh;
    }
    
    void sethh(int hh)      //method overloading
    {
        this->hh = hh;
    }
        
    void setmm()
    {
        cout<<"Set mm: ";
        cin>>mm;
    }
    
    void setmm(int mm)      //method overloading
    {
        this->mm = mm;
    }
    
    void setss()
    {
        cout<<"Set ss: ";
        cin>>ss;
    }  
    
    void setss(int ss)      //method overloading
    {
        this->ss= ss;
    }
    
    void dispTime()
    {
        cout<<hh<<":"<<mm<<":"<<ss;
    }
    
    void setTime()
    {
        sethh();
        setmm();
        setss();
    }
    
    times operator++(int)         //Operator overloading
    {
        times temp;
        ss++;
        if (ss > 59)
        {
          mm++;
          ss = 0;
          
          if (mm > 59)
          {
              hh++;
              mm = 0;
              ss = 0;
              
              if (hh > 23)
              {
                  hh = 0;
                  mm = 0;
                  ss = 0;
              }
          }
        }
        
        temp.sethh(hh);
        temp.setmm(mm);
        temp.setss(ss);
        
        return temp;
    }
};

int main()
{
    times obj;
    obj.sethh();
    obj.sethh("string");
    obj.sethh(21);
    /*obj.setmm();
    obj.setss();*/
    
    obj.setTime();
    obj++;
    //obj+=5;
    obj.dispTime();

    return 0;
}