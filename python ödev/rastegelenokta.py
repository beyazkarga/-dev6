import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KoordinatYonetici:
    def __init__(self, nokta_sayisi, dosya_adi):
        self.nokta_sayisi = nokta_sayisi
        self.dosya_adi = dosya_adi
        self.x_koordinatlar = None
        self.y_koordinatlar = None

    def koordinat_uret(self):
        self.x_koordinatlar = np.random.randint(0, 1001, self.nokta_sayisi)
        self.y_koordinatlar = np.random.randint(0, 1001, self.nokta_sayisi)

    def excel_kaydet(self):
        df = pd.DataFrame({'X': self.x_koordinatlar, 'Y': self.y_koordinatlar})
        df.to_excel(self.dosya_adi, index=False)

    def excel_yukle(self):
        df = pd.read_excel(self.dosya_adi)
        self.x_koordinatlar = df['X']
        self.y_koordinatlar = df['Y']

    def koordinatlari_gorsellestir(self, ızgara_boyutu):
        plt.figure(figsize=(10, 10))
        eksen_basina_ızgara_sayisi = 1000 // ızgara_boyutu
        renk_haritasi = plt.get_cmap('tab20')
        renkler = renk_haritasi.colors

        for i in range(eksen_basina_ızgara_sayisi):
            for j in range(eksen_basina_ızgara_sayisi):
                maske = (self.x_koordinatlar >= i * ızgara_boyutu) & (self.x_koordinatlar < (i + 1) * ızgara_boyutu) & (self.y_koordinatlar >= j * ızgara_boyutu) & (self.y_koordinatlar < (j + 1) * ızgara_boyutu)
                renk_indeksi = (i * eksen_basina_ızgara_sayisi + j) % len(renkler)
                plt.scatter(self.x_koordinatlar[maske], self.y_koordinatlar[maske], color=renkler[renk_indeksi], s=10, alpha=0.6)

        plt.xlim(0, 1000)
        plt.ylim(0, 1000)
        plt.xlabel('X Koordinatları')
        plt.ylabel('Y Koordinatları')
        plt.title(f'{ızgara_boyutu}x{ızgara_boyutu} Izgaralara Bölünmüş Rastgele Noktalar')
        plt.grid(True)
        plt.show()

# Kullanım
nokta_sayisi = 1000
dosya_adi = 'koordinatlar.xlsx'
ızgara_boyutu = 200  # 50, 100 veya 200 olarak değiştirilebilir

yonetici = KoordinatYonetici(nokta_sayisi, dosya_adi)
yonetici.koordinat_uret()
yonetici.excel_kaydet()
yonetici.excel_yukle()
yonetici.koordinatlari_gorsellestir(ızgara_boyutu)
