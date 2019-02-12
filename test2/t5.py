
# 比较一下

# 1
for i in range(5):
    if i == 1:
        print('in for')
else:
    print('in else')

print('----------------------------------')
# 2
for i in range(5):
    if i == 1:
        print('in for')
        break
else:
    print('in else')

# 只有for循环正常退出时才会执行else语句（不是由break结束循环）。而当循环是由break语句中断时，else就不被执行
# 记住只有for正常退出时才能执行到else
# 如果不用else我们也能直接print，为什么还要学习for/else，因为我们有了break这种非正常退出条件啊，
# 设想一下，你在遍历一个序列，并限制了某个条件，满足条件了就退出for，如果都不满足，那么最后就raise一个Error，如果有满足，就不执行raise，
# 就可以在for，之后用else raise Error，有满足的条件就break，就不正常退出循环了就用到了else Error
