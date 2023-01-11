#include <iostream>
using namespace std;

int main() {
int a;
int b;
char x;
while(true){
    cin >>a>>x>>b;
    switch(x){
        case '*':cout << a*b<<endl;break;
        case '/':cout << a/b<<endl;break;
        case '-':cout << a-b<<endl;break;
        case '+':cout << a+b<<endl;break;
        default :cout<< "'"<< x <<"'bu not`g`ri operator"<<endl;
    }
}
  return 0;
}