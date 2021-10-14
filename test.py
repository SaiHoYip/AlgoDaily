def reverse_string(str1):

  stack = ''
  for a in str1:
    stack = a + stack 
  # stack = a + ''
  # stack = b + 'a'
  # stack = c + 'ab'
  str1 = stack
  return str1

print(reverse_string('abc'))
