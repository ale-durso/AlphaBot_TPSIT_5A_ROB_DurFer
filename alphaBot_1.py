from libreria import AlphaBot

bot = AlphaBot(speed=50)

try:
    while True:
        comando = input("Comando (w=avanti, s=indietro, a=sinistra, d=destra, x=stop, q=esci) + Invio: ").lower()

        if comando == 'w':
            bot.forward()
        elif comando == 's':
            bot.backward()
        elif comando == 'a':
            bot.left()
        elif comando == 'd':
            bot.right()
        elif comando == 'x':
            bot.stop()
        elif comando == 'q':
            break

except KeyboardInterrupt:
    pass
finally:
    bot.cleanup()