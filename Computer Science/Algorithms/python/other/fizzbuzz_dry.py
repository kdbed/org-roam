# no duplication

for i in range(1,101):
    ans = ''

    if not i%3:
        ans += 'Fizz'
    if not i%5:
        ans += 'Buzz'

    print(ans or i)
