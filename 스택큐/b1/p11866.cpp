#include <iostream>
#include <queue>
using namespace std;

//큐 이용
int main() {
	int N, K;
	queue<int> q;

	cin >> N >> K;

	//큐에 1부터 N까지 push
	for (int i = 1; i <= N; i++) {
		q.push(i);
	}
	cout << "<";
	
	//k번째 요소를 꺼낼 수 있게
	while (!q.empty()) {
		for (int i = 0; i < K - 1; i++) {
			q.push(q.front());
			q.pop();
		}

		cout << q.front();
		q.pop();

		//마지막이 아니면
		if (!q.empty()) {
			cout << ", ";
		}
	}

	cout << ">";
}