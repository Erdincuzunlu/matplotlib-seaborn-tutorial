##### Veri Görselleştirme : MATPLOTLIB SEARBORN

#### MATPLOTLIB ###

###### KATEGORİK DEĞİŞKEN VARSA : sütun grafik. countplot bar

#### sayısal değişken ise : iki istatistiksel grafik vardır. Histogram ve boxplot

### dipnot : python veri görselleştirme için çok uygun değildir .ama kullanılır.

### küçük çaplı ihtiyaçları görselleştirebiliyoruz.

#### Kategorik değişken görselleştirme
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar') ### *****
plt.show()



#### sayısal değişken görselleştirme.....

plt.hist(df["age"])
plt.show()


### kutu grafik

plt.boxplot(df["fare"])
plt.show()

#### istatistiksel olan grafiklerdir... Histogram ve kutu grafik...
# Hangi aralıklarda hangi frekanslar var bunları gösterir


#### Matlotlib'in Özellikleri


### plot özelliğiii### Veriyi görselleştirmek için kullanılır..

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y, 'o')
plt.show()

x = np.array([1, 8, 9, 10, 11, 13])
y = np.array([1, 3, 5, 6, 8, 12])

plt.plot(x, y, 'o')
plt.show()


### market

y = np.array([1, 3, 5, 6, 8, 12])

plt.plot(y, marker='*')
plt.show()


y = np.array([1, 3, 5, 6, 8, 12])
plt.plot(y, linestyle="dashdot", color='red')
plt.show()


plt.plot(x, marker='o')
plt.show()

markers = ["o", "s", "v", "^", "<", ">", "8", "x"]


### multiple Lines



x= np.array([1, 8, 9, 10, 11, 13])
y = np.array([1, 3, 5, 6, 8, 12])

plt.plot(x)
plt.plot(y)
plt.show()


##### LABELSSS ( etiketler )))

x = np.array([1, 8, 9, 10, 11, 13])
y = np.array([1, 3, 5, 6, 8, 12])

plt.plot(x, y)

import matplotlib.pyplot as plt

# x ve y verilerini tanımlayın
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Çizgi grafiği oluştur
plt.plot(x, y)

# Grafiği ekranda göster
plt.show()


#### Başlık

plt.title("Bu ana başlık")

### X eksenini isimlendirme

plt.xlabel("x ekseni isimlendirmesi")

plt.ylabel("y ekseni isimlendirmesi")

plt.grid()
plt.show()


#### Subplots..

x = np.array([80, 100, 110, 115, 120, 140, 155])
y = np.array([180, 200, 250, 315, 320, 340, 400])

plt.subplot(1, 2, 1)   # 1'e 2 lik grafiğin 1.sini ver .
plt.title("1")
plt.plot(x, y)
plt.show()

x = np.array([80, 100, 110, 115, 120, 140, 155])
y = np.array([180, 200, 250, 315, 320, 340, 400])
plt.subplot(1, 2, 2)  ### bu da 1'e 2 lil grafiğin 2sini ver
plt.title("2")
plt.plot(x, y)
plt.show()


x = np.random.randint(0, 250, 10)
y = np.random.randint(200, 400, 10)



### yaygın olabilecek seaborn modülleri

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

#### 2 adet kategorik değişkenlerimiz var....

#### kadın erkek sigara içiyor içmiyor string formatında olanlar...

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

#### kategorik değişkenleri görselleştirmek için countplot methodu kullanacağız

## searborn kütüphanesi ile sayısal değişkenleri görselleştirme

sns.boxplot(x=df["total_bill"])
plt.show()

#### pandas advance bölümünde kullanılır...

df["total_bill"].hist()
plt.show()