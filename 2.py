a_rate = 7.00
b_rate = 8.55
c_rate = 7.78
d_rate = 4.24

# 人民币金额
rmb_amount = 10000

# 计算兑换后的金额
a_amount = rmb_amount / a_rate
b_amount = rmb_amount / b_rate
c_amount = rmb_amount / c_rate
d_amount = rmb_amount / d_rate

# 打印结果，保留整数
print(f"10000元人民币可以兑换 {int(a_amount)} 美元")
print(f"10000元人民币可以兑换 {int(b_amount)} 英镑")
print(f"10000元人民币可以兑换 {int(c_amount)} 欧元")
print(f"10000元人民币可以兑换 {int(d_amount)} 澳元")
