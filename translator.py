def translate(spider):
  translation = " "
  for letter in spider:
    if letter in "aeiouAEIOU":
      translation = translation + "g"
    else:
      translation = translation + letter
  return translation

print(translate(input("plx enter  :")))
