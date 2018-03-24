from Vector import Vector

class Main:


    if __name__ == "__main__":
        # vet1 = Vector([1.33, 2.44, 3.55])        
        # vet2 = Vector([4.66, 5.77, -1.22])
        # vet3 = Vector([1.33, 2.44, 3.55])

        # print(vet1)
        # print(vet1 == vet2)
        # print(vet1 == vet3)

        # vetAdd = vet1.add(vet2)
        # vetSub = vet1.subtract(vet2)
        # vetMult = vet1.scalar_multiply(vet2)

        # print(' === Add, Sub and Scalar Mult ===')
        # print(vetAdd)
        # print(vetSub)
        # print(vetMult)

        print(' === Magnitude and normalization ===')
        vetM1 = Vector([-0.221, 7.437])
        print('Magnitude of {} = {}'.format(vetM1, vetM1.magnitude()))
        vetM2 = Vector([8.813, -1.331, -6.247])
        print('Magnitude of {} = {}'.format(vetM2, vetM2.magnitude()))
        vetN1 = Vector([5.581, -2.136])
        print('Normalization of {} = {}'.format(vetN1, vetN1.normalize()))
        vetN2 = Vector([1.996, 3.108, -4.554])
        print('Normalization of {} = {}'.format(vetN2, vetN2.normalize()))