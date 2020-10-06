// References:
// https://math.stackexchange.com/questions/1644677/
//   what-to-do-if-the-modulus-is-not-coprime-in-the-chinese-remainder-theorem/
//   1644717
// https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Remainder_BobR {
  public static Scanner in;
  public static long w,h,r1,r2,r3,lo,hi;
  public static long[] lgv; // the three largest volumes

  public static void main(String[] args) {
    in = new Scanner(System.in);
    w = in.nextLong();
    h = in.nextLong();
    r1 = in.nextLong();
    r2 = in.nextLong();
    r3 = in.nextLong();
    lo = in.nextLong();
    hi = in.nextLong();

    //for (int i = 0; i < 3; i++) System.out.print(lgv[i]+" ");
    //System.out.println();

    lgv = vols(w,h);
    long ans = crt(lgv);
    System.out.println(ans);
  }

  // Find x such that:
  //    x = r1 % a[0]
  //    x = r2 % a[1]
  //    x = r3 % a[2]
  //    lo <= x <= hi
  public static long crt(long[] a) {
    // round 1:
//System.out.printf("Resolving x = %d mod %d and x = %d mod %d\n",
//   r1,a[0],r2,a[1]);
    long[] gst = gcd(a[0],a[1]);
    long g = gst[0];
    long s = gst[1];
    long t = gst[2];
//System.out.printf("GCD(%d,%d) = %d; s = %d, t = %d\n",a[0],a[1],g,s,t);
//System.out.printf("%d*%d + %d*%d = %d\n",s,a[0],t,a[1],(s*a[0]+t*a[1]));
    long newa = a[0]/g*a[1];
    long newr = r1 - s*(r1-r2)/g*a[0];
    long check = r2 + t*(r1-r2)/g*a[1];
    if (newr != check) {
       System.out.printf("Error in crt");
    }
    newr = newr % newa;
//System.out.printf("Resolves to x = %d mod %d, where %d is lcm(%d,%d)\n",
//    newr,newa,newa,a[0],a[1]);

    // round 2:
    gst = gcd(newa,a[2]);
    g = gst[0];
    s = gst[1];
    t = gst[2];
//System.out.printf("GCD(%d,%d) = %d; s = %d, t = %d\n",newa,a[2],g,s,t);
//System.out.printf("%d*%d + %d*%d = %d\n",s,newa,t,a[2],(s*newa+t*a[2]));
    long b = newa/g*a[2];
    long r4 = newr - s*(newr-r3)/g*newa;
    check = r3 + t*(newr-r3)/g*a[2];
    if (r4 != check) {
       System.out.printf("Error in crt");
    }
    r4 = r4 % b;
//System.out.printf("Resolves to x = %d mod %d, where %d is lcm(%d,%d)\n",
//    r4,b,b,newa,a[2]);

    // now just get within correct lo/hi range. We want k such that:
    // lo <= k*b + r4 <= hi
    long k = (hi-r4)/b;
    return k*b+r4;
  }

  public static long[] gcd(long a, long b) {
    if (b==0) return new long[]{a,1,0};
    long r0 = a, r1 = b;
    long s0 = 1, t0 = 0;
    long s1 = 0, t1 = 1;
    long q = a/b;
    while (r0 % r1 != 0) {
      long r2 = r0 % r1;
      long s2 = s0 - q*s1;
      long t2 = t0 - q*t1;
      r0 = r1; r1 = r2;
      s0 = s1; s1 = s2;
      t0 = t1; t1 = t2;
      q = r0/r1;
    }
    return new long[]{r1,s1,t1};
  }

  // Volume of a box of height x cut from a sheet of dimensions wxh
  public static long v(long x) {
    return x*(w - 2*x)*(h - 2*x);
  }

  // Find the three largest volumes of boxes, return as an array
  // of size 3 sorted from largest to smallest
  public static long[] vols(long w, long h) {
    // hand calculation: max volume occurs when corner cut, x, is
    // the solution to 12*x*x - 4*(w+h)*x + w*h = 0.
    double a = 12, b = -4*(w+h), c= w*h;
    double x = (-b - Math.sqrt(b*b-4*a*c))/2./a;

    // three largest INTEGER volumes are all clustered around x*(w-2x)*(h-2x)
    int s = (int)Math.floor(x) - 2;
    while (s <= 0)  s++; // just in case floor(x) is <= 2
    Long v[] = new Long[7];
    Arrays.fill(v,0L);
    for (int i = 0; i < 7; i++) {
      if (2*(s+i) >= w || 2*(s+i) >= h) break;
      v[i] = v(s+i);
    }
//    System.out.println();
    Arrays.sort(v,Collections.reverseOrder());

    long ans[] = new long[3];
    int i = 0;
    while (v[i] <= 0) i++;
    int j = 0;
    long last = -1;
    while (j < 3) {
      while (v[i] == last) i++; // there might be duplicates???
      ans[j] = v[i];
      i++;
      last = ans[j];
      j++;
    }
    return ans;
  }
}
