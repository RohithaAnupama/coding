def count(a, b, m, n):
    if ((m == 0 and n == 0) or n == 0):
        return 1
    if (m == 0):
        return 0
    if (a[m - 1] == b):
        return (count(a, b, m - 1, n - 1) +
                count(a, b, m - 1, n))
    else:
        return count(a, b, m - 1, n)
a = "going to go to goa"
b = "go"
last=b[-1]
print(count(a, last, len(a),len(last)))
 
