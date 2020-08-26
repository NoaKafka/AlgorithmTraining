/*
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;


vector<vector<int>> cal(vector<vector<int>> map) {
	vector<vector<int>> ans = map;
	int cnt = 0;
	int n = map.size();
	int m = map[0].size();

	for (int i = 0; i < m; i++) {
		int t = 0;
		//button on
		for (int j = 0; j < n; j++) {
			if (map[j][i] == 0) {
				map[j][i] = 1;
			}
			else {
				map[j][i] = 0;
			}
		}

		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				if (map[j][k] == 0) {
					break;
				}
				if (k == m - 1) {
					t++;
				}
			}
		}

		if (cnt < t) {
			cnt = t;
			ans = map;
		}


		//roll-back
		for (int j = 0; j < n; j++) {
			if (map[j][i] == 0) {
				map[j][i] = 1;
			}
			else {
				map[j][i] = 0;
			}
		}
	}

	return ans;
}

int main() {

	vector<vector<int>> map;

	int n, m;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		vector<int> t;\
			string input;
		for (int j = 0; j < m; j++) {
			scanf("%s", &input);
			if (input[j] == '1') {
				map[i].push_back(1);
			}
			else {
				map[i].push_back(0);
			}
		}
	}

	int num;
	scanf("%d", &num);

	//0이 하나라도 있는 행을 최소화
	for (int i = 0; i < num; i++) {
		map = cal(map);
	}

	int t = 0;
	for (int j = 0; j < n; j++) {
		for (int k = 0; k < m; k++) {
			if (map[j][k] == 0) {
				continue;
			}
			if (k == m - 1) {
				t++;
			}
		}
	}

	printf("%d", t);

	return 0;
}
*/