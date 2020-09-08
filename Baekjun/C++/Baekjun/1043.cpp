/*
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

vector<int> v_know;
bool people[51] = { false };
vector<int> party[51];
int n, p_num, know;

void dfs(int target) {
	//find
	for (int i = 1; i <= p_num; i++) {
		bool check = false;
		for (int j = 0; j < party[i].size(); j++) {
			if (party[i][j] == target) {
				check = true;
				break;
			}
		}
		if (check) {
			for (int j = 0; j < party[i].size(); j++) {
				if (!people[party[i][j]]) {
					dfs(party[i][j]);
				}
			}
		}
	}

	return;
}



int main() {
	
	cin >> n >> p_num;
	cin >> know;

	for (int i = 0; i < know; i++) {
		int t; //진실을 아는 사람의 num
		cin >> t;
		v_know.push_back(t);
	}

	for (int i = 0; i < p_num; i++) {
		int n_invited;
		cin >> n_invited;
		for (int j = 0; j < n_invited; j++) {
			int t;
			cin >> t;
			party[i].push_back(t);
		}
	}

	for (int i = 0; i < v_know.size(); i++) {
		//find party
		int target = v_know[i];
		if (!people[target]) {
			dfs(target);
		}
	}
	
	int ans = 0;
	for (int i = 0; i < n; i++) {
		if (people[i]) {
			ans++;
		}
	}

	cout << ans << endl;

	return 0;
}
*/