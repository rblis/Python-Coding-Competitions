#include <iostream>

using namespace std;

void Bounds(int x, int low, int high){
  if(x < low)
    cout << "Error: " << x << " too low" << endl;
  if(x > high)
    cout << "Error: " << x << " too high " << endl;
}

int main(){
  int a,b,c,d,e,f,g;
  cin >> a >> b >> c >> d >> e >> f >> g;
  if(a > b){
    cout << "Error- a > b" << endl;
  }
  Bounds(a,7,100);
  Bounds(b,7,100);
  Bounds(c,1,1000000000);
  Bounds(d,1,1000000000);
  Bounds(e,1,1000000000);
  Bounds(f,1,1000000000);
  Bounds(g,1,1000000000);

  cout << "OK" << endl;

  return 42;
}
