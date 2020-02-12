//UVa: 10810 - Ultra-QuickSort
#include <vector>
#include <iostream>
using namespace std;

vector<long long int> num;

long long int flip(int low, int hi){
	long long int r = 0;
	if(hi-low <= 1){
		return 0;
	}
	int mid = low + ((hi-low)/2);
	vector<long long int> aux;
	int a = low;
	int b = mid;

	r = flip(low,mid);
	r = r + flip(mid,hi);

	while(a<mid && b<hi){
		if(num[a] <= num[b]){
			aux.push_back(num[a]);
			a++;
		}else if(num[a]>num[b]){
			aux.push_back(num[b]);
			b++;
			r = r + (mid - a);
		}
	}
	while(a<mid){
		aux.push_back(num[a]);
		a++;
	}

	while(b<hi){
		aux.push_back(num[b]);
		b++;
	}
	int j = low;
	for(int i=0; i<aux.size(); i++){
		if(j<hi){
			num[j] = aux[i];
			j++;
		}
	}
	return r;
}

int main(){
	int n;
	long long int s,ans;
	cin >> n;
	while(n != 0){
		for(int i=0; i<n; i++){
			cin >> s;
			num.push_back(s);
		}
		ans = flip(0, n);
		cout << ans << endl;
		num.clear();
		cin >> n;
	}
}