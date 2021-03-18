#include <iostream>
using namespace std;
#define MAX_SIZE 1001

int main() {
	int N, K;
	int data[MAX_SIZE];
	int index = 0;

	cin >> N >> K;

	for (int i = 1; i <= N; i++) {
		data[i] = i;
	}

	cout << "<";
	while (N > 0) {
		index = (index + K) % N;
		if (index == 0) index = N;

		//순열의 마지막 원소
		if (N == 1) {
			cout << data[1] << ">";
		}
		//나머지 경우
		else {
			cout << data[index] << ", ";
			//남은 원소들 한칸씩 앞으로
			for (int i = index; i < N; i++)
				data[i] = data[i + 1];
			index--;
		}
		N--;
	}
}