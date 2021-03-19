#include<bits/stdc++.h>
using namespace std;
int main(){
long long a,b;
cin >> a >> b;
for(int i = 0; i < b- 1; i++)
cout << a / b << " ";
cout << a/b+a%b;
}