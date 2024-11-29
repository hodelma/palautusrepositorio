KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kasvatuskoko = OLETUSKASVATUS if kasvatuskoko is None else kasvatuskoko
        self.kapasiteetti = KAPASITEETTI if kapasiteetti is None else kapasiteetti

        if self.kapasiteetti < 0 or self.kasvatuskoko < 0:
            raise ValueError("Väärä kapasiteetti")
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lukumaara = 0

    def _luo_lista(self, koko):
        return [0] * koko
    
    def kuuluu(self, numero):
        for indeksi in range(self.alkioiden_lukumaara):
            if numero == self.lukujono[indeksi]:
                return True
    
    def lisaa(self, numero):
        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = numero
            self.alkioiden_lukumaara += 1


        if not self.kuuluu(numero):
            self.lukujono[self.alkioiden_lukumaara] = numero
            self.alkioiden_lukumaara += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lukumaara >= len(self.lukujono):
                vanha_taulukko = self.lukujono
                self.lukujono = self._luo_lista(self.alkioiden_lukumaara + self.kasvatuskoko)
                for i in range(self.alkioiden_lukumaara):
                    self.lukujono[i] = vanha_taulukko[i]

    def poista(self, numero):
        alkion_indeksi = -1

        for indeksi in range(0, self.alkioiden_lukumaara):
            if numero == self.lukujono[indeksi]:
                alkion_indeksi = indeksi
                self.lukujono[alkion_indeksi] = 0
                break

        if alkion_indeksi != -1:
            for j in range(alkion_indeksi, self.alkioiden_lukumaara - 1):
                self.lukujono[j] = self.lukujono[j + 1]
            self.alkioiden_lukumaara -= 1

    def kopioi_lista(self, lista_a, lista_b):
        for indeksi in range(0, len(lista_a)):
            lista_b[indeksi] = lista_a[indeksi]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def alkiot_numeroiksi_lista(self):
        taulu = self._luo_lista(self.alkioiden_lukumaara)
        for indeksi in range(0, len(taulu)):
            taulu[indeksi] = self.lukujono[indeksi]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.alkiot_numeroiksi_lista()
        b_taulu = b.alkiot_numeroiksi_lista()

        for indeksi in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[indeksi])

        for indeksi in range(0, len(b_taulu)):
            joukko.lisaa(b_taulu[indeksi])

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.alkiot_numeroiksi_lista()
        b_taulu = b.alkiot_numeroiksi_lista()

        for indeksi in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[indeksi] == b_taulu[j]:
                    joukko.lisaa(b_taulu[j])
        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.alkiot_numeroiksi_lista()
        b_taulu = b.alkiot_numeroiksi_lista()

        for indeksi in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[indeksi])
        for indeksi in range(0, len(b_taulu)):
            joukko.poista(b_taulu[indeksi])
        return joukko

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        else:
            alkiot_tekstina = ", ".join(str(self.lukujono[i]) for i in range(self.alkioiden_lukumaara))
            return "{" + alkiot_tekstina + "}"
