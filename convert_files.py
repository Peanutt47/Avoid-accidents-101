text = """จังหวัดกรุงเทพมหานคร Bangkok
จังหวัดพัทยา Pattaya
จังหวัดกระบี่ Krabi
จังหวัดกาญจนบุรี Kanchanaburi
จังหวัดกาฬสินธุ์ Kalasin
จังหวัดกำแพงเพชร Kamphaeng Phet
จังหวัดขอนแก่น Khon Kaen
จังหวัดจันทบุรี Chanthaburi
จังหวัดฉะเชิงเทรา Chachoengsao
จังหวัดชลบุรี Chon Buri
จังหวัดชัยนาท Chai Nat
จังหวัดชัยภูมิ Chaiyaphum
จังหวัดชุมพร Chumphon
จังหวัดตรัง Trang
จังหวัดตราด Trat
จังหวัดตาก Tak
จังหวัดนครนายก Nakhon Nayok
จังหวัดนครปฐม Nakhon Pathom
จังหวัดนครพนม Nakhon Phanom
จังหวัดนครราชสีมา Nakhon Ratchasima
จังหวัดนครศรีธรรมราช Nakhon Si Thammarat
จังหวัดนครสวรรค์ Nakhon Sawan
จังหวัดนนทบุรี Nonthaburi
จังหวัดนราธิวาส Narathiwat
จังหวัดน่าน Nan
จังหวัดบึงกาฬ Bueng Kan
จังหวัดบุรีรัมย์ Buri Ram
จังหวัดปทุมธานี Pathum Thani
จังหวัดประจวบคีรีขันธ์ Prachuap Khiri Khan
จังหวัดปราจีนบุรี Prachin Buri
จังหวัดปัตตานี Pattani
จังหวัดอยุธยา Phra Nakhon Si Ayutthaya
จังหวัดพะเยา Phayao
จังหวัดพังงา Phangnga
จังหวัดพัทลุง Phatthalung
จังหวัดพิจิตร Phichit
จังหวัดพิษณุโลก Phitsanulok
จังหวัดภูเก็ต Phuket
จังหวัดมหาสารคาม Maha Sarakham
จังหวัดมุกดาหาร Mukdahan
จังหวัดยะลา Yala
จังหวัดยโสธร Yasothon
จังหวัดระนอง Ranong
จังหวัดระยอง Rayong
จังหวัดราชบุรี Ratchaburi
จังหวัดร้อยเอ็ด Roi Et
จังหวัดลพบุรี Lop Buri
จังหวัดลำปาง Lampang
จังหวัดลำพูน Lamphun
จังหวัดศรีสะเกษ Si Sa Ket
จังหวัดสกลนคร Sakon Nakhon
จังหวัดสงขลา Songkhla
จังหวัดสตูล Satun
จังหวัดสมุทรปราการ Samut Prakan
จังหวัดสมุทรสงคราม Samut Songkhram
จังหวัดสมุทรสาคร Samut Sakhon
จังหวัดสระบุรี Saraburi
จังหวัดสระแก้ว Sa Kaeo
จังหวัดสิงห์บุรี Sing Buri
จังหวัดสุพรรณบุรี Suphan Buri
จังหวัดสุราษฎร์ธานี Surat Thani
จังหวัดสุรินทร์ Surin
จังหวัดสุโขทัย Sukhothai
จังหวัดหนองคาย Nong Khai
จังหวัดหนองบัวลำภู Nong Bua Lam Phu
จังหวัดอำนาจเจริญ Amnat Charoen
จังหวัดอุดรธานี Udon Thani
จังหวัดอุตรดิตถ์ Uttaradit
จังหวัดอุทัยธานี Uthai Thani
จังหวัดอุบลราชธานี Ubon Ratchathani
จังหวัดอ่างทอง Ang Thong
จังหวัดเชียงราย Chiang Rai
จังหวัดเชียงใหม่ Chiang Mai
จังหวัดเพชรบุรี Phetchaburi
จังหวัดเพชรบูรณ์ Phetchabun
จังหวัดเลย Loei
จังหวัดแพร่ Phrae
จังหวัดแม่ฮ่องสอน Mae Hong Son"""
print(text[:7])
dict = {}
temp = []
for i in text.split("จังหวัด"):
    if i != "":
     temp.append(i.replace('\n',''))
for i in temp:
    dict[i.split(" ", 1)[0]] = i.split(" ", 1)[1]
print(dict)

import pandas as pd

df = pd.read_csv("accident2022.csv")
df.replace(dict, inplace=True)
df.to_csv("accident2022(eng).csv", encoding='utf-8-sig')



