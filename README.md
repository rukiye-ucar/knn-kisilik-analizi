# knn-kisilik-analizi
# KNN Kişilik Analizi Web Uygulaması
Bu proje Fatma Gizem Arı, Rabia Türkmen ve Rukiye Uçar tarafından hazırlanmıştır. 
Bu proje, kullanıcıdan alınan kişilik anketi cevaplarına göre **K-En Yakın Komşu (KNN)** algoritması kullanarak kişilik analizi yapan bir web uygulamasıdır.  
Proje, makine öğrenmesi modelinin web arayüzü ile birleştirilmesini amaçlamaktadır.

## Proje Amacı

Bu uygulamanın amacı, kullanıcıların belirli sorulara verdikleri cevaplardan yola çıkarak kişilik özelliklerini tahmin etmektir.  
Makine öğrenmesi tarafında **KNN algoritması**, web tarafında ise kullanıcı dostu bir arayüz kullanılmıştır.

Proje özellikle şu konuları göstermek için hazırlanmıştır:

- Makine öğrenmesi modelinin web uygulamasına entegre edilmesi
- Kullanıcıdan form verisi alma
- Alınan verileri Python ile işleme
- Eğitilmiş model ile tahmin yapma
- Sonucu web arayüzünde kullanıcıya gösterme

## Kullanılan Teknolojiler

Projede kullanılan temel teknolojiler şunlardır:

- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **HTML**
- **CSS**
- **JavaScript**
- **Pickle**
- **KNN Makine Öğrenmesi Algoritması**

## Kullanılan Algoritma: KNN

KNN, yani **K-Nearest Neighbors**, sınıflandırma problemlerinde kullanılan temel makine öğrenmesi algoritmalarından biridir.

Bu projede KNN algoritması, kullanıcının verdiği cevapları daha önce eğitilmiş verilerle karşılaştırarak en yakın kişilik sonucunu tahmin etmek için kullanılmıştır.

KNN algoritmasının temel mantığı:

1. Kullanıcıdan gelen cevaplar sayısal verilere dönüştürülür.
2. Bu veriler modelin anlayacağı formata getirilir.
3. Model, gelen veriye en yakın komşuları bulur.
4. En yakın sonuçlara göre kişilik tahmini yapılır.

## Proje Özellikleri

- Kullanıcı dostu kişilik analizi formu
- Web tabanlı arayüz
- Python Flask ile backend yapısı
- Eğitilmiş KNN modeli ile tahmin alma
- Kullanıcı cevaplarına göre kişilik sonucu gösterme
- HTML, CSS ve JavaScript ile hazırlanmış frontend
- Makine öğrenmesi modelinin web uygulamasına entegrasyonu

## Proje Yapısı

Örnek proje dosya yapısı aşağıdaki gibidir:

```text
knn-kisilik-analizi/
│
├── app.py
├── model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
Projenin eğitilmiş modeline buradan ulaşılabilir: https://drive.google.com/file/d/1MQxaEfjdZM-1IFVJ-CltGFkESGxkVixj/view?usp=sharing
