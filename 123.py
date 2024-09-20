# Maveli Chatbot in Python - Answers everything related to Onam celebration

def Maveli():
    print("Maveli: Hello, Njan Maveli! Onathine pati chodyam poratte..!")
    print("Type 'nirthu please' to end the conversation.\n")
    print("Use these Keywords for better output:- 1) enthanu = what, 2) pookalam = flower carpet, 3) sadya = feast, 4) aaghosham = celebration")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "nirthu please" in user_input:
            print("Maveli: Tataaaa njan ponu..! Evarkkum ente hridayam niranja Oonashamsakal🌼❤!")
            break

        # Responding to Onam related questions
        elif "hello" in user_input or "hai" in user_input:
            print("Maveli: Hai makkale....Onam okke ngane ponu....")
            
        elif "sugam" in user_input or "kollam" in user_input or "super" in user_input or "adipoli" in user_input:
            print("Maveli: Aahaa Sandhosham......")

        elif "avataram" in user_input or "avatar" in user_input:
            print("Maveli: Ente shakthiye thadayaan, devanmaar prapanchathinte samrakshakanaaya mahaavishnuvilekku thirinju. Prapancha kramam punasthaapikkumbol ente nanmaye samrakshikkunna reethiyil edapedaan vishnu bhagavan theerumaanichu. Enne samarthamaayum ahimsaathmakamaayum sameepikkan adheham vaamananaayi avatharichu. Njan sangadippicha oru mahathaaya yaagathil (yajnjam) vaamanan ente munbaake prathyakshappettu oru lalithamaaya sammaanam chodichu - moonnadi bhoomi. Audaaryathinu peruketta njan, vaamanan oru saadhaarana braahmananallennu manasilaakkiya thante aathmeeya upadeshtaavaaya shukraachaaryante munnariyippu avaganichu udan thanne abhyarthana anuvadichu.")

        elif user_input in "maveliyude charithram" or user_input in "charithram":
            print("Maveli: Hindu puraanangalil devanmaarude (daivangalude) prathiroopamaayi palappozhum kanakkaakkappedunna asura vamshathilppettayalaanu mahabali. Maha Vishnuvinte bhakthanaaya asura rajavaaya prahlaadante cherumakanaayirunnu adheham. Prahlaadante pithaavu, hiranyakashipu, shakthanum ennaal svechaadhipathiyum aaya rajavaayirunnu, devanmaarodulla ahankarathinum shathruthaykkum perukettavanaayirunnu. Ennirunnaalum, prahlaadan, asurarude kudumbathil janichittum, sadgunasambannanum bhakthanumaayirunnu, avan vishnuvine aaraadhichu.Mahabalikku thante muthachante punyavum bhakthiyum paarambaryamaayi labhichengilum thante asura poorvvikareppole adhikaaram thedukayum cheythu. Adheham thante kaalathe ettavum shakthanaaya rajaakkanmaaril oralaayittheernnu, sainika vijayangalkku maathramalla, thante neethikkum prajakalodulla karuthalinum perukettathaanu.")

        elif user_input == "ethra divasathe aaghosham aanu onam?" or user_input == "onam is celebrated in how many days" or "days" in user_input or "diavsam" in user_input or user_input == "number of days" or user_input == "divasangal":
            print("Onam 10 divasam neenda aaghosham aanu.")
            
        elif user_input == "onam" or "enthanu onam" in user_input or "what is onam" in user_input:
            print("Maveli: Malayalikalude deshiya ulsavam aanu Onam.Chingamasathilanu Onam Malayalikal Aaghoshikunnath...Njan ningale kaanuvan varshathil orikkal ethunna divasam aanu Onam.")
        
        elif "who are you" in user_input or "maveli" in user_input or user_input == "ningal aara":
            print("Maveli: Enne arayilla....?  Njan Mahabali thampuran athava Maveli, Keralathile ithihaasa rajavu. Ente bharanakaalathu, bhoomi samrudhamaayirunnu, ellaavarum samathwathilum aikyathilum jeevichu. Ente aalukal enne valareyadhikam snehichu, Maha Vishnu enne paathaalathilekku ayachengilum, ella varshavum onakkaalathu njaan ente priyappetta prajakale sandarshikkanum avarude sandosham kaananum madangivarum.")
        
        elif "story of onam" in user_input or "legend of onam" in user_input or "ithihasam" in user_input:
            print("Maveli: Ente prajakale sandharsikanulla ente thirichuvaravanu Onathinte ithihasam ennu arayapedunnath. Vamanan enne pathalathilek ayachathinu shesham aanu Maha Vishu enik ee varam nalkiyath.")
        
        elif "pookalam" in user_input or "enthinanu onathinu pookalam idunnath?" in user_input:
            print("Maveli: Prakrithiyodulla aadarasoochakamaayum enne varavelkkunnathinumaayi Onakkaalathu nadathunna pushpaalankaramaanu pookkalam!")

        elif user_input == "pathu divasangalilaayi engane aanu onam aagoshikkunnath?" or "10 days of onam" in user_input:
            print("Maveli: Patthudivasathe onam atham naalil aarambhichu thiruvonanaalil samaapikkum. Ooro divasathinum athintethaaya praadhaanyamundu. Aalukal pushpa paravathaanikal (pookkalam) thayyaarakki thudangunnu, thiruvaathira, virunnukal (sadya), saamskarika prakadanangal, kalikal thudangiya parambaraagatha nrithangaliloode aagoshangal kramena vardhikkunnu. Avasaana divasamaaya thiruvonam, enne varavelkkanulla vipulamaaya sadyakalum praarthanakalumulla ellathilum shreshtamaanu.")

        elif user_input == "thiruvonam" or "thiruvonathinte mahathmyam" in user_input or "thiruvonathinte pradhanyam" in user_input or user_input == "importance of thiruvonam":
            print("Maveli: Aagoshangalude paaramyathe adayalappeduthunna thiruvonamaanu onathinte ettavum pradhaanappetta dinam. Mahabali rajavaaya njaan ente janangale sandarshikkunna divasamaanennaanu viswasam. Valiya virunnukal orukkunnu, enne swagatham cheyyunnathinaayi aachaarangal nadathappedunnu, ente aalukal sandoshavum samrudhiyum undennu urappaakkunnu.")
        
        elif "sadya" in user_input:
            print("Maveli: Onakkaalathu vaazhayilayil vilambunna valiya bhakshana virunnu aanu sadya. Chor, saambar, aviyal, paayasam, angane palathum ithil ulppedunnu!")
        
        elif "vallamkali" in user_input or "boat race" in user_input:
            print("Maveli: Ente naattukaarude koottaaya pravarthanatheyum chaithanyatheyum pratheekappeduthunna parambaraagatha malsaram aanu Onakalath nadakunna Vallamkali.")
        
        elif user_input == "clothes" or "onakkodi" in user_input or "onakodi" in user_input:
            print("Maveli: Onakkaalathu dharikkunna puthuvasthratheyaanu Onakkodi ennu parayunnathu. Aagoshathinte adayalamaayi aalukal parasparam puthiya vasthrangal sammaanikkunnu.")
        
        elif "thiruvathira" in user_input:
            print("Maveli: Snehavum sandoshavum aagoshikkan sthreekal onakkaalathu nadathunna parambaraagatha nrithamaanu thiruvaathira.")
            
        elif "onam games" in user_input or "onakalikal" in user_input:
            print("Maveli: Vadamvali, Kuttiyum kolum ennivayulppede onakkaalathu kalikkunna parambaraagatha kalikalaanu Onakkalikal.!")
        
        elif "vishnu" in user_input:
            print("Maveli: Maha vishnu thante vaamanaavathaarathil ennodu moonnadi bhoomi chodichu, oduvil enne paathaalathilekku ayachu. Pakshe ella onathinum njan ente prajakale kanan thirichu vararund!")
        
        elif "how is onam celebrated" in user_input or "aaghosham" in user_input or "onaghosham" in user_input:
            print("Maveli: Sadya, pookkalam, thiruvaathira, vallamkali, Onakkodi ennivayodeyaanu onam aagoshikkunnathu. Ithu sandoshathinteyum Othorumayudeyum samayamaanu.")
        
        elif user_input == "happy onam" or user_input == "happy":
            print("Maveli: Nandi! Ningalkkum sandoshavum aishvaryavum niranja oru Onam aashamsikkunnu!")

        elif user_input == "enthukondaanu aalukal onathinu onakkodi dharikkunnathu?":
            print("Maveli: Onakkaalathu aalukal dharikkunna puthuvasthratheyaanu onakkodi ennu parayunnathu. Ithu puthukkalinteyum visudhiyudeyum sandoshathinteyum pratheekamaanu. Kudumbathinum suhruthukkalkkum puthuvasthrangal sammaanikkunnathu snehathinteyum samrudhiyudeyum adayalamaayi onakkaalathu oru pradhaana aachaaramaanu.")

        elif "vallamkali" in user_input or user_input == "enthukondanu vallamkali onathinu nadathunnath":
            print("Maveli: Onakkaalathu nadakkunna prasidhamaaya paambu vallamkaliyaanu vallamkali. Aalukal ee neenda boatukal samanvayathode thuzhayumbol ithu aikyatheyum team workineyum pratheekappeduthunnu. Janakkoottathe aakarshikkunnathum onagoshangalude highlight aayathumaaya oru valiya kaazchayaanithu.")

        elif "vamanan" in user_input or "Maha Vishnu" in user_input or user_input == "who is vamanan" or user_input == "aaranu vamanan" or user_input == "vamanan aaranu":
            print("Maveli: Maha Vishnu vaamanan enna braahmanante roopameduthu enne sandarshichu. Avan moonnadi bhoomi chodichu, udaaramathiyaaya rajavaayathinal njaan sammathichu. Ennaal vaamanan randu padikal kondu bhoomiyeyum aakshatheyum aavaranam cheythu valuthaayi valarnnu. Moonnaamathethinu, njaan ente thala vaagdaanam cheythu, avan enne paathaalathilekku thallivittu. Ennirunnaalum, ella varshavum onakkaalathu ente aalukale sandarshikkanulla anugraham enikku labhichu.")

        elif user_input == "relation between onam and maveli" or user_input == "maveliyum onavum thammil ulla bhandham":
            print("Maveli: Njaan, Mahabali rajavu (maaveli), keralam neethiyum nyaayavum samathwavumaayi bharichu. Ente bharanakaalathu aalukal sandustaraayirunnu, samrudhiyil jeevichu. Maha Vishnu enne paathaalathilekku paranjayachengilum, ente aalukal enne snehathode orkkukayum onakkaalathu gambheeramaaya aagoshangalode enne sweekarikkukayum cheyyunnu.")

        elif user_input == "christmas":
            print("Maveli: Christmasine pati Santa claus gptyod poyi chodiku makane...!")
        
        else:
            print("Maveli: Athoke arayan mathram njan valarnilla...Ee pinchu manasine ingane novikalle..🥺!..........ULLATH KOND ONAM POLE ENNU KETITILLE....🫣")

# Run the Maveli chatbot
if __name__ == "__main__":
    Maveli()
