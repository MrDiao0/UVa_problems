#include <iostream>
using namespace std;

unsigned long long int x;
int mod(int a,int n,int m){
	if(n>1 && n%2==0){
		x = mod(a,n>>1,m);
		return (x*x)%m;
	}
	else if(n>1){
		x = mod(a,(n-1)>>1,m);
		return (((x*x)%m)*a)%m;
	}
	else{
		return a;
	}
}

int main(){
	unsigned long long int B,p,M;
	while(cin>>B){
		cin >> p >> M;

		if(p>0){ cout << mod(B,p,M) << endl; }
		else{ cout << 1%M << endl; }
	}
}