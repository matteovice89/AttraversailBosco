class Mappa:
    def __init__(self, mappa):
        self.mappa = mappa

    def stampa(self):
        for r in self.mappa:
            print(" ".join(r))


class Giocatore:
    def __init__(self, nome, posizione, vita, direzione):
        self.nome = nome
        self.posizione = posizione
        self.vita = vita

    def muovi(self):
        verticale = self.posizione[0]
        orizzontale = self.posizione[1]
        vn = verticale  # variabili di comodo per scontro albero
        on = orizzontale

        if cartina.mappa[verticale][orizzontale] == "C":
            print('Sei bloccato in un cespuglio devi usare un\'ascia')
        else:
            if self.direzione == 'nord':
                if self.posizione[0] == 0:
                    print('Sei sul confine non puoi avvanzare verso nord')
                else:
                    nord = self.posizione[0]
                    self.posizione[0] = nord - 1

            if self.direzione == 'sud':
                if self.posizione[0] == len(cartina.mappa) - 1:
                    print('Sei sul confine non puoi avvanzare verso sud')
                else:
                    sud = self.posizione[0]
                    self.posizione[0] = sud + 1

            if self.direzione == 'est':
                if self.posizione[1] == len(cartina.mappa) - 1:
                    print('Sei sul confine non puoi avvanzare verso est')
                else:
                    est = self.posizione[1]
                    self.posizione[1] = est + 1

            if self.direzione == 'ovest':
                if self.posizione[1] == 0:
                    print('Sei sul confine non puoi avvanzare verso ovest')
                else:
                    ovest = self.posizione[1]
                    self.posizione[1] = ovest - 1
                    # aggiorno le variabili verticale e orizzontale e controllo di non essere su un albero
        verticale = self.posizione[0]
        orizzontale = self.posizione[1]

        if cartina.mappa[verticale][orizzontale] == "A":
            self.posizione[0] = vn
            self.posizione[1] = on
            self.vita -= 1
            print('Hai sbattuto male contro un albero, hai perso una vita e ti rimangono ', self.vita, ' vite')

        # print(self.posizione) #serve per il debug

    def guarda(self):  # al posto di aggiornare la mappa in questa versione ci si guarda attorno e ci si orienta
        # print(self.posizione)
        verticale = self.posizione[0]
        orizzontale = self.posizione[1]
        # print(verticale)
        # print(orizzontale)
        try:
            nord = cartina.mappa[verticale - 1][orizzontale]
            print('a nord è presente', nord)
        except IndexError:
            print('A nord c\'è il confine')
        try:
            sud = cartina.mappa[verticale + 1][orizzontale]
            print('a sud è presente', sud)
        except IndexError:
            print('A sud c\'è il confine')
        try:
            est = cartina.mappa[verticale][orizzontale - 1]
            print('a est è presente', est)
        except IndexError:
            print('A est c\'è il confine')
        try:
            ovest = cartina.mappa[verticale][orizzontale + 1]
            print('a ovest è presente', ovest)
        except IndexError:
            print('A ovest c\'è il confine')

    def abbatti(self):  # usa l'ascia e abbatte cespugli, rovi ecc
        verticale = self.posizione[0]
        orizzontale = self.posizione[1]
        if cartina.mappa[verticale][orizzontale] != "C":
            print('Non ci sono rovi o cespugli da abbattere')
        else:
            cartina.mappa[verticale][orizzontale] = "S"
            print('Cespuglio abbattuto')


class Elementi:  # questa serve per ragruppare gli elementi come alberi cespugli e altro
    def __init__(self, genere, vivo, posizione):
        self.genere = genere
        self.vivo = vivo
        self.posizione = posizione


# attualmente non mi serve, ma se implemento mostri ecc è pronta

class Gioco:  # la classe non è essenziale ora ma se implemento nuove cose è già pronta
    def __init__(self, inizio, fine):
        self.inizio = inizio
        self.fine = fine
