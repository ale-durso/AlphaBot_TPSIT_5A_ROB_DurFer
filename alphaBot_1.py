import curses  # Libreria standard di Python per gestire l'input da tastiera in tempo reale
from libreria import AlphaBot

bot = AlphaBot(speed=50)

stdscr = curses.initscr()    # initscr() trasforma la finestra del terminale per catturare direttamente la pressione dei tasti

while True:
    tasto = stdscr.getkey().lower()    # getkey() si blocca in attesa di un tasto e lo legge
    if tasto == 'w':
        bot.right()      
    elif tasto == 's':
        bot.left()     
    elif tasto == 'a':
        bot.forward()    
    elif tasto == 'd':
        bot.backward()  
    elif tasto == 'e':
        bot.stop()      
    elif tasto == 'q':
        break            

curses.endwin()    # riporta il terminale alla  modalità normale prima di uscire
bot.cleanup()    # Spegne motori e rilascia i PIN
