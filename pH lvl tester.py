ph_lvl = int(input('what is the pH level? (0-14)'))
if ph_lvl > 7:
  print('Basic')
elif ph_lvl < 7:
  print('Acidic')
else:
  print('Neutral')