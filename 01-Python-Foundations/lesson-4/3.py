txt = input()
vowels = "aeiouAEIOU"
ans = ""
count = 0
skip = []

for i in range(len(txt)):
    ans += txt[i]
    count += 1

    if i == len(txt) - 1:  
        break

    if count >= 3: 
        if txt[i] in vowels or txt[i] in skip:
            continue
        else:
            skip.append(txt[i])
            ans += "_"
            count = 0

print(ans)
