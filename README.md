# Microsoft Visual C++ Runtimes All-in-One Installer

Bu proje, Microsoft Visual C++ Runtimes'ı kolayca indirip kurmak için bir araçtır. Windows'un gerreksinim duyduğu tüm gerekli bileşenleri tek bir paket halinde sunar.

## Özellikler

- Tek tıkla tüm Microsoft Visual C++ Runtimes sürümlerini indirin ve kurun.
- Otomatik kurulum, sadece çalıştırın ve arkanıza yaslanın.

## İndir
- (Buraya tıklayarak)[https://github.com/barankrky/vcredist_installer/releases/latest] en son versiyonu indirebilirsiniz.

## Kaynak Kodu

1. Bu projeyi klonlayın veya indirin:
   ```bash
   git clone https://github.com/barankrky/vcredist_installer.git
   cd vcredist_installer
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Programı çalıştırın:
   ```bash
   python main.py
   ```

## Kullanım

Program çalıştığında, Microsoft Visual C++ Runtimes'ı indirmeye başlayacaktır. İlerleme çubuğu, indirme işleminin durumunu gösterecektir. İndirme tamamlandığında, gerekli bileşenler otomatik olarak kurulacaktır. Herhangi bir ek işlem gerektirmez.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasını kontrol edin.
