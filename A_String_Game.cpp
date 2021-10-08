#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int x[200005], lt, lp, lo, hi, mid;
string t, p;
char s[200005], ss[200005];

bool check(int m){
    memcpy(ss, s, sizeof(s));
    for(int i=0;i<m;i++) ss[x[i]] = ' ';
    int j = 0;
    for(int i=0;i<lp;i++,j++){
        while(j<lt && ss[j] != p[i]) j++;
        if(j==lt) return false;
    }
    return true;
}

int main(){
    cin >> t;
    cin >> p;
    lt = t.size();
    lp = p.size();
    for(int i=0;i<lt;i++) {
        s[i] = t[i];
        cin >> x[i];
        x[i]--;
    }

    lo = 0;
    hi = lt+1;
    while(lo<hi-1){
        mid = lo + (hi-lo)/2;
        if(check(mid)) lo = mid;
        else hi = mid;
    }
    cout << lo;
}