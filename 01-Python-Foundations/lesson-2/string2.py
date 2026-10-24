txt = "LMaasleitbtui"
str1, str2 = "", ""
for i in range(len(txt)):
    if i % 2 == 0:
        str1 += txt[i]
    else:
        str2 += txt[i]
print(str1, str2)