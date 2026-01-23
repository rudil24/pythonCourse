#Gauss challenge
gauss_sum = 0
print("*** Gauss challenge ***")
print("Enter a natural number (an integer greater than 0), and I will calculate the sum of the first n natural numbers!")
n = int(input("Enter a number: "))
if n <= 0:
    print("Exiting. Next time, please enter a valid natural number greater than 0.")
    exit()
for i in range(1, n + 1):
    gauss_sum += i
print(f"The sum of the first {n} natural numbers is:", gauss_sum)
# Expected output: 5050