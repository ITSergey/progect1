def F(curr, end):
    if curr > end or curr == 29: return 0
    if curr == end: return 1
    if curr < end: return F(curr+1, end) + F(curr*2, end) + F(curr*3, end)
print(F(2, 13) * F(13, 44))


#or curr == 22
# + F(curr+3, end)
