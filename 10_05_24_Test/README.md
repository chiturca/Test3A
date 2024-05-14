# Decorator Nedir?
<p>Decoratorlar, Python'da işlevleri (functions) veya sınıfları (classes) değiştirmek veya genişletmek için kullanılan işlevlerdir. Genellikle bir fonksiyonu sarmalayarak veya bir sınıfı sarmalayarak çalışırlar. Bu, bir işlevin veya sınıfın davranışını değiştirmek veya genişletmek için kodu değiştirmeden kullanmamızı sağlar.</p>

## PyTest ve Decoratorlar
<p>PyTest, Python dilinde yazılmış bir test çerçevesidir. Bu çerçeve, testlerinizi yazmamıza, organize etmemize ve çalıştırmamıza olanak tanır. PyTest, test fonksiyonlarına özel decoratorler sağlar. Bu decoratorler, testlerin davranışını değiştirmek veya yapılandırmak için kullanılır. Bazen decoratorle ilgili bilgiler daha geniş konuların altında yer alabilir. Örneğin, PyTest belgelerinde dekoratörlerle ilgili bilgiler, "test fixtures" veya "custom markers" ile ilgili bölümlerde de bulunabilir.</p>

### PyTest Decoratorleri:
1. ***@pytest.fixture:***
<p>PyTest'in "@pytest.fixture" decoratoru, test fonksiyonlarına bağımlılıkları sağlamak için kullanılır. Örneğin, bir test fonksiyonunun bir veritabanı bağlantısına ihtiyacı varsa, bu decoratoru kullanarak veritabanı bağlantısını oluşturabilir ve test fonksiyonuna sağlayabiliriz.</p>

```
import pytest

@pytest.fixture
def database_connection():
    # Veritabanı bağlantısı oluşturulur
    return db_connection

def test_database_operation(database_connection):
    # Testler yapılır ve database_connection bağımlılığı kullanılır
    assert True
    
```
2. ***@pytest.mark.parametrize:***
<p>PyTest'in "@pytest.mark.parametrize" decoratoru, bir test fonksiyonunu aynı testi farklı parametrelerle çalıştırmak için kullanılır. Bu şekilde, aynı testin farklı senaryolarını tek bir test fonksiyonunda birleştirebiliriz.</p>

```
import pytest

@pytest.mark.parametrize(("input" , "expected"), [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected
    
```

3. ***@pytest.mark.skip:***
<p>PyTest'in "@pytest.mark.skip" decoratoru, bir test fonksiyonunun atlanmasını sağlar. Belirli koşullar altında bir testin geçici olarak devre dışı bırakılması gerektiğinde kullanılabilir.</p>

```
import pytest

@pytest.mark.skip(reason="Bu test henüz uygulanmadı")
def test_unimplemented_feature():
    assert False
    
```

4. ***@pytest.mark.xfail:***
<p>PyTest'in "@pytest.mark.xfail" decoratoru, bir testin bilerek başarısız olabileceğini belirtmek için kullanılır. Bu şekilde, testin başarısız olması beklenir ve test sonucu başarısız olarak işaretlenmez.</p>

```
import pytest

@pytest.mark.xfail(reason="Bu testin başarısız olması bekleniyor")
def test_something():
    assert False
    
```
