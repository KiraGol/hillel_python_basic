# 2. Написати програму яка форматуватиме номер телефону до єдиного вигляду.
#   На введення програма приймає рядок введеного телефонного номера, наприклад:
#   063-999-99-99 повертає (+38) 063 999-99-99
#   063 999-99-99 повертає (+38) 063 999-99-99
#   063-99999-99 повертає (+38) 063 999-99-99
#   +3806399-999-99 повертає (+38) 063 999-99-99
#   380639999999 повертає (+38) 063 999-99-99
#   Якщо щось не так із номером - пише 'Failed to recognize number'.
import re


telList = list(input("Enter your phone number: "))
newTelList = [ ''.join(filter(str.isdigit, telList))]
[print('(+38) {}-{}-{}-{}'.format(tel[2:5], tel[5:8], tel[8:10], tel[10:12]))
 for tel in newTelList]