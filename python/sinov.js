
#include <iostream>
using namespace std;

int main(){
    while(true){
        int num=0;
        int num2=1;
        int num_temp;
        int num_next=1;
        int n;
        cin >> n;
        if (n>=1)
            cout <<0 <<" ";
        if (n>=2)
            cout <<1<<" ";
        for (int i=0 ;i<n-2;i++){
            num_next=num+num2;
            cout <<num_next<<" ";
            num=num2;
            num2 =num_next;
        }
        cout <<endl;
    }
return 0;
}