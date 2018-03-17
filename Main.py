from Vector import Vector

class Main:


    if __name__ == "__main__":
        vet1 = Vector([1.33, 2.44, 3.55])        
        vet2 = Vector([4.66, 5.77, -1.22])
        vet3 = Vector([1.33, 2.44, 3.55])

        print(vet1)
        print(vet1 == vet2)
        print(vet1 == vet3)

        vetAdd = vet1.add(vet2)
        vetSub = vet1.subtract(vet2)
        vetMult = vet1.scalar_multiply(vet2)

        print(' === Add, Sub and Scalar Mult ===')
        print(vetAdd)
        print(vetSub)
        print(vetMult)