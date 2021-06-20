#include <iostream>
using namespace std;

int main() {
	long long t;
	cin >> t;

	for(int i=0; i < t; i++) {
	  long long n;
	  cin >> n;
	  int turn = 0;
	  long long total = 0;
	  while(n>0) {
		if(n%2==0 && (n%4==2 or n==4)) {
		  if (turn == 0) {
			total += n/2;
		  }
		  n -= n/2;
		} else {
		  if (turn == 0) {
			total++;
		  }
		  n--;
		}
		turn = 1 - turn;
	  }
	  cout << total << endl;
	}
}
