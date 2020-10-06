#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;

long long gcd(long long a, long long b, long long &s, long long &t)
{
    long long s0=1, s1=0;
    long long t0=0, t1=1;
    while (b != 0) {
        long long q = a/b;
        long long tmp = a%b;
        a = b;
        b = tmp;
        tmp = s0 - q*s1;
        s0 = s1;
        s1 = tmp;
        tmp = t0 - q*t1;
        t0 = t1;
        t1 = tmp;
    }
    s = s0;
    t = t0;
    return a;
}


void calcThreeLargest(long long x, long long y, long long m[])
{
    long long maxVal = (x + y - sqrt(x*x+y*y-x*y))/6.0;
    m[0] = 0;
    for(long long val = maxVal-2; val <= maxVal+2; val++) {
        long long vol = ((4*val - 2*(x+y))*val + x*y)*val;
        if (vol > m[0]) {
            m[2] = m[1];
            m[1] = m[0];
            m[0] = vol;
        }
        else if (vol == m[0])
            continue;
        else if (vol > m[1]) {
            m[2] = m[1];
            m[1] = vol;
        }
        else if (vol == m[1])
            continue;
        else if (vol > m[2])
            m[2] = vol;
    }
}

void solve(long long a[], long long m[], int n, long long &x, long long &mod)
/*
 * solve system of modular equations x = a[i] mod m[i], 1<=i<=n, using strong chinese remainder theorem
 * adapted from code at https://forthright48.com/chinese-remainder-theorem-part-2-non-coprime-moduli/
 *
 * solution is any y = x % mod
 */
{
    long long s, t;
    long long a1 = a[0];
    long long m1 = m[0];
    for ( int i = 1; i < n; i++ ) {
        int a2 = a[i];
        int m2 = m[i];

        long long g =gcd(m1, m2, s, t);
        if ( a1 % g != a2 % g ) {  // should never happen
            cout << "ERROR: unsolvable set of equations" << endl;
            x = mod = -1;
            return;
        }

        gcd(m1/g, m2/g, s, t);

        mod = m1 / g * m2;

        long long x = (a1*(m2/g)*t + a2*(m1/g)*s) % mod;

        a1 = x;
        if (a1 < 0) a1 += mod;
        m1 = mod;
    }
    x = a1;
}

int main()
{
    long long x, y, low, high;
    long long a[3], m[3];
    long long s, t;
    long long ans, mod;

    cin >> x >> y >> a[0] >> a[1] >> a[2] >> low >> high;
    calcThreeLargest(x, y, m);
    solve(a, m, 3, ans, mod);
    while (ans < low) {
        ans += mod;
    }
    cout << ans << endl;
    if (ans > high)
        cout << "ERROR: answer out of range" << endl;
    if (ans + mod <= high)
        cout << "ERROR: second solution = " << ans+mod << endl;
}
