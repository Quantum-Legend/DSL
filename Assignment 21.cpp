/*
Write C++ program for storing appointment schedule for day. Appointments are booked
randomly using linked list. Set start and end time and min and max duration for visit slot.
Write functions fora) Display free slots
b) Book appointment
c) Cancel appointment ( check validity, time bounds, availability)
d) Sort list based on time
e) Sort list based on time using pointer manipulation*/

#include<iostream>
using namespace std;

int size;	// No of Nodes or Appointments

struct SLL_Node	// Node Structure of each Appointment
{
    int start;
    int end;
    int min;
    int max;
    int flag;
    struct SLL_Node *next;
}*head;


class App_Shedule
{
  public:
	void create_Shed();
         	 
	void display_Shed();

	void book_App();

	void cancel_App();

	void sort_App();
	
}A1;

int main()
{
   int ch;
   char ans;
   
   do
   {    
      cout<<"\n\n *** Menu ***";
      cout<<"\n 1. Create Appointment Schedule";
      cout<<"\n 2. Display Free Slots";
      cout<<"\n 3. Book an Appointment";
      cout<<"\n 4. Cancel an Appointment";
      cout<<"\n 5. Sort slots based on Time";

      
      cout<<"\n\n\t Enter your choice: ";                        
      cin>>ch;
      
      switch(ch)
      {
         case 1: A1.create_Shed();
         	 break;
         	 
         case 2: A1.display_Shed();
         	 break;         	 
         	 
         case 3: A1.book_App();
         	 break;
         	 
         case 4: A1.cancel_App();
         	 break;

         case 5: A1.sort_App();
         	 break;
         	 
         default: cout<<"\n\t Wrong choice!!!";
	          	 
      }
      
      cout<<"\n\n\t Do you wanna continue? (y/n) : ";
      cin>>ans;
   }while(ans == 'y');
   
}

void App_Shedule :: create_Shed()           //Function Definition to create Appointment Schedule
{
    int i;
    struct SLL_Node *temp, *last;
    
    head = NULL;
    
    cout<<"\n\n\t How many Appointment Slots: ";
    cin>>size;
    
    for(i=0; i<size; i++)
    {
       temp = new(struct SLL_Node);         // Step 1: Dynamic Memory Allocation
       
       cout<<"\n\n\t Enter Start Time: ";   // Step 2: Assign Data & Address
       cin>>temp->start; 
       cout<<"\n\t Enter End Time: ";
       cin>>temp->end;
       cout<<"\n\n\t Enter Minimum Duration: ";
       cin>>temp->min;
       cout<<"\n\t Enter Maximum Duration: ";
       cin>>temp->max;
       temp->flag = 0;
       temp->next = NULL;
       
       if(head == NULL)
       {
          head = temp;
          last = head;
       }
       else
       {
          last->next = temp;
          last = last->next;
       }
       
    }
}
