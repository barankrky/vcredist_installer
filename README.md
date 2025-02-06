# Microsoft Visual C++ Runtimes All-in-One Installer

Bu proje, Microsoft Visual C++ Runtimes'ı kolayca indirip kurmak için bir araçtır. Kullanıcıların ihtiyaç duyduğu tüm gerekli bileşenleri tek bir paket halinde sunar.

## Özellikler

- Tüm Microsoft Visual C++ Runtimes sürümlerini tek bir tıklama ile indirin ve kurun.
- İndirme işlemi sırasında ilerleme çubuğu ile kullanıcı geri bildirimi.
- Geçici dosyaların otomatik temizlenmesi.

## Gereksinimler

- Python 3.12 veya daha yeni bir sürüm.
- `requests` ve `tqdm` kütüphaneleri. (Gerekirse, `pip install requests tqdm` komutunu kullanarak yükleyebilirsiniz.)

## Kurulum

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
