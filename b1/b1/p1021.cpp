#include <iostream>
#include <deque>
using namespace std;
deque<int> dq;

void calc1() {
	dq.pop_front();
}

void calc2() {
	int tmp = dq.front();
	dq.pop_front();
	dq.push_back(tmp);
}

void calc3() {
	int tmp = dq.back();
	dq.pop_back();
	dq.push_front(tmp);
}

int main() {
	int N, M;
	int locate[50];
	int sum = 0;

	cin >> N >> M;

	//deque 만들기
	for (int i = 1; i <= N; i++) {
		dq.push_back(i);
	}

	//뽑아내려는 수 위치 배열에 저장
	for (int i = 1; i <= M; i++) {
		cin >> locate[i];
	}

	for (int i = 1; i <= M; i++) {
		int loc = locate[i];
		int index = 0;
		for (int j = 0; j < dq.size(); ++j) {
			if (dq[j] == loc) {
				index = j;
				break;
			}
		}
		//왼쪽 길이 < 오른쪽 길이 
		if (index < dq.size() - index) {
			while (dq.front() != loc) {
				calc2();
				++sum;
			}
			calc1();
		}
		//왼쪽 길이 > 오른쪽 길이
		else {
			while (dq.front() != loc) {
				calc3();
				++sum;
			}
			calc1();
		}
	}


	//시간초과??
	/*for (int i = 1; i <= M; i++) {
		int loc = locate[i];
		int left = 0, right = 0;
		int j = 1;

		while (dq.front() != loc) {
			for (j = 1; j <= dq.size(); j++) {
				if (dq[j] == loc)
					break;
				else
					left++;
			}
			right = dq.size() - left;

			if (left < right) {
				calc2();
				sum++;
			}
		}
		calc1();
	}*/
	
	cout << sum;
}