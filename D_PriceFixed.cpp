#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
int main(){
    int n;
    long long a, b, needed=0;

    scanf("%d", &n);
    vector< pair<long long, long long> > v;
    for(int i = 0;i < n;i++){
        scanf("%lld %lld", &a, &b);
        needed += a;
        v.push_back(make_pair(b, a));
    }
    sort(v.begin(), v.end());

    long long items=0, total=0, buy;
    int i=0, j=n-1;

    while(items < needed){
        if(v[i].first <= items){
            buy = v[i].second;
            v[i].second = 0;
            items += buy;
            total += buy;
            i++;
        } else {
            if(v[j].second >= v[i].first - items){
                buy = v[i].first - items;
                v[j].second -= buy;
                items += buy;
                total += buy*2;
                if(v[j].second == 0){
                    j--;
                }
            } else {
                buy = v[j].second;
                v[j].second = 0;
                items += buy;
                total += buy*2;
                j--;
            }
        }
    }
    printf("%lld", total);
}