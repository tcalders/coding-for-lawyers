# Ask birthyear 	hint: a number is “int”  y=int(input(…
#
# Categorize into:
# The Baby Boomer Generation – born 1946-1964.
# Generation X – born 1965-1979.
# Millennials – born 1980-1994.
# Generation Z – born 1995-2012.
# Gen Alpha – born 2013 – 2025.
#
# Print the generation someone born in that year belongs to

birthyear = int(input("Give your birthyear : "))

if birthyear >= 1946 and birthyear <= 1964:
  print("Hello boomer")
elif birthyear>=1965 and birthyear <= 1979:
  print("Hello genX")
elif birthyear>=1980 and birthyear <= 1994:
  print("Hello millenial")
elif birthyear>=1995 and birthyear <= 2012:
  print("hello genZ")
elif birthyear>=2013 and birthyear <= 2025:
  print("hello genAlpha")
else:
  print("hello there")