#include <vector>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int map[51][51] = {0,};
int f_num[51] = { 0, };
int t_friend[51] = { 0, };
int n;

int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		
		string s;
		cin >> s;
		for (int j = i+1; j < n; j++) {
			if (s[j] == 'Y') {
				map[i][j] = 1;
				map[j][i] = 1;
				f_num[i]++;
				f_num[j]++;
			}
			else {
				map[i][j] = 0;
				map[j][i] = 0;
			}
		}
	}

	for (int i = 0; i < n; i++) {

		bool rvisited[51] = { 0, };
		bool visited[51] = {0,};
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 1) {
				visited[j] = true;
			}
		}
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 1 && visited[j]) {
				for (int k = 0; k < n; k++) {
					if (map[j][k] == 1 && map[i][k] == 0) {
						rvisited[i] = true;
					}
				}
			}
		}
		for (int j = 0; j < n; j++) {
			if (rvisited[j]) {
				t_friend[i]++;
			}
		}
		
	}

	int ans = 0;

	for (int i = 0; i < n; i++) {
		//cout << f_num[i] << " + " << t_friend[i] << endl;
		int sum = f_num[i] + t_friend[i];
		if (ans < sum) {
			ans = sum;
		}
	}
	cout << ans << endl;

	return 0;
}