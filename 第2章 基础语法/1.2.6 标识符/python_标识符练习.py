# 规则1：内容限定， 限制只能使用中文、数字、英文、下划线(_)，注意不能以数字开头，不推荐使用中文作为标识符
# 示例(错误）
# 123_weijing = "weijing"（用了数字开头的标识符）
# weijing_! = "weijing"（标识符中含有感叹号"!"）

# 示例（正确）
name_zhangweijing = "weijing"
_name_weijing = "weijing"
_name_1 = "weijing"

# 规则2：大小写敏感
Zwj = "weijing"
zwj = "666"
print(Zwj)
print(zwj)

# 规格3：不可使用关键
# 示例（错误）
# class = "zwj"（使用了关键词class)
# def = 666（使用了关键词def）
# 119 = "zwj"(使用了关键词119)
Class = 666 # (大小写敏感，大写C的Class不会导致报错)