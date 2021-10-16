#include <iostream>
using namespace std;

int main() {
    int t;
    int a;
    cin>>t;
    //hello 
    for(int y =0;y<t;y++){
        int n, s;
        scanf("%d %d",&n,&s);
        int sum = n*(n+1);
        sum = sum/2;
        int ans = -1;
        int curr = 0;
        int a;
        for(int i=n;i>0;i--){
            //cout<<curr<<" --- "<<sum<<endl;
            if(curr + sum - i == s){ ans = i;break;}
            sum -= i;
            curr += i;
        }
        cout<<ans<<endl;
        
    }
    // your code goes here
    return 0;
}
