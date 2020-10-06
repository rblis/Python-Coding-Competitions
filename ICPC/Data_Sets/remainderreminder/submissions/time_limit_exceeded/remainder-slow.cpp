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

//  cout << x1 << " " << x2 << endl;

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

int main(){
 

   long long a, b,c,d,e,f,g;
  cin >> a >> b >> c >> d >> e >> f >> g;
  vector<long long> best_volumes;
  Find_Best_Volumes(a,b, best_volumes);
 // for(long long i = 0; i < best_volumes.size(); i++)
  //  cout << best_volumes[i] << endl;

  int best = -1;
  for(int i = f; i <=g; i++){
    if(i%best_volumes[0] == c  &&
       i%best_volumes[1] == d &&
       i%best_volumes[2] == e){
      if(best != -1){
	cout << "Error- solutions of " << best << " and " << i << endl;
      }
      best = i;
    }
  }
  cout << best << endl;
  return 0;
}
      
