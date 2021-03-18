#include <iostream>
#include <string>
#include <stack>

using namespace std;
int num = 0;
string ps;

void checkVPS() {
	stack<char> s;
	//괄호 문자열 입력받기
	cin >> ps;

	for (int i = 0; i < ps.length(); i++) {
		if (ps[i] == '(')
			s.push(ps[i]);
		else {
			if (!s.empty()) {
				if (s.top() == '(')
					s.pop();
			}
			else {
				s.push(ps[i]);
				break;
			}
		}
	}

	if (s.size() == 0) {
		cout << "YES" << endl;
	}
	else {
		cout << "NO" << endl;
	}
}
int main() {

	//입력 데이터의 수
	cin >> num;
	for (int i = 0; i < num; i++) {
		checkVPS();
	}
}
