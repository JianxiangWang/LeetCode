#!/usr/bin/env python
#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
public int countPrimes(int n) {
   boolean[] isPrime = new boolean[n];
   for (int i = 2; i < n; i++) {
      isPrime[i] = true;
   }
   // Loop's ending condition is i * i < n instead of i < sqrt(n)
   // to avoid repeatedly calling an expensive function sqrt().
   for (int i = 2; i * i < n; i++) {
      if (!isPrime[i]) continue;
      for (int j = i * i; j < n; j += i) {
         isPrime[j] = false;
      }
   }
   int count = 0;
   for (int i = 2; i < n; i++) {
      if (isPrime[i]) count++;
   }
   return count;
}

'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 0

        isPrime = [True] * (n+1)
        isPrime[0], isPrime[1] = False, False

        for i in range(2, n):
            if i * i > n:
                break

            if isPrime[i] == False:
                continue

            j = i*i
            while j <= n:
                isPrime[j]=False
                j+=i

        # count
        c = 0
        for i in range(n):
            if isPrime[i]:
                c += 1
        return c



if __name__ == '__main__':
    print Solution().countPrimes(10)





