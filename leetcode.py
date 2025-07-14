'''
Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
From the first two customers in order, we collect two $5 bills.
Input: bills = [5,5,10,10,20]

Output: false
Explanation:
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
'''
from typing import List, Optional

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False

        fiveDollars = 0
        tenDollars = 0

        for x in bills:
            if x == 5:
                fiveDollars += 1

            elif x == 10:
                if fiveDollars > 0:
                    fiveDollars -= 1

                else:
                    return False

                tenDollars += 1
            else:
                if fiveDollars > 0 and tenDollars > 0:
                    fiveDollars -= 1
                    tenDollars -= 1

                elif fiveDollars > 2:
                    fiveDollars -= 3
                else:
                    return False
            print(fiveDollars, tenDollars)

        return True

mysol = Solution()
print(mysol.lemonadeChange([5, 5, 5, 10, 20]))
