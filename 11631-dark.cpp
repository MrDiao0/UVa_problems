//UVa: 11631 - Dark roads
#include <bits/stdc++.h>
#include <tuple>
#include <vector>
#include <iostream>
using namespace std;

class UnionFind{
private:
	vector<int> p,rank;
public:
	UnionFind(int N){
		rank.assign(N,0);
		p.assign(N,0);
		for(int i = 0;i < N;i++){
			p[i]  = i;
		}
	}
	int findset(int i){
		return (p[i] == i) ? i: (p[i] = findset(p[i]));
	}
	void unionSet(int i,int j){
		int x = findset(i),y = findset(j);
		if(x != y){
			if(rank[x]>rank[y]){
				p[y] = x;
			}
			else{
				p[x] = y;
				if(rank[x] == rank[y]){
					rank[y]++;
				}
			}
		}
	}
};

bool sortthird(const tuple<int,int,int>& a, const tuple<int,int,int>& b){
	return (get<2>(a) < get<2>(b));
}

int kruskal(vector<tuple<int,int,int> > G, int n){
	int ans = 0, i = 0;
	int u,v,d;
	sort(G.begin(),G.end(),sortthird);
	UnionFind uf(n);
	while(i != G.size()){
		u = get<0>(G[i]);
		v = get<1>(G[i]);
		d = get<2>(G[i]);
		if(uf.findset(u) != uf.findset(v)){
			ans += d;
			uf.unionSet(u,v);
		}
		i++;
	}
	return ans;
}

int main(){
	int n,m,u,v,w,cnt;
	cin >> n >> m;
	while(n+m>0){
		cnt = 0;
		vector<tuple<int,int,int> > G;
		for(int i=0;i<m;i++){
			cin >> u >> v >> w;
			cnt += w;
			G.push_back(make_tuple(u,v,w));
		}
		cout << cnt-kruskal(G,n) << endl;
		cin >> n >> m;
	}
}