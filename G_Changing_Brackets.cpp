#include <iostream>
#include <cstring>
using namespace std;

int t, n, q, x, y;
string s;

int main(){
    cin >> t;
    while(t--){
        cin >> s;
        n = s.size();
        int b[n];
        memset(b, -1, sizeof(b));
        for(int i=0;i<n;i++){
            if(s[i] == '[' or s[i] == ']'){
                b[i] = i%2;
            }
        }
        int l0[n], l1[n];
        memset(l0, 0, sizeof(l0));
        memset(l1, 0, sizeof(l1));
        int c0=0, c1=0;
        for(int i=0;i<n;i++){
            if(b[i] == 0) c0++;
            else if(b[i] == 1) c1++;
            l0[i] = c0;
            l1[i] = c1;
        }
        cin >> q;
        while(q--){
            cin >> x >> y;
            if(x>1) cout << abs((l0[y-1]-l0[x-2]) - (l1[y-1]-l1[x-2])) << endl;
            else cout << abs(l0[y-1] - l1[y-1]) << endl;
        }
    }
}