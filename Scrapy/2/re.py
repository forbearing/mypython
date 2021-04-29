#!/bin/env python3

# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo', content)
# print(result)
# print(result.group())
# print(result.span())

# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
# print(result)
# print(result.group(1))
# print(result.span())

# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result.group(1))

# import re
# content = 'price is $5.00'
# result = re.match('price is \$5\.00', content)
# #result = re.match('price is $5.00', content)
# print(result.string)



import re
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Stings'
# content = re.sub('\d+', '', content)
# print(content)
# content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Stings'
# content = re.sub('\d+', 'wokao', content)
# print(content)

content = re.sub('(\d+)', r'\1 890', content)
print(content)
