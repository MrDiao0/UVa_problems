//UVa: 12785 -Emacs Plugin
#include <vector>
#include <string>
#include <iostream>
using namespace std;

vector<int> computeFailure(string P){
	int m = P.length();
	vector<int> fail(m,-1);
	int j = 0;
	for(int i=1;i<m;i++){
		fail[i] = j;
		while(j>0 && P[i]!=P[j]){
			j = fail[j];
		}
		j++;
	}
	return fail;
}

int KMP(string T,string P){
	int ans = -1;
	int n = T.length();
	int m = P.length();
	int j = 1;
	vector<int> fail = computeFailure(P);
	for(int i=1;i<n;i++){
		while(j>0 && j<m && T[i]!=P[j]){
			j = fail[j];
		}
		if(j==m){
			ans = i-m+1;
		}
		j++;
	}
	return ans;
}

int main(){
	int i,j;
	bool ans;
	int cases;
	vector<string> subW;
	string word,sub,search;
	while(cin >> cases){
		cin >> word;
		while(cases > 0){
			j = 0;
			ans = true;
			cin >> sub;
			search = " ";
			for(int a=0;a<sub.length();a++){
				if(sub[a]!='*'){ search.push_back(sub[a]); }
				else{ subW.push_back(search); search = " "; }
			}
			if(search.length()>0){ subW.push_back(search); }
			
			for(int u=0;u<subW.size();u++){
				if(ans){
					i = j;
					j = KMP(" "+word.substr(i)+" ",subW[u]);
					if(j!=-1){ j += i+subW[u].length()-2; }
					else{ ans = false; }
				}
			}
			if(ans){ cout << "yes" << endl;}
			else{ cout << "no" << endl; }
			cases--;
			subW.clear();
		}
	}
}