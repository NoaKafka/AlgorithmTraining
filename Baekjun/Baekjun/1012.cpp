/*
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int Map[51][51] = {0,};
int ans = 2;
void dfs(int i, int j) {
	//╩С
	if (i-1 >= 0) {
		if (Map[i - 1][j] == 1) {
			Map[i - 1][j] = ans;
			dfs(i - 1, j);
		}
	}
	//го
	if (i+1 <= 50) {
		if (Map[i+1][j] == 1) {
			Map[i + 1][j] = ans;
			dfs(i + 1, j);
		}
	}
	//аб
	if (j - 1 >= 0) {
		if (Map[i][j - 1] == 1) {
			Map[i][j - 1] = ans;
			dfs(i, j - 1);
		}
	}
	//©Л
	if (j + 1 <= 50) {
		if (Map[i][j + 1] == 1) {
			Map[i][j + 1] = ans;
			dfs(i, j + 1);
		}
	}
	return;
}




int main() {

	int n;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		int row, col, time;
		cin >> col >> row >> time;
		
		for (int j = 0; j < time; j++) {
			int r, c;
			cin >> r >> c;
			Map[c][r] = 1;
		}
		

		for (int j = 0; j < col; j++) {
			for (int k = 0; k < row; k++) {
				if (Map[k][j] == 1) {
					dfs(k, j);
					ans++;
				}
			}
		}
		cout << ans - 2 << endl;
		ans = 2;
		memset(Map, 0, sizeof(Map));
	}
	return 0;
}
*/