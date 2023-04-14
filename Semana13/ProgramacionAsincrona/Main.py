# Tema asincronia
import asyncio
import random


async def MetodoA():
    print('inicioA')
    # conectarse a un BD y traer 5 millones
    await asyncio.sleep(30)
    print('finA')


async def MetodoB():
    print('inicioB')
    # conecion a un servicio externo y esto tiene una duracion de 20
    await asyncio.sleep(20)
    print('finB')


async def ImprimirNumerosAleatorios():
    for i in range(1000):
        print(random.randint(1, 10))
        await asyncio.sleep(0)


async def main():
    tareaA = MetodoA()  # 30
    tareaB = MetodoB()  # 20
    tareaC = ImprimirNumerosAleatorios()
    await asyncio.gather(tareaA, tareaB, tareaC)


asyncio.run(main())
