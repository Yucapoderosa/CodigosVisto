#Tema asincronia
import asyncio


async def MetodoA():
    print('inicioA')
    #conectarse a un BD y traer 5 millones
    await asyncio.sleep(30)
    print('finA')
    
async def MetodoB():
    print('inicioB')
    #conecion a un servicio externo y esto tiene una duracion de 10
    await asyncio.sleep(20)
    print('finB')
    
    
async def main():
    MetodoA() # 30
    MetodoB() # 20
    l = await asyncio.gather(MetodoA(),MetodoB()) #30
    
    
asyncio.run(main())