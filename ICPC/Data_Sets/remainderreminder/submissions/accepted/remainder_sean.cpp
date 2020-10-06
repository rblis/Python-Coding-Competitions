#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

long long Volume(long long a, long long b, long long x){
  return (a-2*x)*(b-2*x)*x;
}

void Sort(vector<long long>& v){
  for(long long i = 0; i < v.size(); i++){
    for(long long j = 0; j < v.size()-1; j++){
      if(v[j] < v[j+1]){
	long long temp = v[j];
	v[j] = v[j+1];
	v[j+1] = temp;
      }
    }
  }
}

void Find_Best_Volumes(long long a, long long b, vector<long long>& best_volumes){
  long long quad_a = 12;
  long long quad_b = 4*a+4*b;
  long long quad_c = a*b;

 
  
  long long x1 = (quad_b + sqrt(quad_b*quad_b-4*quad_a*quad_c))/(2*quad_a);
  long long x2 = (quad_b - sqrt(quad_b*quad_b-4*quad_a*quad_c))/(2*quad_a);

  // cout << x1 << " " << x2 << endl;

  long long x;
  if(Volume(a,b,x1) > Volume(a,b,x2))
    x = x1;
  else
    x = x2;

  best_volumes.resize(0);
  for(long long i = x-2; i <= x+2; i++)
    best_volumes.push_back(Volume(a,b,i));

  Sort(best_volumes);
  best_volumes.resize(3);
}


long long Euclid(long long a, long long b, long long& x, long long& y){
  if(a == 0){ // uh-oh
    x = 0;
    y = 1;
    return b;
  }
  long long x1,y1;
  long long gcd = Euclid(b%a, a, x1,y1);
  x = y1-(b/a)*x1;
  y = x1;
  return gcd;
}
  
  
// returns a value between low and high that is congruent to all 3 mods
long long Solve(long long rem1, long long rem2, long long rem3, long long low, long long high, const vector<long long>& mods){

  long long gcd,u,v;
  gcd = Euclid(mods[0], mods[1],u,v);

  if(rem1 % gcd != rem2 % gcd)
    cout << "NO SOLUTION EXISTS" << endl;

  long long p,q;
  long long temp = Euclid(mods[0]/gcd, mods[1]/gcd, p, q);

  long long x = rem1 * mods[1]/gcd * q;
  x = x + rem2 * mods[0]/gcd * p ;

  long long m = mods[0] * mods[1] / gcd;

  x = x % m;  // keep it small
  
  // so x solves the first 2 equations, and is a solution mod m.
  // now we need a solution for for x mod m and rem3 mod mods[2]

  gcd = Euclid(m, mods[2], u, v);
  if(x < 0)
    x = x + m;
  
  if(x % gcd != rem3 % gcd)
    cout << "NO SOLUTION EXISTS!" << endl;
  temp = Euclid(m/gcd, mods[2]/gcd, p, q);

  long long answer = x * mods[2] * q / gcd;
  answer = answer + rem3 * m * p / gcd;

  long long final_mod = m * mods[2] / gcd;

  answer = answer % final_mod; // keep it small
  while(answer > high)
    answer = answer - final_mod;

  while(answer < low)
    answer = answer + final_mod;

  return answer;
    
  
}
  
  
  
  
int main(){
  long long a, b,c,d,e,f,g;
  cin >> a >> b >> c >> d >> e >> f >> g;
  vector<long long> best_volumes;
  Find_Best_Volumes(a,b, best_volumes);
  // for(long long i = 0; i < best_volumes.size(); i++)
  // cout << best_volumes[i] << endl;

  long long x = Solve(c,d,e,f,g,best_volumes);
  cout << x << endl;
  return 0;
}
