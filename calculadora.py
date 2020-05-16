import os
import time


class Calculadora:

    def __init__(self):
        self.__primeiro_valor = 0
        self.__segundo_valor = 0
        self.__opcao = -1

    def calcular(self):
        while(self.__opcao != 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("="*30)
            print("\tCalculadora Master")
            print("="*30)
            print("\n\n\n")
            print("[1] -> Somar")
            print("[2] -> Subtrair")
            print("[3] -> Multiplicar")
            print("[4] -> Dividir")
            print("[0] -> Sair")
            print("\n\n")
            self.__opcao = int(input("Digite a opcao desajada=> "))

            if(self.__opcao == 1):
                self.__somar()
            elif(self.__opcao == 2):
                self.__subtrair()
            elif(self.__opcao == 3):
                self.__multiplicar()
            elif(self.__opcao == 4):
                self.__dividir()
            else:
                print("Opcao invalida")
            time.sleep(2.4)
        if(self.__opcao == 0):
            print("\n\nObrigado por utilizar a calculadora.")

    def __inserir_numeros(self):
        self.__primeiro_valor = int(input("Digite o primeiro valor: "))
        self.__segundo_valor = int(input("Digite o segundo valor: "))

    def __somar(self):
        self.__inserir_numeros()
        print('{} + {} = {}'.format(self.__primeiro_valor, self.__segundo_valor, self.__primeiro_valor + self.__segundo_valor))
        self.__opcao = int(input("[1] -> Deseja continuar | [0] para sair => "))

    def __subtrair(self):
        self.__inserir_numeros()
        print('{} - {} = {}'.format(self.__primeiro_valor, self.__segundo_valor, self.__primeiro_valor - self.__segundo_valor))
        self.__opcao = int(input("[1] -> Deseja continuar | [0] para sair => "))

    def __multiplicar(self):
        self.__inserir_numeros()
        print('{} * {} = {}'.format(self.__primeiro_valor, self.__segundo_valor, self.__primeiro_valor * self.__segundo_valor))
        self.__opcao = int(input("[1] -> Deseja continuar | [0] para sair => "))

    def __dividir(self):
        self.__inserir_numeros()
        print('{} / {} = {}'.format(self.__primeiro_valor, self.__segundo_valor, self.__primeiro_valor / self.__segundo_valor))
        self.__opcao = int(input("[1] -> Deseja continuar | [0] para sair => "))



calculadora = Calculadora();
calculadora.calcular();