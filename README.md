The Set Cover Problem is an important problem in the fields of combinatorial optimization and computational complexity theory. This problem involves finding the smallest subset of sets that cover a given universal set. Specifically, given a collection of subsets of a universal set, the goal is to select the fewest possible subsets that together cover the entire universal set.

Definition of the Set Cover Problem
Universal Set (U): A set of elements that need to be covered.
Subsets (S): A collection of subsets that collectively cover the elements of the universal set.
Objective: To select the minimum number of subsets that cover all the elements in the universal set.

Formülasyon
Formel olarak, set cover problemi şu şekilde tanımlanabilir:


U bir evrensel küme olsun.

=
{
𝑆
1
,
𝑆
2
,
…
,
𝑆
𝑚
}
S={S 
1
​
 ,S 
2
​
 ,…,S 
m
​
 } alt kümeler koleksiyonu olsun, burada her 
𝑆
𝑖
⊆
𝑈
S 
i
​
 ⊆U.
Amaç, 
𝐶
⊆
𝑆
C⊆S olacak şekilde, 
𝐶
C'deki kümelerin birleşimi 
𝑈
U'yu kapsasın ve 
∣
𝐶
∣
∣C∣ minimum olsun.

Örnek
Bir örnekle açıklayalım:

Veri:

Evrensel Küme: 
𝑈
=
{
1
,
2
,
3
,
4
,
5
}
U={1,2,3,4,5}
Alt Kümeler: 
𝑆
=
{
𝑆
1
,
𝑆
2
,
𝑆
3
,
𝑆
4
}
S={S 
1
​
 ,S 
2
​
 ,S 
3
​
 ,S 
4
​
 }
𝑆
1
=
{
1
,
2
,
3
}
S 
1
​
 ={1,2,3}
𝑆
2
=
{
2
,
4
}
S 
2
​
 ={2,4}
𝑆
3
=
{
3
,
4
}
S 
3
​
 ={3,4}
𝑆
4
=
{
4
,
5
}
S 
4
​
 ={4,5}
Çözüm:

Alt kümelerden hangilerini seçmeliyiz ki tüm elemanları kapsayalım ve en az sayıda alt küme seçilmiş olsun?
Adım adım bakalım:

𝑆
1
S 
1
​
 'i seçersek: 
{
1
,
2
,
3
}
{1,2,3} kapsandı.
Geriye kalanlar: 
{
4
,
5
}
{4,5}
𝑆
4
S 
4
​
 'i seçersek: 
{
4
,
5
}
{4,5} kapsandı.
Bu durumda, 
𝑆
1
S 
1
​
  ve 
𝑆
4
S 
4
​
 'i seçerek tüm elemanları kapsayabiliriz. Yani, en az iki alt kümeyle evrensel kümedeki tüm elemanları kapsayabiliyoruz.

Başka bir çözüm yolu daha deneyelim:

𝑆
2
S 
2
​
 'yi seçersek: 
{
2
,
4
}
{2,4} kapsandı.
𝑆
3
S 
3
​
 'ü seçersek: 
{
3
,
4
}
{3,4} kapsandı. Ancak, 
4
4 zaten kapsandı.
Geriye kalanlar: 
{
1
,
3
,
5
}
{1,3,5}
Bu durumda 
𝑆
1
S 
1
​
 'i ve 
𝑆
4
S 
4
​
 'i seçerek yine aynı sonuca ulaşırız, yani 
{
1
,
2
,
3
,
4
,
5
}
{1,2,3,4,5}.
En İyi Çözüm:

𝑆
1
S 
1
​
  ve 
𝑆
4
S 
4
​
 'ü seçerek tüm elemanları kapsamak en az sayıda küme ile mümkündür.
NP-Tam Problemi
Set cover problemi, NP-tam (NP-complete) bir problem olarak sınıflandırılır. Bu, problemin çözümünün doğruluğunu kontrol etmenin kolay, ancak çözümünü bulmanın zor olduğu anlamına gelir. Büyük veri kümelerinde optimum çözüm bulmak hesaplama açısından oldukça zor olabilir. Bu nedenle, genellikle yaklaşık algoritmalar kullanılır.

Uygulama Alanları
Set cover probleminin uygulama alanları oldukça geniştir. Örneğin:

Ağ Tasarımı: Ağ düğümlerinin kapsanması.
Veri Madenciliği: Özellik seçimi.
Hizmet Yerleştirme: Minimum sayıda hizmet noktası ile tüm müşterilerin kapsanması.
Sonuç olarak, set cover problemi teorik olarak önemli olduğu kadar pratik uygulamalarda da yaygın olarak karşımıza çıkar.

################ KOD AÇIKLAMASI ###############

Evren ve Alt Kümelerin Oluşturulması

python
Kodu kopyala
import random
import itertools

def generate_universe_and_subsets(universe_size, num_subset, min_set_size, max_set_size):
    universe= set(range(1, universe_size+1))

    subsets = []
    remaining_elements = set(universe)

    while remaining_elements:
        set_size= random.randint(min_set_size, max_set_size)
        new_subset= set(random.sample(list(remaining_elements), min(set_size, len(remaining_elements))))
        subsets.append(new_subset)
        remaining_elements -= new_subset

    for _ in range(num_subset - len(subsets)):
        set_size = random.randint(min_set_size, max_set_size)
        new_subset = set(random.sample(list(universe), set_size))
        subsets.append(new_subset)

    return universe, subsets

universe, subsets = generate_universe_and_subsets(universe_size=80, num_subset=50, min_set_size=2, max_set_size=15)
generate_universe_and_subsets fonksiyonu, belirli bir boyutta evren kümesi ve alt kümeler oluşturur.
universe_size, evren kümesinin boyutunu belirler.
num_subset, kaç tane alt küme oluşturulacağını belirler.
min_set_size ve max_set_size, alt kümelerin minimum ve maksimum boyutlarını belirler.
İlk döngüde, remaining_elements (kapsanmamış elemanlar) boşalana kadar rastgele boyutta ve elemanlarda alt kümeler oluşturulur.
İkinci döngüde, yeterli sayıda alt küme oluşturulmadıysa rastgele alt kümeler eklenir.
Brute Force Set Cover

python
Kodu kopyala
def brute_force_set_cover(universe, sets):
    n = len(sets)

    for  i in range(1, n+1):
        for subset in itertools.combinations(sets, i):
            if set.union(*subset) == universe:
                return subset
brute_force_set_cover fonksiyonu, tüm alt küme kombinasyonlarını deneyerek evren kümesini kapsayan en küçük alt küme kombinasyonunu bulur.
itertools.combinations kullanarak alt kümelerin tüm olası kombinasyonlarını oluşturur.
Eğer bir kombinasyon evren kümesini tam olarak kapsıyorsa (yani birleşim evren kümesine eşitse), bu kombinasyon döndürülür.
Greedy Set Cover

python
Kodu kopyala
def greedy_set_cover(universe, sets):
    uncovered = universe.copy()
    solution = []

    while uncovered:
        best_set = max(sets, key=lambda s: len(s & uncovered))
        solution.append(best_set)
        uncovered -= best_set

    return solution
greedy_set_cover fonksiyonu, açgözlü bir yaklaşım kullanarak evren kümesini kapsayan alt kümeleri seçer.
uncovered kümesi, kapsanmamış elemanları takip eder.
Döngüde, sets içindeki alt kümelerden uncovered ile en çok ortak elemanı olan alt küme (best_set) seçilir.
Bu alt küme çözüme eklenir ve uncovered kümesinden bu alt kümenin elemanları çıkarılır.
Döngü, uncovered kümesi boşalana kadar devam eder.
Sonuçların Karşılaştırılması

python
Kodu kopyala
solution = greedy_set_cover(universe, subsets)
print(solution)
print(len(solution))

solution = brute_force_set_cover(universe, subsets)
print(solution)
print(len(solution))
greedy_set_cover fonksiyonu çağrılır ve sonucu yazdırılır.
brute_force_set_cover fonksiyonu çağrılır ve sonucu yazdırılır.
Her iki fonksiyonun sonucu ve seçilen alt kümelerin sayısı karşılaştırılır.


############### 
SONUÇ
###############

Kaba kuvvet yöntemiyle aldığımız çıktılar daha başarılı fakat çalışma süresi çok uzun.
greedy_set_cover yöntemi çok daha hızlı ama kabul edilebilir sonuçlar üretir.

Girdi: 
universe, subsets = generate_universe_and_subsets(universe_size=50, num_subset=30, min_set_size=2, max_set_size=15)

Çıktılar:
U= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}

S= 
{32, 34, 40, 10, 50, 19, 26, 28, 30}
{24, 27, 44, 46}
{33, 7, 8, 11, 13, 15, 49, 18, 29, 31}
{3, 12, 14, 16, 17}
{1, 2, 4, 5, 41, 42, 43, 9, 22, 23}
{36, 37, 38, 6, 39, 47, 48, 20, 21, 25}
{35, 45}
{33, 6, 8, 9, 43, 17, 19, 20, 22, 24, 27, 28, 31}
{1, 12, 45, 44, 47, 50, 26}
{28, 47}
{16, 44}
{33, 1, 9, 17, 30}
{32, 37, 39, 40, 41, 19, 21, 23, 24, 27, 30}
{1, 4, 44, 46, 48, 21, 26, 29, 30}
{34, 7, 10, 43, 44, 21, 22}
{1, 2, 35, 4, 7, 10, 45, 47, 16, 49, 18, 24, 30}
{8, 18, 27, 45}
{12, 5, 6}
{7, 8, 41, 9, 11, 14, 25, 28}
{34, 5, 39, 11, 43, 48, 21, 23, 26}
{43, 36, 21, 44}
{17, 12, 46}
{2, 5, 37, 40, 41, 9, 11, 43, 45, 47, 49, 17, 24, 30, 31}
{33, 4, 7, 8, 41, 10, 12, 14, 16, 21, 25, 26}
{36, 29, 6, 39}
{1, 34, 37, 6, 43, 12, 44, 14, 15, 45, 17}
{24, 36, 21, 30}
{35, 4, 37, 7, 40, 11, 44, 15, 50, 18, 19, 21, 24, 28, 31}
{1, 38, 41, 43, 44, 13, 14, 46, 26}
{35, 4, 11, 12, 21, 25}

greedy_set_cover:
[{2, 5, 37, 40, 41, 9, 11, 43, 45, 47, 49, 17, 24, 30, 31}, {33, 4, 7, 8, 41, 10, 12, 14, 16, 21, 25, 26}, {35, 4, 37, 7, 40, 11, 44, 15, 50, 18, 19, 21, 24, 28, 31}, {36, 37, 38, 6, 39, 47, 48, 20, 21, 25}, {1, 2, 4, 5, 41, 42, 43, 9, 22, 23}, {32, 34, 40, 10, 50, 19, 26, 28, 30}, {24, 27, 44, 46}, {33, 7, 8, 11, 13, 15, 49, 18, 29, 31}, {3, 12, 14, 16, 17}]
9 (boyut)

brute_force_set_cover:
({32, 34, 40, 10, 50, 19, 26, 28, 30}, {24, 27, 44, 46}, {33, 7, 8, 11, 13, 15, 49, 18, 29, 31}, {3, 12, 14, 16, 17}, {1, 2, 4, 5, 41, 42, 43, 9, 22, 23}, {36, 37, 38, 6, 39, 47, 48, 20, 21, 25}, {35, 45})
7 (boyut)

##### Sonuç
Görüldüğü üzere "greedy_set_cover" 9 tane alt küme seçerken "brute_force_set_cover" sadece 7 alt küme seçerek işlemi yaptı. Yanlız süre olarak daha uzun sürdü.
