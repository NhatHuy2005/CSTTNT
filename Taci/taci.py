import random

def generate_taci_file(filename):

    n = random.randint(3, 99)
    

    numbers = list(range(n * n))
    

    random.shuffle(numbers)
    
    with open(filename, 'w') as file:
        file.write(f"{n}\n")  
        for i in range(n):
            file.write(" ".join(map(str, numbers[i * n:(i + 1) * n])) + "\n")


generate_taci_file("taci1.txt")
generate_taci_file("taci2.txt")
generate_taci_file("taci3.txt")
print("Da tao file thanh cong!")