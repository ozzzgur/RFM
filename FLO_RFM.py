
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
                     # b. Değişken isimleri,
                     # c. Betimsel istatistik,
                     # d. Boş değer,
                     # e. Değişken tipleri, incelemesi yapınız.
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.


# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
# 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

# GÖREV 2: RFM Metriklerinin Hesaplanması
# Recency, Frequency, Monetary
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
# ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
# yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.

# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
# alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.
# GÖREV 6: Tüm süreci fonksiyonlaştırınız.





###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################
import datetime as dt
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.width', 500)
df = pd.read_csv("python_for_data_science/pythonProject/odevler/flo/flo_data_20k.csv")

df.head(10)
df.columns
df.info()
df.describe().T
df.isnull().sum()

# 2. Veri setinde
        # a. İlk 10 gözlem,
        # b. Değişken isimleri,
        # c. Boyut,
        # d. Betimsel istatistik,
        # e. Boş değer,
        # f. Değişken tipleri, incelemesi yapınız.



# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.


df["order_num_total_ever_both"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]

df["customer_value_total_ever_both"] = df["customer_value_total_ever_online"] + df ["customer_value_total_ever_offline"]




# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.


# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)

def objtoday(dataframe):
    for column in dataframe.columns[dataframe.columns.str.contains("date")]:
        dataframe[column] = dataframe[column].apply(pd.to_datetime)
        print(f"{column} changed to datetime")
objtoday(df)


# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız. 


df.groupby("order_channel").agg({"master_id": "count",
                                 "order_num_total_ever_both": "mean",
                                 "customer_value_total_ever_both": "mean"})

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.sort_values("customer_value_total_ever_both",ascending = False).head(10)


# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.sort_values("order_num_total_ever_both",ascending= False).head(10)


# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def prep_data(dataframe):
    objtoday(dataframe)
    dataframe["order_num_total_ever_both"] = dataframe["order_num_total_ever_online"] + dataframe[
        "order_num_total_ever_offline"]
    dataframe["customer_value_total_ever_both"] = dataframe["customer_value_total_ever_online"] + dataframe[
        "customer_value_total_ever_offline"]
#def data_prep(dataframe):
#    dataframe["order_num_total"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
#    dataframe["customer_value_total"] = dataframe["customer_value_total_ever_offline"] + dataframe["customer_value_total_ever_online"]
#    date_columns = dataframe.columns[dataframe.columns.str.contains("date")]
#    dataframe[date_columns] = dataframe[date_columns].apply(pd.to_datetime)
#    return df
prep_data(df)

###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################



# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi
df.head()
df["last_order_date"].max()
today = dt.datetime(2021,6, 1)
#apply(lambda x: x.days)
df["recency"] = (today - df["last_order_date"]).apply(lambda x: x.days)

df["frequency"] = df["order_num_total_ever_both" ]



df["monetary"] = df ["customer_value_total_ever_both"]

rfm = df[["master_id","recency","frequency","monetary","interested_in_categories_12","customer_value_total_ever_both"]]

rfm.describe().T


###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################



#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi

rfm["recency_score"] = pd.qcut(rfm["recency"],5,labels=[5 ,4 ,3 ,2 ,1 ])


rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"),5, labels= [1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels= [1, 2, 3, 4, 5])





# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi

rfm["rfm_score"] = (rfm["recency_score"].astype(str)+rfm["frequency_score"].astype(str))


rfm.describe().T

rfm[rfm["rfm_score"]=="55"]


###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}


rfm["segment"] = rfm["rfm_score"].replace(seg_map,regex=True)






###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.


rfm.groupby("segment").agg({"recency": "mean",
                            "frequency" : "mean",
                            "monetary" : "mean"})

# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.


target = rfm[rfm["interested_in_categories_12"].str.contains("KADIN")]
target = target[(target["segment"]=="champions") | (target["segment"] == "loyal_customers") &\
                (target["customer_value_total_ever_both"].mean() > 250)]
woman_champ_loyal_250 = target[["segment","customer_value_total_ever_both","interested_in_categories_12"]]


woman_champ_loyal_250.to_csv("yeni_marka_hedef_musteri.csv")
#flo_kadin = new_df.loc[(new_df["segment"].isin(["champions", 'loyal_customers'])) &
#           (new_df["interested_in_categories_12"].str.contains("KADIN"))]



# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.

target_2 = rfm[(rfm["interested_in_categories_12"].str.contains("COCUK")) | (rfm["interested_in_categories_12"].str.contains("ERKEK"))]

target_customer = target_2[(target_2["segment"] == "cant_loose") | (target_2["segment"] =='hibernating') | \
    (target_2["segment"]=='new_customers')]

target_customer.to_csv("indirim_hedef_müşteri_ids.csv")


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

def objtoday(dataframe):
    for column in dataframe.columns[dataframe.columns.str.contains("date")]:
        dataframe[column] = dataframe[column].apply(pd.to_datetime)
        print(f"{column} changed to datetime")
objtoday(df)


def prep_data(dataframe):
    objtoday(dataframe)
    dataframe["order_num_total_ever_both"] = dataframe["order_num_total_ever_online"] + dataframe[
        "order_num_total_ever_offline"]
    dataframe["customer_value_total_ever_both"] = dataframe["customer_value_total_ever_online"] + dataframe[
        "customer_value_total_ever_offline"]

prep_data(df)

def create_rfm(dataframe,csv=False):
    # Veri hazırlama
    prep_data(dataframe)

    # RFM Metriklerinin Hazırlanması

    today = dataframe["last_order_date"].max()+ dt.timedelta(days=2)

    dataframe["recency"] = (today - dataframe["last_order_date"]).apply(lambda x: x.days)

    dataframe["frequency"] = dataframe["order_num_total_ever_both"]

    dataframe["monetary"] = dataframe["customer_value_total_ever_both"]

    rfm = dataframe[["master_id", "recency", "frequency", "monetary", "interested_in_categories_12",
              "customer_value_total_ever_both"]]


    # RFM Scorenın Oluşturulması

    rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])

    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

    rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])

    rfm["rfm_score"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

    # Segmentasyon

    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_Risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm["segment"] = rfm["rfm_score"].replace(seg_map, regex=True)

    rfm.index = rfm.index.astype(int)

    if csv:
        rfm.to_csv("casestudy1.csv")

    return rfm


create_rfm(df,csv=True)
