# Flask Nedir?

Python ile yazılmış bir web microframework paketidir. Performanslı ve modern web yazılımları yapmanıza yardımcı olur.

## Kurulum

Flask'ın, `Werkzeug` ve `Jinja2` gibi bir çok pakete bağımlılığı vardır. Flask'ı çalıştırmak için bu gerekli paketlerin de sisteme kurulu olması gerekiyor. Tabi 
ki tüm paketleri elle kurmakla uğraşmayacağız, bunun için çeşitli kurulum yöntemlerini izleyeceğiz.

### Virtualenv

Birden fazla Python projesi geliştiriyor ve bu projelerde de paketlerin farklı versiyonlarını kullanıyorsanız, geliştirme sırasında en iyi tercihiniz 
`virtualenv` olacaktır. Python'un kendi versiyonları arasında da geçiş yapabileceğiniz `virtualenv` ile projeye özel gereksinimleri çok rahat bir şekilde 
belirtebilirsiniz. 

Mac OS X ve Linux dağıtımları için `virtualenv` kurulumunu şu şekilde yapabilirsiniz.

```bash
$ pip install virtualenv
```

Paket yöneticinizde bulunuyorsa dilerseniz o şekilde de kurulum yapabilirsiniz. Örneğin **Ubuntu** için:

```bash
$ apt-get install python-virtualenv
```

Virtualenv'i kullanabilmek için öncelikle kendinize sanal ortam için bir klasör oluşturmanız gerekiyor. Genellikle proje dizininde açtığınız `venv` klasörü 
tercih edilir.

```bash
$ mkdir projem
$ cd projem
$ virtualenv venv
```

Virtualenv tarafından oluşturulan sanal ortam `venv` klasörü içerisinde olacaktır. Bu sanal ortamı aktif hale getirmek için aşağıdaki komutu çalıştırmanız 
yeterli olur.

```bash
$ . venv/bin/activate
```

Artık bu adımdan sonra yükleyeceğiniz tüm paketler bu sanal ortam üzerinde kurulacaktır.

```bash
$ pip install Flask
```

Gerçek ortamınıza dönmek veya başka bir sanal ortama geçmek isterseniz, bu sanal ortamdan çıkmanız gerekiyor. Onun için de

```bash
$ deactivate
```

## Sistem Geneli

Flask'ı sistem geneline kurmak isterseniz (kesinlikle önermiyorum) `pip` ile kurulumunu gerçekleştirebilirsiniz.

```bash
$ pip install Flask
```

## Hello World

Flask'ı kullanmadan önce basit bir `hello world` uygulamasını deneyelim. Bunun için öncelikle `hello-world.py` isminde bir dosya oluşturalım ve içeriğini şu 
şekilde düzenleyelim.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'
```

Bu kodumuzu çalıştırmak için öncelikle Flask'ın hangi dosyayı kullanacağını ortam değişkeni olarak belirtelim.

```bash
$ export FLASK_APP=hello-world.py
```

Ardından Flask'a bu dosyayı çalıştırmasını söyleyelim.

```bash
$ flask run
 * Serving Flask app "hello-world"
 * Running on http://127.0.0.1:5000/ 
```

Kontrol etmek için [http://localhost:5000](http://localhost:5000) adresini 
deneyebiliriz.

## Neler Yaptık?

İlk olarak **Flask** sınıfını dahil ettik. Bu sınıftan oluşturduğumuz nesne 
bizim uygulamamız olacaktır.

Ardından bu sınıftan bir nesne oluşturduk. İlk belirlediğimiz 
parametre(`__name__`) bu uygulamanın modül veya paket ismiydi. Eğer tek 
modül olarak kullanıyorsanız `__name__` değerini vermeniz gerekiyor çünkü 
Flask, import edilen nesnenin uygulama mı yoksa bir paket mi olduğuna bu 
şekilde karar veriyor. Gerekli tema ve statik dosyalara bunlar üzerinden 
ulaşacaktır.

Bu işlemin ardından bir **rota** oluşturduk. Eğer URL belirtilen şemaya 
uyuyorsa bir sonraki fonksiyonu çalıştırmasını sağladık.

Fonksiyon içerisinde döndürülecek değeri hazırladık.

Artık **/** adresine gidildiğinde `hello_world` fonksiyonumuz devreye 
giriyor ve kullanıcıya `Hello, World!` sonucunu çıktı olarak veriyor.

## Rota

Modern web uygulamalarının hepsi güzel URL yapısına sahiptir. 
`/?module=haber&haberID=52` gibi bir adresi hem hatırlamak zordur hem de 
kullanıcılar tarafından kötü görülecektir. Bunun yerine `haber-52` veya 
`linux-yaz-kampi-basladi` gibi bir adrese sahip olmak çok daha iyi 
olacaktır.

Flask uygulamanız içinde adresi yakalayıp gerekli işlemi yapmak için 
`route()` dekoratörünü kullanacağız. Bunun bir örneğini **hello-world** 
uygulamasında gördük. Anasayfa için tanımlama yapmıştık. Aynı şekilde 
`/deneme` sayfası için de bir rota tanımlayabiliriz.

```python
@app.route('/deneme')
def denemeMetodu():
	return 'DENEME!'
```

Tabi ki hepsi için bu şekilde ayrı ayrı oluşturma yapmayacağız. Her haber 
için ayrı bir rota oluşturmak oldukça mantıksız olacaktır.

## Rota Değişkenleri

URL içerisinde ne geleceğini bilmediğiniz kısımlar için rota değişkenlerini 
kullanabilirsiniz. Örneğin `haber-52` için bizim `haber-` kısmı sabittir ve 
`52` değerine ihtiyacımız olacaktır. Bu adrese göre bizim rota değişkenimiz 
`52`'nin olduğu kısımdır. Buna göre rotamız şu şekilde olabilir.

```python
@app.route('/haber-<haberid>')
def haber_goster(haberid):
	return "Haber Detay" + haberid
```

Belirli veri türlerine çevirmek için başına veri türünü ekleyip araya `:` 
koyabilirsiniz. Bu veri otomatik olarak o veri türüne çevrilecektir.

```python
@app.route('/haber-<int:haberid>')
def haber_goster(haberid):
	return "Haber Detay" + str(haberid)
```


