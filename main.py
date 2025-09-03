from impostazioni import *

cartina = Mappa([
    ["*", "S", "S", "U", "A"],
    ["A", "C", "A", "A", "A"],
    ["A", "S", "S", "S", "A"],
    ["S", "S", "A", "S", "A"],
    ["A", "A", "S", "I", "A"]
])

partita = Gioco([4, 3], [0, 3])
partenza = partita.inizio
fine = partita.fine
nomepl1 = str(input('Benvenuto, inserisci il tuo nome\n'))
player1 = Giocatore(nomepl1, partenza, 3, '')
cespuglio1 = Elementi('cespuglio', True, [1, 1])  # cespuglio ricresce non muore per ora lascio così
print('Ottimo', nomepl1, 'Dovrai riusciure ad uscire dal bosco, Per orientarti usa la cartina che vedi qui sotto, A sono gli alberi, S il sentiero, I inizio e U uscita\n')
cartina.stampa()
print(
    '\n Per guardati attorno ti basterà scrivere guarda, e per muoverti usa i punti cardinali precduti da # (#nord, #sud, #ovest ed #est)\n')
print(
    'ad esempio digita vai a #nord per muoverti di una posizione verso nord ecc..se ti trovi nei cespugli usa il comando usa ascia per liberarti\n')
print('Spero di averti detto tutto..ah si usa comando mappa se non sai dove sei..in bocca al lupo e partiamo\n')
comando = 'inizio'

while comando != 'end':

    comando = str(input(''))
    if 'mappa' in comando:  # se scrivo usa la mappa o guarda la mappa comunque funziona
        cartina.stampa()
    elif 'guarda' in comando:
        player1.guarda()
    elif '#nord' in comando:  # tengo il cancelletto perchè est è contenuto in ovest
        player1.direzione = 'nord'
        player1.muovi()
    elif '#sud' in comando:
        player1.direzione = 'sud'
        player1.muovi()
    elif '#est' in comando:
        player1.direzione = 'est'
        player1.muovi()
    elif '#ovest' in comando:
        player1.direzione = 'ovest'
        player1.muovi()
    elif 'ascia' in comando:
        cespugli = []
        player1.abbatti()
    if player1.vita <= 0:
        print('Hai perso tutte le vite e sei morto')
        comando = 'end'
    if player1.posizione == fine:
        print('Congratulazioni sei uscito dal bosco')
        comando = 'end'

    # print(player1.posizione)
    # print (fine)
