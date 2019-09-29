//UVa: 12086 - Potentiometers
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class SegmentTree{
private:
	vector<int> tree,A;
	int n_list;
	int left(int p){ return (p << 1)+1; }
	int right(int p){ return  (p+1) << 1; }

	int build(int i, int low, int hi){
		if(low+1 == hi){ tree[i] = A[low]; }
		else{
			int mid = low+((hi-low)>>1);
			tree[i] = build(left(i),low,mid) + build(right(i),mid,hi);
		}
		return tree[i];
	}

	int suma(int i, int ilow, int ihi, int low, int hi){
		if(ihi<=low || hi<=ilow){ return 0; }
		else if(low<=ilow && ihi<=hi){ return tree[i]; }
		else if(ilow+1==ihi){return tree[i]; }
		else{
			int imid = ilow+((ihi-ilow)>>1);
			int il = left(i);
			int ir = right(i);
			return suma(il,ilow,imid,low,hi)+suma(ir,imid,ihi,low,hi);
		}
	}

	int update(int i,int low,int hi,int j,int x){
		int l,r;
		if(low+1==hi){ tree[i] = x; }
		else{
			int mid = low+((hi-low)>>1);
			int il = left(i);
			int ir = right(i);
			if(j<mid){
				l = update(il,low,mid,j,x);
				r = tree[ir];
			}
			else{
				l = tree[il];
				r = update(ir,mid,hi,j,x);
			}
			tree[i] = l+r;
		}
		return tree[i];
	}
public:
	SegmentTree(const vector<int> &_A){
		A = _A;
		n_list = (int)A.size();
		tree.assign(n_list<<2,0);
		build(0,0,n_list);
	}

	int suma(int lo, int hi){
		if(lo==hi){ return 0; }
		else{ return suma(0,0,n_list,lo,hi); }
	}

	void update(int j, int x){
		update(0,0,n_list,j,x);
	}
};

int main(){
	int n,m,x,y,cases = 1;
	vector<int> l;
	char t;
	cin >> n;
	for(int i=0;i<3;i++){
		if(n>0){
			while(n>0){
				cin >> m;
				l.push_back(m);
				n--;
			}
			SegmentTree ST(l);
			cout << "Case " << cases << ":" << endl;
			cin >> t;
			while(t!='E'){
				if(t=='M'){
					cin >> x >> y;
					cout << ST.suma(x-1,y) << endl;
				}
				else if(t=='S'){
					cin >> x >> y;
					ST.update(x-1,y);
				}
				cin >> t;
			}
			l.clear();
			cin >> t >> t;
			cases++;
		}
		cin >> n;
		if(n>0){ cout << endl; }
	}
}