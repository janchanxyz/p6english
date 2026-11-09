#!/usr/bin/env python3
"""Build curated P4-appropriate English spelling pool with zh-Hant glosses.

Honesty note (written into README): Hong Kong EDB does not publish a separate
P4-only wordlist. Official targets are ~1000 by end of KS1 and ~2000 by end of
primary (KS2). The interactive Wordlists package (vocab09) is no longer a
machine-readable download. This pool is curated for Primary 4 spelling practice
from EDB thematic categories (animals, food, school, body, weather, transport,
home, jobs, sports, nature) and typical KS2 textbook vocabulary — concrete /
imageable nouns & verbs preferred so Wikimedia illustrations make sense.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "words-data.json"

# (word, zh, pos, theme) — single lowercase a-z words, length 4–12
RAW = [
  # Animals
  ("animal","動物","n","animals"),("tiger","老虎","n","animals"),("lion","獅子","n","animals"),
  ("elephant","大象","n","animals"),("monkey","猴子","n","animals"),("rabbit","兔子","n","animals"),
  ("turtle","烏龜","n","animals"),("butterfly","蝴蝶","n","animals"),("penguin","企鵝","n","animals"),
  ("dolphin","海豚","n","animals"),("giraffe","長頸鹿","n","animals"),("kangaroo","袋鼠","n","animals"),
  ("squirrel","松鼠","n","animals"),("leopard","豹","n","animals"),("peacock","孔雀","n","animals"),
  ("parrot","鸚鵡","n","animals"),("chicken","雞","n","animals"),("horse","馬","n","animals"),
  ("sheep","羊","n","animals"),("mouse","老鼠","n","animals"),("snake","蛇","n","animals"),
  ("frog","青蛙","n","animals"),("whale","鯨魚","n","animals"),("shark","鯊魚","n","animals"),
  ("zebra","斑馬","n","animals"),("panda","熊貓","n","animals"),("camel","駱駝","n","animals"),
  ("eagle","鷹","n","animals"),("spider","蜘蛛","n","animals"),("insect","昆蟲","n","animals"),
  ("puppy","小狗","n","animals"),("kitten","小貓","n","animals"),("goldfish","金魚","n","animals"),
  ("hamster","倉鼠","n","animals"),("crocodile","鱷魚","n","animals"),("octopus","八爪魚","n","animals"),
  # Food & drink
  ("apple","蘋果","n","food"),("banana","香蕉","n","food"),("orange","橙","n","food"),
  ("grape","葡萄","n","food"),("mango","芒果","n","food"),("watermelon","西瓜","n","food"),
  ("strawberry","草莓","n","food"),("pineapple","菠蘿","n","food"),("peach","桃","n","food"),
  ("lemon","檸檬","n","food"),("cherry","櫻桃","n","food"),("coconut","椰子","n","food"),
  ("bread","麵包","n","food"),("butter","牛油","n","food"),("cheese","芝士","n","food"),
  ("biscuit","餅乾","n","food"),("cookie","曲奇","n","food"),("sandwich","三文治","n","food"),
  ("hamburger","漢堡包","n","food"),("pizza","披薩","n","food"),("noodle","麵","n","food"),
  ("rice","飯","n","food"),("soup","湯","n","food"),("salad","沙律","n","food"),
  ("chicken","雞肉","n","food"),("sausage","香腸","n","food"),("egg","雞蛋","n","food"),
  ("milk","牛奶","n","food"),("juice","果汁","n","food"),("water","水","n","food"),
  ("coffee","咖啡","n","food"),("tea","茶","n","food"),("sugar","糖","n","food"),
  ("honey","蜜糖","n","food"),("chocolate","朱古力","n","food"),("icecream","雪糕","n","food"),
  ("candy","糖果","n","food"),("cake","蛋糕","n","food"),("pancake","班戟","n","food"),
  ("tomato","番茄","n","food"),("potato","馬鈴薯","n","food"),("carrot","紅蘿蔔","n","food"),
  ("onion","洋蔥","n","food"),("cabbage","椰菜","n","food"),("mushroom","蘑菇","n","food"),
  ("pepper","胡椒","n","food"),("breakfast","早餐","n","food"),("lunch","午餐","n","food"),
  ("dinner","晚餐","n","food"),("snack","小食","n","food"),("fruit","水果","n","food"),
  ("vegetable","蔬菜","n","food"),("kitchen","廚房","n","home"),
  # School & learning
  ("school","學校","n","school"),("teacher","老師","n","school"),("student","學生","n","school"),
  ("classroom","課室","n","school"),("blackboard","黑板","n","school"),("whiteboard","白板","n","school"),
  ("pencil","鉛筆","n","school"),("eraser","擦膠","n","school"),("ruler","間尺","n","school"),
  ("scissors","剪刀","n","school"),("glue","膠水","n","school"),("crayon","蠟筆","n","school"),
  ("marker","記號筆","n","school"),("notebook","筆記簿","n","school"),("textbook","教科書","n","school"),
  ("homework","家課","n","school"),("library","圖書館","n","school"),("dictionary","字典","n","school"),
  ("computer","電腦","n","school"),("tablet","平板電腦","n","school"),("backpack","背囊","n","school"),
  ("uniform","校服","n","school"),("recess","小息","n","school"),("principal","校長","n","school"),
  ("lesson","課堂","n","school"),("subject","科目","n","school"),("english","英文","n","school"),
  ("science","科學","n","school"),("maths","數學","n","school"),("music","音樂","n","school"),
  ("art","美術","n","school"),("history","歷史","n","school"),("geography","地理","n","school"),
  ("exam","考試","n","school"),("project","專題研習","n","school"),("classmate","同學","n","school"),
  ("question","問題","n","school"),("answer","答案","n","school"),("story","故事","n","school"),
  ("poem","詩","n","school"),("letter","信件","n","school"),("stamp","郵票","n","school"),
  # Body & senses
  ("body","身體","n","body"),("head","頭","n","body"),("hair","頭髮","n","body"),
  ("face","臉","n","body"),("eye","眼睛","n","body"),("ear","耳朵","n","body"),
  ("nose","鼻子","n","body"),("mouth","嘴巴","n","body"),("tooth","牙齒","n","body"),
  ("tongue","舌頭","n","body"),("neck","頸","n","body"),("shoulder","肩膀","n","body"),
  ("arm","手臂","n","body"),("hand","手","n","body"),("finger","手指","n","body"),
  ("leg","腿","n","body"),("foot","腳","n","body"),("knee","膝蓋","n","body"),
  ("heart","心臟","n","body"),("stomach","肚子","n","body"),("skin","皮膚","n","body"),
  ("bone","骨頭","n","body"),("blood","血液","n","body"),("brain","大腦","n","body"),
  # Clothes
  ("clothes","衣服","n","clothes"),("shirt","恤衫","n","clothes"),("blouse","女裝恤衫","n","clothes"),
  ("tshirt","T恤","n","clothes"),("sweater","冷衫","n","clothes"),("jacket","外套","n","clothes"),
  ("coat","大衣","n","clothes"),("dress","連身裙","n","clothes"),("skirt","裙子","n","clothes"),
  ("trousers","長褲","n","clothes"),("shorts","短褲","n","clothes"),("jeans","牛仔褲","n","clothes"),
  ("socks","襪子","n","clothes"),("shoes","鞋子","n","clothes"),("boots","靴子","n","clothes"),
  ("sandals","涼鞋","n","clothes"),("hat","帽子","n","clothes"),("cap","棒球帽","n","clothes"),
  ("scarf","圍巾","n","clothes"),("gloves","手套","n","clothes"),("belt","腰帶","n","clothes"),
  ("umbrella","雨傘","n","clothes"),("glasses","眼鏡","n","clothes"),("watch","手錶","n","clothes"),
  # Weather & nature
  ("weather","天氣","n","weather"),("sunny","晴朗的","adj","weather"),("cloudy","多雲的","adj","weather"),
  ("rainy","下雨的","adj","weather"),("windy","有風的","adj","weather"),("stormy","暴風雨的","adj","weather"),
  ("foggy","有霧的","adj","weather"),("snowy","下雪的","adj","weather"),("hot","熱的","adj","weather"),
  ("cold","冷的","adj","weather"),("warm","溫暖的","adj","weather"),("cool","涼爽的","adj","weather"),
  ("spring","春天","n","weather"),("summer","夏天","n","weather"),("autumn","秋天","n","weather"),
  ("winter","冬天","n","weather"),("rainbow","彩虹","n","weather"),("thunder","雷","n","weather"),
  ("lightning","閃電","n","weather"),("cloud","雲","n","weather"),("rain","雨","n","weather"),
  ("snow","雪","n","weather"),("wind","風","n","weather"),("sunshine","陽光","n","weather"),
  ("forest","森林","n","nature"),("mountain","山","n","nature"),("river","河","n","nature"),
  ("ocean","海洋","n","nature"),("beach","沙灘","n","nature"),("island","島","n","nature"),
  ("desert","沙漠","n","nature"),("garden","花園","n","nature"),("flower","花","n","nature"),
  ("tree","樹","n","nature"),("leaf","葉子","n","nature"),("grass","草","n","nature"),
  ("plant","植物","n","nature"),("seed","種子","n","nature"),("rock","岩石","n","nature"),
  ("stone","石頭","n","nature"),("sand","沙","n","nature"),("sky","天空","n","nature"),
  ("star","星星","n","nature"),("moon","月亮","n","nature"),("planet","行星","n","nature"),
  ("earth","地球","n","nature"),("sun","太陽","n","nature"),("fire","火","n","nature"),
  # Transport & places
  ("transport","交通","n","transport"),("bus","巴士","n","transport"),("train","火車","n","transport"),
  ("tram","電車","n","transport"),("ferry","渡輪","n","transport"),("taxi","的士","n","transport"),
  ("airplane","飛機","n","transport"),("helicopter","直升機","n","transport"),("bicycle","單車","n","transport"),
  ("scooter","滑板車","n","transport"),("motorcycle","電單車","n","transport"),("subway","地下鐵","n","transport"),
  ("station","車站","n","transport"),("airport","機場","n","transport"),("harbour","海港","n","transport"),
  ("bridge","橋","n","transport"),("tunnel","隧道","n","transport"),("road","路","n","transport"),
  ("street","街道","n","places"),("park","公園","n","places"),("market","街市","n","places"),
  ("supermarket","超級市場","n","places"),("restaurant","餐廳","n","places"),("hospital","醫院","n","places"),
  ("clinic","診所","n","places"),("museum","博物館","n","places"),("cinema","戲院","n","places"),
  ("theatre","劇院","n","places"),("stadium","體育館","n","places"),("playground","遊樂場","n","places"),
  ("swimming","游泳","n","sports"),("pool","泳池","n","places"),("zoo","動物園","n","places"),
  ("farm","農場","n","places"),("factory","工廠","n","places"),("office","辦公室","n","places"),
  ("hotel","酒店","n","places"),("bank","銀行","n","places"),("post","郵局","n","places"),
  ("church","教堂","n","places"),("temple","廟宇","n","places"),("castle","城堡","n","places"),
  ("village","鄉村","n","places"),("city","城市","n","places"),("country","國家","n","places"),
  # Home
  ("house","房子","n","home"),("apartment","公寓","n","home"),("bedroom","睡房","n","home"),
  ("bathroom","浴室","n","home"),("living","客廳","n","home"),("window","窗","n","home"),
  ("door","門","n","home"),("floor","地板","n","home"),("ceiling","天花板","n","home"),
  ("wall","牆","n","home"),("table","桌子","n","home"),("chair","椅子","n","home"),
  ("sofa","沙發","n","home"),("bed","床","n","home"),("pillow","枕頭","n","home"),
  ("blanket","毯","n","home"),("curtain","窗簾","n","home"),("lamp","燈","n","home"),
  ("mirror","鏡子","n","home"),("clock","時鐘","n","home"),("fridge","雪櫃","n","home"),
  ("oven","焗爐","n","home"),("stove","爐灶","n","home"),("microwave","微波爐","n","home"),
  ("washer","洗衣機","n","home"),("television","電視","n","home"),("telephone","電話","n","home"),
  ("camera","相機","n","home"),("radio","收音機","n","home"),("toy","玩具","n","home"),
  ("doll","玩偶","n","home"),("balloon","氣球","n","home"),("candle","蠟燭","n","home"),
  # Jobs & people
  ("doctor","醫生","n","jobs"),("nurse","護士","n","jobs"),("dentist","牙醫","n","jobs"),
  ("farmer","農夫","n","jobs"),("chef","廚師","n","jobs"),("baker","麵包師傅","n","jobs"),
  ("pilot","機師","n","jobs"),("driver","司機","n","jobs"),("police","警察","n","jobs"),
  ("firefighter","消防員","n","jobs"),("soldier","士兵","n","jobs"),("singer","歌手","n","jobs"),
  ("dancer","舞蹈員","n","jobs"),("actor","演員","n","jobs"),("artist","藝術家","n","jobs"),
  ("writer","作家","n","jobs"),("reporter","記者","n","jobs"),("engineer","工程師","n","jobs"),
  ("scientist","科學家","n","jobs"),("vet","獸醫","n","jobs"),("mailman","郵差","n","jobs"),
  ("family","家庭","n","people"),("parent","父母","n","people"),("father","父親","n","people"),
  ("mother","母親","n","people"),("brother","兄弟","n","people"),("sister","姊妹","n","people"),
  ("grandpa","爺爺","n","people"),("grandma","嫲嫲","n","people"),("cousin","堂表親","n","people"),
  ("friend","朋友","n","people"),("neighbour","鄰居","n","people"),("baby","嬰兒","n","people"),
  ("child","小孩","n","people"),("teenager","青少年","n","people"),("adult","大人","n","people"),
  # Sports & hobbies
  ("sport","運動","n","sports"),("football","足球","n","sports"),("basketball","籃球","n","sports"),
  ("volleyball","排球","n","sports"),("tennis","網球","n","sports"),("badminton","羽毛球","n","sports"),
  ("baseball","棒球","n","sports"),("hockey","曲棍球","n","sports"),("golf","高爾夫球","n","sports"),
  ("running","跑步","n","sports"),("jumping","跳躍","n","sports"),("cycling","騎單車","n","sports"),
  ("skating","溜冰","n","sports"),("skiing","滑雪","n","sports"),("surfing","滑浪","n","sports"),
  ("hiking","遠足","n","sports"),("camping","露營","n","sports"),("fishing","釣魚","n","sports"),
  ("reading","閱讀","n","hobbies"),("drawing","繪畫","n","hobbies"),("painting","油畫","n","hobbies"),
  ("singing","唱歌","n","hobbies"),("dancing","跳舞","n","hobbies"),("cooking","煮食","n","hobbies"),
  ("gardening","園藝","n","hobbies"),("puzzle","拼圖","n","hobbies"),("game","遊戲","n","hobbies"),
  # Verbs (imageable actions)
  ("jump","跳","v","verbs"),("climb","爬","v","verbs"),("swim","游","v","verbs"),
  ("fly","飛","v","verbs"),("run","跑","v","verbs"),("walk","走","v","verbs"),
  ("dance","跳舞","v","verbs"),("sing","唱歌","v","verbs"),("laugh","笑","v","verbs"),
  ("cry","哭","v","verbs"),("sleep","睡覺","v","verbs"),("wake","醒來","v","verbs"),
  ("eat","吃","v","verbs"),("drink","喝","v","verbs"),("cook","煮","v","verbs"),
  ("bake","焗","v","verbs"),("wash","洗","v","verbs"),("clean","清潔","v","verbs"),
  ("write","寫","v","verbs"),("read","讀","v","verbs"),("draw","畫","v","verbs"),
  ("paint","油漆","v","verbs"),("build","建造","v","verbs"),("open","打開","v","verbs"),
  ("close","關上","v","verbs"),("push","推","v","verbs"),("pull","拉","v","verbs"),
  ("throw","拋","v","verbs"),("catch","接住","v","verbs"),("kick","踢","v","verbs"),
  ("carry","攜帶","v","verbs"),("hold","握住","v","verbs"),("give","給","v","verbs"),
  ("take","拿","v","verbs"),("bring","帶來","v","verbs"),("find","找到","v","verbs"),
  ("lose","失去","v","verbs"),("help","幫助","v","verbs"),("play","玩","v","verbs"),
  ("work","工作","v","verbs"),("study","學習","v","verbs"),("learn","學習","v","verbs"),
  ("teach","教","v","verbs"),("listen","聽","v","verbs"),("speak","說","v","verbs"),
  ("talk","談話","v","verbs"),("think","想","v","verbs"),("dream","做夢","v","verbs"),
  ("smile","微笑","v","verbs"),("hug","擁抱","v","verbs"),("wave","揮手","v","verbs"),
  # Adjectives / describing (imageable where possible)
  ("happy","開心的","adj","feelings"),("sad","傷心的","adj","feelings"),("angry","生氣的","adj","feelings"),
  ("scared","害怕的","adj","feelings"),("tired","疲倦的","adj","feelings"),("excited","興奮的","adj","feelings"),
  ("lonely","寂寞的","adj","feelings"),("proud","自豪的","adj","feelings"),("brave","勇敢的","adj","feelings"),
  ("kind","善良的","adj","feelings"),("funny","有趣的","adj","feelings"),("clever","聰明的","adj","feelings"),
  ("beautiful","美麗的","adj","describing"),("ugly","醜陋的","adj","describing"),("pretty","漂亮的","adj","describing"),
  ("colourful","色彩繽紛的","adj","describing"),("bright","明亮的","adj","describing"),("dark","黑暗的","adj","describing"),
  ("heavy","重的","adj","describing"),("light","輕的","adj","describing"),("strong","強壯的","adj","describing"),
  ("weak","弱的","adj","describing"),("fast","快的","adj","describing"),("slow","慢的","adj","describing"),
  ("quiet","安靜的","adj","describing"),("noisy","嘈吵的","adj","describing"),("soft","軟的","adj","describing"),
  ("hard","硬的","adj","describing"),("smooth","光滑的","adj","describing"),("rough","粗糙的","adj","describing"),
  ("round","圓的","adj","describing"),("square","正方形的","adj","describing"),("triangle","三角形","n","describing"),
  ("circle","圓形","n","describing"),("rectangle","長方形","n","describing"),
  # Colours & numbers-ish nouns
  ("colour","顏色","n","colours"),("yellow","黃色","n","colours"),("purple","紫色","n","colours"),
  ("orange","橙色","n","colours"),("brown","棕色","n","colours"),("black","黑色","n","colours"),
  ("white","白色","n","colours"),("green","綠色","n","colours"),("blue","藍色","n","colours"),
  ("pink","粉紅色","n","colours"),("grey","灰色","n","colours"),("golden","金色的","adj","colours"),
  # Time
  ("morning","早上","n","time"),("afternoon","下午","n","time"),("evening","傍晚","n","time"),
  ("night","夜晚","n","time"),("midnight","午夜","n","time"),("today","今天","n","time"),
  ("tomorrow","明天","n","time"),("yesterday","昨天","n","time"),("weekend","週末","n","time"),
  ("holiday","假期","n","time"),("birthday","生日","n","time"),("calendar","日曆","n","time"),
  ("minute","分鐘","n","time"),("hour","小時","n","time"),("second","秒","n","time"),
  # Misc imageable KS2
  ("present","禮物","n","misc"),("gift","禮物","n","misc"),("party","派對","n","misc"),
  ("festival","節日","n","misc"),("parade","巡遊","n","misc"),("flag","旗","n","misc"),
  ("map","地圖","n","misc"),("globe","地球儀","n","misc"),("robot","機械人","n","misc"),
  ("machine","機器","n","misc"),("tool","工具","n","misc"),("hammer","鎚","n","misc"),
  ("ladder","梯子","n","misc"),("rope","繩","n","misc"),("box","盒子","n","misc"),
  ("bag","袋","n","misc"),("bottle","瓶子","n","misc"),("cup","杯","n","misc"),
  ("plate","碟","n","misc"),("bowl","碗","n","misc"),("spoon","匙羹","n","misc"),
  ("fork","叉","n","misc"),("knife","刀","n","misc"),("key","鎖匙","n","misc"),
  ("lock","鎖","n","misc"),("coin","硬幣","n","misc"),("money","錢","n","misc"),
  ("ticket","門票","n","misc"),("passport","護照","n","misc"),("photo","相片","n","misc"),
  ("picture","圖畫","n","misc"),("poster","海報","n","misc"),("newspaper","報紙","n","misc"),
  ("magazine","雜誌","n","misc"),("envelope","信封","n","misc"),("parcel","包裹","n","misc"),
  ("treasure","寶藏","n","misc"),("diamond","鑽石","n","misc"),("jewel","珠寶","n","misc"),
  ("crown","皇冠","n","misc"),("throne","寶座","n","misc"),("dragon","龍","n","misc"),
  ("monster","怪獸","n","misc"),("fairy","仙女","n","misc"),("wizard","巫師","n","misc"),
  ("pirate","海盜","n","misc"),("knight","騎士","n","misc"),("prince","王子","n","misc"),
  ("princess","公主","n","misc"),("queen","女王","n","misc"),("king","國王","n","misc"),
]

def normalize_word(w: str) -> str:
    w = w.strip().lower()
    w = w.replace("-", "").replace(" ", "")
    # keep only a-z
    return "".join(c for c in w if "a" <= c <= "z")

def main():
    seen = set()
    items = []
    for word, zh, pos, theme in RAW:
        w = normalize_word(word)
        if not w or w in seen:
            continue
        if len(w) < 4 or len(w) > 12:
            continue
        seen.add(w)
        items.append({
            "id": w,
            "word": w,
            "zh": zh,
            "pos": pos,
            "theme": theme,
            "imageUrl": "",
            "imageCredit": "",
            "imageUrls": [],
        })
    items.sort(key=lambda x: x["word"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} words → {OUT}")

if __name__ == "__main__":
    main()
