
sound_effects = """4011\tEffect Activate
4012\tMetal Slash
4013\tElectricity crackling
4019\tPower Up Additional
1026\tPower Up Additional
102\tSwoosh Small
103\tSwoosh Big
1000\tSmack
1001	Simple Punch
1002	R explosion
1003	Grasp, Grab, Clench
1004	Long Clench
1006	Scratch, Grab
1011	Dust Cloud
1015	Energy Blast Release
1016	Energy Blast Shot
1017	Energy Impact
1018	Super Attack Start Sound
1019	Flight Hum
1020	Energy Charging
1021	Energy Charge Release
1022	Energy Beam
1024	Generic Explosion
1031	Cut
1032	Slash
1035	Super Attack cut in
1036	Aura Powering Up
1037	Energy Swelling
1038	Electric Pulse
1040	Screen Shatter
1041	Crack Screen
1042	Dramatic Effect Cut in - Dodge Sound
1043	Electricity (Battle Start)
1044	Rumbling
1045	Break Swoosh
1046	Metal Scratch - Hit
1047	Fast Movement
1048	Sudden Movement
1049	Electricity Disharge
1050	Static Electricity
1053	Launched Flying, Firework Launch
1055	Electric Shock, Orb Charging
1056	Electric Current
1062	Effect Cut In Sound - end of intro sound
1063	EZA Battle Level
1066	Giant Roar
1067	Shine Explosion, SR Explosion
1069	Large Energy Surge Explosion
1070	Crunchy Bite
1071	Munching
1106	Footstep 1
1107	Footstep 2
1108	Footstep 3
1109	Vanishing Step
1110	Impact
1114	Pulse Shot
1115	Magical Chime
1117	Multiple Wind Swirls
1120	DBZ Heavy Impact - Powerful Punch
1121	Sent Flying
1122	Energy Instant Surge
1123	Machine Ambience - Dark Catherdral Ambience
1125	Distant Roar
1126	Dramatic Shock, Glass Shatter - Impact
1127	Magic Energy Metamorph
1128	Distant Energy Wave
1129	Wind Howling
1130	Energy Cluster (Chirp)
1131	Energy Cluster Release
1132	Energy Gathering
1133	Energy Ball Shot
1134	Drinking, Gulping
1135	Mechanical Step
1136	Mechanical Whirring - Mechanical Charge Up
1137	Energy Release Shockwave
1138	Pitter Patter, Wings Flapping
1139	Birds Chirping
1140	Insects Buzzing
1141	Steel Clash 1
1142	Quick Air Sweep
1143	Steel Clash 2
1144	Mechanical Screech
1145	Energy Cluster Shot
1146	Energy Pulse Wave
1147	Malfunctioning, High Electrical Current
1148	Short-circuiting
1149	Machine Gun Fire, SMG Gun Shots
1150	Gun Reload
1153	Deep Impact
1154	Energy Shot Forming
1155	Energy Bullet Fire
1156	Wind Gust
1159	Big Explosion 1
1160	Big Explosion 2
1161	Energy Field Surge
1163	Splash
1164	Wind Blowing
1165	Strong Winds - Waves
1166	Tides
1167	Wind Rise - Zoom
1168	Rubble Falling
1169	Metal Slam
1170	Weapon Wielded
1171	Gleam
1172	Energy Slice
1173	Ground Shake & Energy
1174	More Bird Chirping
1175	Wind Increasing Speed
1176	Wind Blowing & Electricity
1177	Pulse Shot
1178	Energy Pulse Bullet Shot
1182	Distant Bang
1185	Energy Whistling
1189	Swipe
1191	Intense Energy Converging
1193	Flying Crashing Through Enviornment
1202	Ki Converging
1203	Motor, Static Whirring
1207	High Jump
1208	Gripping, Landing
1209	Harnessing Energy
1210	Lots of energy gathering (long)
1216	Energy Shine Glitter
1217	Energy Shine Burst
1218	Soda Can
1229	Distant Thunder, Robes - clothes blowing in the wind
1231	Gust Clearing Dust
1232	Dash Movement
1233	Grabbing Lightly - Softly, Firmly
1235	Beam Sword, Light Swoosh
1236	Energy Disperse
1237	Dramatic Wood Hit
1238	Drawing Blade - Sword, Clashing Sword
1243	Radio Static
1245	Quick Swipe, Wind Swipe
1247	Steam Releasing, Buu letting out steam
1251	Boing
1252	Faint Electric Current
1254	Energy Winding
1255	Energy Swirling
1258	Energy Surge Impact
1260	Pumping, Cocking Gun
1264	Shinning Energy Release
1268	Wind Noise
1269	Machine Ambience
1273	Potara Earings pulse
1274	Energy Swoosh
1275	Energy buzzing
1276	Ki Ball Charging
1280	Ear twitch, body twitch
1281	Siren, Ki Ringing
1282	Ki Cluster
1283	Ki Bomb Forming
1288	Wind chimes, sparkles
1289	Magical Glow
1296	Ki Ball Charging Long
1308	Dark Ambience With Chimes
1315	Bling
1324	Tapion's Flute (Ocarina) 1
1331	Cape, Clothes 1
1332	Cape, Clothes 2
1333	Cape, Clothes 3
1367	Rubbing Cloth
1387	Metal Sheet, Metal Clank
1396	Fly Buzzing energy
1397	Radiating Energy
1406	Barrage of Ki Shots
1425	Rapid Punches
1472	Heavy Footstep (Broly)
1515	Super attack Start Sound"""

list_with_id = sound_effects.split("\n")
id_and_name = {}
for x in list_with_id:
    id_and_name[x.split("\t")[0]] = x.split("\t")[1]
    
if __name__ == "__main__":
    for x in id_and_name:
        print(x, id_and_name.get(x))
    