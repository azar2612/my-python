def translate(spider):
  azar = " "
  for letter in spider:
    if letter in "aeiouAEIOU":
      azar = azar + "g"
    else:
      azar = azar + letter
  return azar

print(translate(input("plx enter  :")))