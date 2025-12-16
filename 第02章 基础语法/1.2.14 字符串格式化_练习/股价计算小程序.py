name = "味精集团"
stock_price = 13.19
stock_code = "003072"
stock_price_daily_growth_factor = 1.2
growth_days = 5
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
# 计算，经过growth_days天的增长后，股价达到了多少钱
# 使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数
print(f"{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f"% (stock_price_daily_growth_factor, growth_days, finally_stock_price))

