#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

class myfunc{
public:
	bool operator() (const vector<int>& p1 , const vector<int>& p2) const
	{	
		if (p1[0] > p2[0]){
			return true;
		}
		else{
			return false;
		}
	}
};

int dijkstra(vector<vector<int > > G,vector<int> posy,vector<int> posx){
	priority_queue< vector<int> , vector< vector<int> > , myfunc> pri;
	vector<int> sup(G[0].size(),100000000);
	vector<int> sup2(G[0].size(),0);
	vector< vector<int> > ans(G.size(),sup);
	vector< vector<int> > visited(G.size(),sup2);
	vector<int> temp,xd;
	ans[0][0] = G[0][0];
	xd.push_back(G[0][0]);
	xd.push_back(0);
	xd.push_back(0);
	pri.push(xd);
	
	while (pri.size()!= 0){
		temp = pri.top();
		pri.pop();
		if(visited[temp[1]][temp[2]] == 0){
			for( int i = 0; i < 4 ; i++){
				int vary = posy[i] + temp[1];
				int varx = posx[i] + temp[2];

				if(vary >= 0 and vary < G.size() and varx>= 0 and varx < G[0].size()){
					
					if(temp[0] + G[vary][varx] < ans[vary][varx]){
						xd.clear();	
						ans[vary][varx] = temp[0] + G[vary][varx];
						xd.push_back(ans[vary][varx]);
						xd.push_back(vary);
						xd.push_back(varx);
						pri.push(xd); 
					}
				}
			}
			visited[temp[1]][temp[2]] = 1;
		}
	}

	return ans[G.size()-1][G[0].size()-1];
}

int main(){
	int cases;
	cin >> cases;
	for(int i=0; i<cases; i++){
		int n,m,x,ans;
		cin >> n >> m;
		vector< vector<int> > G;
		vector<int> aux;
		for(int u=0; u<n; u++){
			G.push_back(aux);
			for(int v=0; v<m; v++){
				cin >> x;
				G[u].push_back(x);
			}
		}
		vector<int> posx;
		posx.push_back(-1); posx.push_back(0); posx.push_back(0); posx.push_back(1);
		vector<int> posy;
		posy.push_back(0); posy.push_back(-1); posy.push_back(1); posy.push_back(0);
		ans = dijkstra(G,posx,posy);
		cout << ans << endl;
	}
}