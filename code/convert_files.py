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
จังหวัดพังงา Phang Nga
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

df = pd.read_csv("../file/accident2022.csv")
df.replace(dict, inplace=True)
df.to_csv("accident2022(eng).csv", encoding='utf-8-sig')
# import json
#
# listf = []
# with open("thailand_province_relations.txt", "r") as file:
#     data = file.read().splitlines()
# for i in data:
#     source, destinations = i.split(" -> ")
#     destinations_list = destinations.split(", ")
#     for j in destinations_list:
#         listf.append((source, j))
#
#
# with open('province.json', 'r') as file:
#     data = json.load(file)
# # Create a list of tuples
# # formatted_routes = [(source, destination) for destination in destinations_list]
#
# print(listf)
# import networkx as nx
# import matplotlib.pyplot as plt
#
# def haversine_distance(lat1, lon1, lat2, lon2):
#     from math import radians, sin, cos, sqrt, atan2
#
#     # Convert coordinates to radians
#     lat1 = radians(lat1)
#     lon1 = radians(lon1)
#     lat2 = radians(lat2)
#     lon2 = radians(lon2)
#
#     # Haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1-a))
#     radius = 6371  # Radius of the Earth in kilometers
#     distance = radius * c
#     return distance
#
# # Create an empty graph
# G = nx.Graph()
# for province in data:
#     G.add_node(province)
# # Add edges to the graph
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         province_i = list(data.keys())[i]
#         province_j = list(data.keys())[j]
#         coordinates_i = data[province_i]
#         coordinates_j = data[province_j]
#         distance = haversine_distance(coordinates_i[0], coordinates_i[1], coordinates_j[0], coordinates_j[1])
#         for c in listf:
#             G.add_edge(c[0], c[1], weight=distance)
#         # graph.add_edge(province_i, province_j, weight=distance)
#
# # Plot the network graph
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(G, seed=42)
# nx.draw_networkx(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=8)
# plt.title("Province Connections")
# plt.axis('off')
# plt.tight_layout()
# plt.show()
