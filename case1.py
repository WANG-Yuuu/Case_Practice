# Case 1: 计算投资组合的收益率
portfolio = {
'股票':5000,
'债券':3000,
'基金':2000
}

returns = {
'股票':0.08,
'债券':0.04,
'基金':0.02
}

end_values=[]
total_end_value=0

for asset in portfolio:
    initial_value = portfolio[asset]
    return_rate = returns[asset]
    end_value = initial_value * (1 + return_rate)  # 计算年末价值
    end_values.append(end_value)
    print(f"{asset}的年末价值：{end_value:.0f}元")

total_end_value = sum(end_values)
print(f"投资组合的总年末价值：{total_end_value:.0f}元")

