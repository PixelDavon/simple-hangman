# hangman

word = 'australia'  # change word

g = "_" * len(word)

while g != word:
  print(g)
  b = input('Input Guess: ')
  ng = ""
  for i in range(len(word)):
    if b == word[i]:
      ng += b
    else:
      ng += g[i]
  g = ng

print('congratz')  # win message
