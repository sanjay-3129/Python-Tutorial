#while loop
i = 1
while i<=7:
   print(i)
   i = i + 1

print("Finished!")
print()

#break
i = 0
while 1==1:  #infinite loop
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")
print()

#Continue
i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")
