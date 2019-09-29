//UVa: 11624 - Fire!
#include <deque>
#include <tuple>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int deltar[4] = {-1,0,0,1};
int deltac[4] = {0,-1,1,0};

int bfs(vector<vector<int> > maze, deque<tuple<int,int> > fire, int src[2]){
	deque<tuple<int,int,int> > queue,auxq;
	deque<tuple<int,int> > auxfq; 
	tuple<int,int,int> aux;
	tuple<int,int> auxf;
	int r,c,dr,dc;
	int dist = 0;

	queue.push_back(make_tuple(src[0],src[1],0));

	while(queue.size()>0){
		aux = queue.front();
		queue.pop_front();
		r = get<0>(aux);
		c = get<1>(aux);
		dist = get<2>(aux);
		if(maze[r][c] != 2){
			for(int u=0;u<4;u++){
				dr = r + deltar[u];
				dc = c + deltac[u];
				if(dr==maze.size() || dr<0 || dc==maze[0].size() || dc<0){
					return dist + 1;
				}
				else if(maze[dr][dc] == 0){
					maze[dr][dc] = 1;
					auxq.push_back(make_tuple(dr,dc,dist+1));
				}
			}
		}
		if(queue.size() == 0 && auxq.size() > 0){
			queue.swap(auxq);
			auxq.clear();

			while(fire.size()>0){
				auxf = fire.front();
				fire.pop_front();

				r = get<0>(auxf);
				c = get<1>(auxf);
				for(int u=0;u<4;u++){
					dr = r + deltar[u];
					dc = c + deltac[u];
					if(dr<maze.size() && dc<maze[0].size()){
						if(maze[dr][dc] != 2){
							maze[dr][dc] = 2;
							auxfq.push_back(make_tuple(dr,dc));
						}
					}
				}	
			}
			fire.swap(auxfq);
			auxfq.clear();
		}
	}
	return -1;
}

int main(){
	int cases,ans,R,C;
	string line;
	cin >> cases;
	while(cases>0){
		vector<vector<int> > maze;
		cin >> R >> C;
		int src[2] = { };
		deque<tuple<int,int> > fire;
		vector<int> tmp;

		for(int i=0; i<R; i++){
			cin >> line;
			maze.push_back(tmp);
			for(int j=0; j<C; j++){
				switch(line[j]){
				case '.':
					maze[i].push_back(0);
					break;
				case '#':
					maze[i].push_back(2);
					break;
				case 'F':
					maze[i].push_back(2);
					fire.push_back(make_tuple(i,j));
					break;
				case 'J':
					maze[i].push_back(1);
					src[0] = i; src[1] = j;
					break;
				}
			}
		}
		
		ans = bfs(maze, fire, src);
		if(ans == -1){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout << ans << endl;
		}
		cases--;
	}
}