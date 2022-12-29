/*
Queues are frequently used in computer programming, and a typical example is the
creation of a job queue by an operating system. If the operating system does not use
priorities, then the jobs are processed in the order they enter the system. Write C++
program for simulating job queue. Write functions to add job and delete job from queue.
*/
#include <iostream>
#include <string.h>
using namespace std;

#define Size 5
class jobq
{
    private:
    int f, r;
    public:
    string q[Size];
    jobq()
    {
        f = -1;
        r = -1;
    }
    bool empty()
    {
        if(f == -1 && r == -1)
            return true;
        else
            return false;
    }
    bool full()
    {
        if(r == Size-1)
            return true;
        else
            return false;
    }
    void insert(string x)
    {
        if(full())
            cout << "ERROR: OVERFLOW - Queue is full. " << x << " could not be inserted" << endl;
        else
        {
            if (f == -1) {f = 0;}
            r++;
            q[r] = x;
            cout << x << " is inserted in the Queue" << endl;
        }
    }
    void del()
    {
        if(empty())
            cout << "ERROR: UNDERFLOW - Queue is empty" << endl;
        else
        {
            if(f == r)
            {
                cout << q[f] << " is deleted from front" << endl;
                f = r =-1;
            }
            else
            {
                cout << q[f] << " is deleted from front" << endl;
                f++;
            }
        }
    }
    void display()
    {
        if(empty())
            cout << "The Queue is empty";
        else
        {
            cout << "The Queue is: ";
            for(int i = f; i <= r; i++)
                cout << q[i] << " | ";
        }
        cout << endl;
    }
};
int main()
{
    jobq q1;
    q1.insert("Job 1");
    q1.insert("Job 2");
    q1.insert("Job 3");
    q1.display();
    q1.insert("Job 4");
    q1.insert("Job 5");
    q1.display();
    q1.insert("Job 6");
    q1.display();
    q1.del();
    q1.display();
    q1.del();
    q1.display();
    q1.del();
    q1.display();
    q1.del();
    q1.display();
    q1.del();
    q1.display();
    q1.del();
    q1.display();
}
