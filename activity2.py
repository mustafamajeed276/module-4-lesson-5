s1 = {3, 2, 1}
s2 = {'c', 'b', 'a'}
s3 = list(zip(s1, s2))
print(s3, '\n')
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x ,y)
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]
newdict = {stocks : prices for stocks, prices in zip(stocks, prices)}
print('\n{}'.format(newdict))