# Bertrand's Postulate
 
### When n > 3, there will always be a prime number between n and 2n-2 as long as n is >= 4



from BP import Bertrand


b = Bertrand()

b_100 = b.bertrand_single(100, show_range=True)
>> 100 198

b.bertrand_range(100)
>>>
index num	length
0	4	1
1	5	1
2	6	1
3	7	1
4	8	2
...	...	...
91	95	18
92	96	18
93	97	18
94	98	19
95	99	19
