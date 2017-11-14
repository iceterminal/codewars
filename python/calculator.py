class Calculator(object):
  def evaluate(self, string):
    list = string.split()
    for i in range(len(list)):
        if list[i] == '*' or list[i] == '/':
            if list[i] == '*':
                number = float(list[i-1])*float(list[i+1])
            if list[i] == '/':
                number = float(list[i-1])/float(list[i+1])
            list[i-1] = '0'
            if list[i-2] == '-':
                list[i] = '-'
            else:
                list[i] = '+'
            list[i+1] = str(number)
    print(list)
    total = float(list[0])
    for i in range(1,len(list)):
        if list[i] == '+':
            total += float(list[i+1])
        if list[i] == '-':
            total -= float(list[i+1])
    return total


print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
# => 7
print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
# 8
