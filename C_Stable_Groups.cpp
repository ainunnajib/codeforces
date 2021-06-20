#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    long long n, k, x;
    cin >> n >> k >> x;

    long long l[n];
    for(int i = 0; i<n; ++i){
        cin >> l[i];
    }
    sort(l, l+n);

    vector<long long> gaps;
    for(int i = 1; i<n; ++i){
        if(l[i]-l[i-1] > x){
            gaps.push_back((l[i]-l[i-1]-1)/x);
        }
    }
    sort(gaps.begin(), gaps.end());
    long long ans = gaps.size()+1;
    for(int i=0;i<gaps.size();i++){
        if(k>=gaps[i]){
            k -= gaps[i];
            ans--;
        } else {
            break;
        }
    }
    cout << ans;
}