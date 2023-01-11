// // Online C++ compiler to run C++ program online
// #include <iostream>

// using namespace std;
// int main() {
//     int a,b;
//     while (true){
//         cin>>a>>b;
//         if (a>b ){
//             cout <<a/b+1<<endl;
//         }
//         else if(a==b){
//             cout <<a/b+1<<endl;
//         }
        
        
        
//         else{
//             cout <<1<<endl;
//         }
//     }
//     return 0;
// }

// Online C++ compiler to run C++ program online
#include <iostream>
#include <cstdlib>
using namespace std;
int main() {
    srand(time(0)
    int a=1+(rand()%6);
    int b=1+(rand()%6);
    cout<<a;
    cout<<b;
    int l;
    cin >>l;
    if (l==a+b){
        cout <<"to`g`ri";
    }
    else{
        cout <<"noto`g`ri";
    }

    return 0;
}