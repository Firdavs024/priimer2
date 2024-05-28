def isPalindrome(slovo):
    rev = ''.join(reversed(slovo))
    if (slovo == rev):
        return True
    return False
slovo = ("malams")
end = isPalindrome(slovo)
print(end)

nomber = int(input("Введите число "))
for item in range(1,11):
    print(f'{nomber} * {item} = {nomber * item}')