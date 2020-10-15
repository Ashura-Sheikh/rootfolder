a = 500000000
b = 55465215
c = a * b + b
# Testing 0
print(c)
def main():
    while True:
        if a < b:
            print(str(b) + " " + "is greater")
            break
        elif a > b:
            print(str(a) + " " + "is greater")
            break
        else:
            print("test failed")
            break

main()
