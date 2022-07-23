names = []

new_name = ''

while new_name != 'quit':
  new_name = input("Please tell me someone I should know, or enter 'quit': ")

  names.append(new_name)

print(names)