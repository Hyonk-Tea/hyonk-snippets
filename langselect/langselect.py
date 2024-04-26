print('first: select language (først, plukke ut språk)')
print('[e]nglish / [n]orsk')

lang = str(input()) # this is the logic for languages
if lang == 'E' or lang == 'e':
  lines = open('english.txt').readlines()
elif lang == 'N' or lang == 'n':
  lines = open('norsk.txt').readlines()
else:
    print('you did not put a valid language!')
    exit()
print(lines[0])
