# Decorator Nedir?

<p>Decoratorlar, Python'da işlevleri (functions) veya sınıfları (classes) değiştirmek veya genişletmek için kullanılan işlevlerdir. Genellikle bir fonksiyonu sarmalayarak veya bir sınıfı sarmalayarak çalışırlar. Bu, bir işlevin veya sınıfın davranışını değiştirmek veya genişletmek için kodu değiştirmeden kullanmamızı sağlar.</p>

## PyTest ve Decoratorlar

<p>PyTest, Python dilinde yazılmış bir test çerçevesidir. Bu çerçeve, testlerinizi yazmamıza, organize etmemize ve çalıştırmamıza olanak tanır. PyTest, test fonksiyonlarına özel decoratorler sağlar. Bu decoratorler, testlerin davranışını değiştirmek veya yapılandırmak için kullanılır. Bazen decoratorle ilgili bilgiler daha geniş konuların altında yer alabilir. Örneğin, PyTest belgelerinde dekoratörlerle ilgili bilgiler, "test fixtures" veya "custom markers" ile ilgili bölümlerde de bulunabilir.</p>

### PyTest Decoratorleri:

1. **_@pytest.fixture:_**
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

2. **_@pytest.mark.parametrize:_**
<p>PyTest'in "@pytest.mark.parametrize" decoratoru, bir test fonksiyonunu aynı testi farklı parametrelerle çalıştırmak için kullanılır. Bu şekilde, aynı testin farklı senaryolarını tek bir test fonksiyonunda birleştirebiliriz.</p>

```
import pytest

@pytest.mark.parametrize(("input" , "expected"), [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected

```

3. **_@pytest.mark.timeout(seconds=N)_**
<p>Timeout, bir testin belirli bir sürede tamamlanmasını sağlamak için kullanılan bir özelliktir.</p>
<p>"@pytest.mark.timeout(seconds=N)" Bir testin en fazla N saniye içinde tamamlanmasını sağlar.</p>

```
import pytest

@pytest.mark.timeout(seconds=5)
def test_long_running_operation():
    # Uzun süren bir işlem
    assert True

```

    3.a. ***`real` Timeout:*** Bu, bir testin gerçek dünya zamanına göre ne kadar sürede tamamlanması gerektiğini belirtir. Yani, testin başlatılması ve sonlandırılması arasındaki toplam geçen zamanı ölçer.

    ```
    import pytest

    @pytest.mark.timeout(seconds=5)
    def test_real_timeout():
        # Bu testin 5 saniye içinde tamamlanması gerekir
        # Eğer 5 saniye içinde tamamlanmazsa, timeout hatası alınır
        assert True

    ```

    3.b.***`cpu` Timeout***: Bu, bir testin işlemci zamanına (CPU zamanına) göre ne kadar sürede tamamlanması gerektiğini belirtir. Yani, testin gerçek zamanı değil, işlemci tarafından kullanılan zamanı ölçer.


    ```
    import pytest

    @pytest.mark.timeout(seconds=5, method="cpu")
    def test_cpu_timeout():
        # Bu testin 5 saniye boyunca toplam CPU zamanı kullanması gerekir
        # Eğer 5 saniye içinde tamamlanmazsa, timeout hatası alınır
        assert True

    ```

Bu iki tür timeout, testlerin ne kadar sürede tamamlanması gerektiğini kontrol etmek için kullanılır. `real` timeout, genellikle bir testin belirli bir sürede gerçek dünya zamanına göre tamamlanmasını sağlamak için kullanılırken, `cpu` timeout, testin işlemci zamanına göre ne kadar sürede tamamlanması gerektiğini kontrol etmek için kullanılır.

4. **_@pytest.mark.skip:_**
<p>PyTest'in "@pytest.mark.skip" decoratoru, bir test fonksiyonunun atlanmasını sağlar. Belirli koşullar altında bir testin geçici olarak devre dışı bırakılması gerektiğinde kullanılabilir.</p>

```
import pytest

@pytest.mark.skip(reason="Bu test henüz uygulanmadı")
def test_unimplemented_feature():
    assert False

```

5. **_@pytest.mark.xfail:_**
<p>PyTest'in "@pytest.mark.xfail" decoratoru, bir testin bilerek başarısız olabileceğini belirtmek için kullanılır. Bu şekilde, testin başarısız olması beklenir ve test sonucu başarısız olarak işaretlenmez.</p>

```
import pytest

@pytest.mark.xfail(reason="Bu testin başarısız olması bekleniyor")
def test_something():
    assert False

```
