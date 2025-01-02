import os, sys

#### DLC 도전과제 저장하는 구조체 ####
class DLC: 
    ## 구조체 본체
    def __init__(self, image, name, description):
        self.image = image
        self.name = name
        self.description = description

    ## 구조체 확인용 함수
    def show_info(self):
        print(f"[이미지]: {self.image}")
        print(f"[이름]: {self.name}")
        print(f"[설명]:")
        for description in self.descriptions:
            print(f"- {description}")


#### 이미지 객체(이미지 경로)를 배열에 저장하는 함수 ####
def load_images(image_dir):
    # 이미지 배열 선언
    respect_images = []

    # 이미지 파일 목록 얻기
    image_files = os.listdir(image_dir)

    # # 이미지 파일 오름차순 정렬
    image_files.sort(key=lambda x: int(x.split(".")[0]))

    # 이미지 배열에 이미지 객체 저장
    for image_file in image_files:
        image_path = image_dir + "/" + image_file
        respect_images.append(image_path)

    return respect_images   # 이미지 객체를 저장한 리스트 변수 반환

final_data = []   # 모든 데이터셋을 병합 저장할 리스트 변수 초기화


# 절대경로
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)





rptv_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/1. DJMAX RESPECT V")
rptv_name = ["이 게임은 내가 지배한다",
            "나만 운없어...",
            "대신귀여운업적을드리겠습니다",
            "압도적 감사",
            "엔비레인저가 되고싶어",
            "기어 중의 기어",
            "노트의 형태",
            "플레이트 콜렉터",
            "아무 말 대잔치",
            "마이 리틀 갤러리",
            
            "와 무대를 뒤집어 놓으셨다",
            "실력 검증",
            "손은 노트보다 빠르니까",
            "숨겨왔던 재능",
            "콤보를 위해 판정은 포기!",
            "한계 돌파",
            "JUST 100%",
            "푹 빠졌구나",
            "내가 DJMAX를 온라인때부터 시작했다",
            "ON AIR",
            
            "공기반 소리반",
            "여러분의 관심사와 흥미를 빅 데이터로 분석하여",
            "투머치토커",
            "하트 시그널",
            "순탄한 여행",
            "프로다운 실력",
            "BEAT MAESTRO",
            "내 솜씨를 제대로 보여줄 시간이군",
            "자강두천",
            "내가 브론즈일리 없어",
            
            "흑염룡이 잠깐 꿈틀거림",
            "금빛환향",
            "아 너무 무섭다",
            "콤보 마이스터",
            "THE LORD OF COMBO",
            "점수를 모아야 이득인 부분",
            "열심히 해야지 방법이 없습니다",
            "완벽 그 자체",
            "S랭크 마스터",
            "축제 분위기",
            
            "츄라이 츄라이",
            "지기 싫다고 생각하고 있어",
            "왕위를 계승시키는 중입니다",
            "슈퍼 루키",
            "절반의 성공",
            "DJMAX GRAND MASTER",
            "해피 럭키 데이",
            "그 성과",
            "고고학자",
            "내 마음 속에 저장",
            
            "DJ Alpha Resigns",
            "RESPECT V"]

rptv_description = ["모든 곡을 클리어했다.⭐",
                    "BREAK 1개로 클리어했다.",
                    "처음으로 클리어에 실패했다.",
                    "크레딧을 처음으로 감상했다.⭐",
                    "콜렉션에서 NB Ranger 시리즈의 모든 뮤직 비디오를 감상했다.⭐",
                    "10가지의 기어를 획득했다.⭐",
                    "10가지의 노트를 획득했다.",
                    "30가지의 플레이트를 획득했다.",
                    "50가지의 코멘트를 획득했다.",
                    "100장의 이미지를 획득했다.",
                    
                    "난이도 10 이상의 패턴 10개를 MAX COMBO로 클리어했다.⭐",
                    "난이도 10 이상의 패턴 30개를 MAX COMBO로 클리어했다.⭐",
                    "난이도 10 이상의 패턴 50개를 MAX COMBO로 클리어했다.⭐",
                    "100개의 패턴을 MAX COMBO로 클리어했다.⭐",
                    "300개의 패턴을 MAX COMBO로 클리어했다.⭐",
                    "500개의 패턴을 MAX COMBO로 클리어했다.⭐",
                    "PERFECT PLAY로 클리어했다.",
                    "임의의 버튼으로 마스터 스코어의 달성률을 40% 달성했다.⭐",
                    "임의의 버튼으로 마스터 스코어의 달성률을 80% 달성했다.⭐",
                    "AIR를 처음으로 플레이했다.",
                    
                    "OPEN MATCH에서 채팅을 전송했다.⭐",
                    "AIR에서 자신이 가장 좋아하는 곡을 플레이했다.⭐",
                    "AIR에서 10곡에 대한 코멘트를 작성했다.",
                    "AIR에서 스티커를 붙였다.",
                    "미션 10개를 클리어했다.⭐",
                    "미션 30개를 클리어했다.⭐",
                    "미션 50개를 클리어했다.⭐",
                    "래더 매치를 처음으로 플레이했다.",
                    "래더 매치에서 동점을 기록했다.⭐",
                    "래더 매치에서 브론즈 등급으로 승급했다.⭐",
                    
                    "래더 매치에서 실버 등급으로 승급했다.⭐",
                    "래더 매치에서 골드 등급으로 승급했다.⭐",
                    "한 곡에서 5,000 콤보 이상으로 클리어했다.⭐",
                    "100,000 콤보를 달성했다.",
                    "999,999 콤보를 달성했다.",
                    "누적 점수가 100,000,000점을 돌파했다.⭐",
                    "누적 점수가 200,000,000점을 돌파했다.⭐",
                    "누적 점수가 300,000,000점을 돌파했다.⭐",
                    "S랭크로 100회 클리어 했다.",
                    "오픈 매치에서 모두가 MAX COMBO로 클리어했다.⭐",
                    
                    "오픈 매치를 100회 플레이했다.",
                    "오픈 매치에서 스코어 부문 1등을 기록했다.⭐",
                    "오픈 매치에서 호스트 권한을 넘겨주었다.⭐",
                    "레벨 10을 달성했다.",
                    "레벨 50을 달성했다.",
                    "레벨 99를 달성했다.",
                    "정확하게 777 콤보로 클리어했다.⭐",
                    "한 곡에서 10,000 콤보 이상으로 클리어했다.⭐",
                    "처음으로 숨겨진 BGA를 발견했다.⭐",
                    "모든 숨겨진 BGA를 발견했다.⭐",
                    
                    "미션에서 A.I.를 상대로 승리했다.⭐",
                    "DJMAX RESPECT V의 모든 도전과제를 달성했다.⭐"]

rptv_caption = ["본편(리스펙트, 포터블1, 포터블2, 길티기어) 수록곡만 해당, 과제 달성 시점에서 자신이 해금한 곡만 클리어 하면 된다. 길티기어가 포함되는 이유는 무료로 제공되기 때문.",
                "", "", 
                "100레벨 달성 시 컬렉션에서 Dream it ~DJMAX RESPECT V credit~의 BGA를 볼 수 있으며, 이것을 감상하면 된다.",
                "대상: NB Ranger, NB Rangers -Returns-, NB POWER, NB RANGER - Virgin Force",
                "기어팩 DLC 포함. 기본 기어 수집 중에 개별 기어 DLC나 시리즈별 DLC를 구매한 다음에 게임을 실행해도 10개 이상 획득으로 인식하여 자동으로 달성된다. 또한 소녀전선과 CHUNITHM, 그리고 클리어 패스 시즌 1(온라인의 PG-mk2 기어)이 있는 현재는 기어가 총 46개이다.",
                "", "", "", "", 
                "중복 허용\n\nSC는 별도 난이도로 간주하여 카운트되지 않는다.",
                "중복 허용\n\nSC는 별도 난이도로 간주하여 카운트되지 않는다.",
                "중복 허용\n\nSC는 별도 난이도로 간주하여 카운트되지 않는다.",
                "중복 허용\n\nSC는 별도 난이도로 간주하여 카운트되지 않는다.",
                "중복 허용\n\nSC는 별도 난이도로 간주하여 카운트되지 않는다.",
                "중복 허용\n\nSC는 별도 난이도로 간주하여 카운트되지 않는다.",
                "",
                "중복 불가",
                "중복 불가",
                "",
                "달성 조건이 변경된 도전과제로, 변경 이전에는 AIR에서 코멘트를 작성하는 것이 조건이었다.",
                "자신이 가장 좋아하는 곡 = 자신이 가장 많이 플레이 한 곡. 해당하는 곡이 여러 곡이라면 그 중 하나만 플레이해도 달성된다. 오토플레이를 켜든 끄든 상관 없이 곡이 시작되자마자 달성된다.",
                "", "",
                "DLC 포함", "DLC 포함", "DLC 포함",
                "",
                "0점 동점은 불인정. 폭사하더라도 최소 1점은 얻어야 과제를 달성할 수 있다. 도전과제 특성상 중~하위권 티어에서는 일반적인 상황에서는 달성하기 어려우므로 플레이어들이 합의하에 첫 노트만 치고 비기는 방식으로 과제를 달성하기도 한다. AI와의 대전이 있는 미션에서 동점을 기록해도 달성된다.",
                "언랭크 봇전 5판을 통해 하위 랭크를 건너뛰고 상위 랭크로 배치되면 하위 랭크 도전과제도 같이 달성된다.",
                "언랭크 봇전 5판을 통해 하위 랭크를 건너뛰고 상위 랭크로 배치되면 하위 랭크 도전과제도 같이 달성된다.",
                "언랭크 봇전 5판을 통해 하위 랭크를 건너뛰고 상위 랭크로 배치되면 하위 랭크 도전과제도 같이 달성된다.",
                "달성 방법은 많지만 7레벨인 Always 4B HD를 풀콤보로 깨는 것이 가장 쉬운 방법 중 하나이다.",
                "",
                "",
                "중복 허용", "중복 허용", "중복 허용", "중복 허용",
                "6인 이하 방에서는 달성할 수 없다.",
                "",
                "6인 이하 방에서는 달성할 수 없다.",
                "방장 넘기기 이외의 경우로 방장이 바뀌었을 경우(게임 중 통신 오류, 방 나가기) 달성되지 않는다.",
                "", "", "",
                "맥스 콤보 777이 아니라 곡이 끝나는 시점에 777 콤보가 되어야 한다. 가장 쉬운 방법은 TECHNIKA 1 PACK이 있다면 Beyond the Future 4B MX을 맥스 콤보하는 것만으로 가능하다. TECHNIKA 1 PACK이 없다면 V EXTENSION PACK에 수록된 Move Yourself 4B MX를 피버를 끄고 플레이해서 첫번째 노트만 치지 않고 나머지는 노 미스로 플레이하는 것으로 가능하며, V EXTENSION PACK이 없다면 기본곡인 I want you ~반짝 반짝 Sunshine~ 4B HD를 피버를 끄고 11 COMBO → 3 BREAK → 이후 노 미스로 플레이해도 된다.",
                "대상: 통상곡 한정 시 Sad Machine 5B SC, POP/STARS 5B/6B/8B SC, NB RANGER - Virgin Force 6B SC, Ghost Voices 6B HD, Minimal Life 4B/5B SC. DLC를 포함하면 더 많다. 조건을 충족하는 곡 대부분이 SC 10렙을 상회하는 곡이라 난이도가 부담스럽다면 염라 ~Original Ver.~를 4B SC로 하면 수월하게 달성할 수 있다. 사실 6키 실력이 된다는 가정하에는 Ghost Voices로 더욱 쉽게 날먹할 수 있다. SC 2렙의 Blue Destination 4B SC로 더욱 날먹이 가능해졌다.",
                "대상: NB RANGER - Virgin Force, A Lie, Enemy Storm, Never Say, WhiteBlue, Out Law \n\n발견이기 때문에 맥스 콤보를 할 필요 없이 확인만 하면 되고, 프리스타일 외에 미션 모드에서 발견하는 경우에도 정상적으로 카운트된다.",
                "대상: NB RANGER - Virgin Force, A Lie, Enemy Storm, Never Say, WhiteBlue, Out Law \n\n발견이기 때문에 맥스 콤보를 할 필요 없이 확인만 하면 되고, 프리스타일 외에 미션 모드에서 발견하는 경우에도 정상적으로 카운트된다.",
                "본편 미션과 DLC 미션 상관 없이 AI와 대결하는 미션을 아무거나 클리어하면 된다. 트릴로지 DLC의 T-SIDE 미션 4의 ""Electronic License""가 AI 프로토타입이고 그 외의 미션은 전부 오리지널 AI이다.",
                "DLC 미포함"]

rptv = []
for i in range(len(load_images(rptv_dir))):
    rptv.append({"image": load_images(rptv_dir)[i], 
                "keyword": "RPTV", 
                "name": rptv_name[i], 
                "description": rptv_description[i],
                "checked": False,
                "caption": rptv_caption[i]})



##########################################################################################



ex1_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/2. V EXTENSION")
ex1_name = ["짤줍짤줍",
           "멈추지 않는 수집 욕구",
           "SC는 어쩔 수 없지",
           "신곡 감상평",
           "상상도 못한 정체",
           "DJMAX ACADEMY",
           "자신과의 싸움",
           "누나 나 죽어",
           "꿈어린"]
ex1_description = ["10장의 V EXTENSION 이미지를 획득했다.",
                  "3장의 V EXTENSION 플레이트를 획득했다.",
                  "V EXTENSION 곡의 SC 패턴을 MAX COMBO로 클리어했다.",
                  "AIR에서 V EXTENSION 곡에 대한 코멘트를 작성했다.⭐",
                  "Starlight Guitar 미션을 클리어했다.",
                  "V EXTENSION 곡을 모두 S랭크로 클리어했다.⭐",
                  "V EXTENSION 곡에서 50개의 패턴을 MAX COMBO로 클리어했다.⭐",
                  "Icy Blonde 미션을 클리어했다.",
                  "Dream it 기어와 노트를 장착한 상태로 Dream it을 MAX COMBO로 클리어했다."]

ex1_caption = ["", "", "",
               "V EXTENSION DLC를 소지하고 있지 않으면 조건을 만족해도 과제를 달성할 수 없다.",
               "",
               "난이도, 버튼 무관",
               "중복 불가",
               "", ""]

ex1 = []
for i in range(len(load_images(ex1_dir))):
    ex1.append({"image": load_images(ex1_dir)[i], 
                "keyword": "EX1", 
                "name": ex1_name[i], 
                "description": ex1_description[i],
                "checked": False,
                "caption": ex1_caption[i]})



##########################################################################################




tr_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/3. TRILOGY")
tr_name = ["당신은 대체…",
            "제 여자친구가 확실합니다!",
            "수호천사",
            "뉴 스킨 작렬…!",
            "다음 이벤트도 기대해주세요",
            "대신푸우른USB를드리겠습니다",
            "나올수도 있고 안나올수도 있습니다"]
tr_description = ["TRILOGY 곡을 모두 S랭크로 클리어했다.⭐",
                  "오픈 매치에서 모두가 Someday를 MAX COMBO로 클리어했다.⭐",
                  "오픈 매치에서 My Jealousy를 MAX COMBO로 클리어했다.⭐",
                  "TRILOGY 전용 UI 스킨을 적용했다.",
                  "DJMAX RESPECT U 미션을 클리어했다.",
                  "TRILOGY 곡을 내가 좋아하는 곡 순위권에 등극시켰다.",
                  "TRILOGY 곡 중 숨겨진 BGA를 발견했다.⭐"]

tr_caption = ["난이도, 버튼 무관",
              "6인 이하 방에서는 달성할 수 없다.",
              "인원 제한 없음",
              "", "", "",
              "대상: STOP"]

tr = []
for i in range(len(load_images(tr_dir))):
    tr.append({"image": load_images(tr_dir)[i], 
                "keyword": "TR", 
                "name": tr_name[i], 
                "description": tr_description[i],
                "checked": False,
                "caption": tr_caption[i]})



##########################################################################################



clsq_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/4. CLAZZIQUAI")
clsq_name = ["클럽 투어에 오신것을 환영합니다",
             "CE Style",
             "Metro Project",
             "역시 프로 리듬게이머는 달라",
             "클리어 위주로 갑시다",
             "DJ Clazzi",
             "Go Back From the Top",
             "DJMAX ARTIST TEAM"]
clsq_description = ["Electronic City를 클리어했다.",
                    "Lover(CE Style), Y(CE Style)을 MAX COMBO로 클리어했다.⭐",
                    "오픈 매치에서 Clazziquai Edition 곡을 모두가 다른 패턴으로 선택하여 클리어했다.⭐",
                    "Clazziquai Edition 곡 중 한 곡의 모든 패턴을 MAX COMBO로 클리어했다.⭐",
                    "Clazziquai Edition 곡을 모두 S랭크로 클리어했다.⭐",
                    "Clazziquai의 곡을 모두 MAX COMBO로 클리어했다.⭐",
                    "Clazziquai Edition 곡 중 숨겨진 BGA를 발견했다.⭐",
                    "DJMAX TOURNAMENT LIVE 미션을 클리어했다."]

clsq_caption = ["",
                "난이도, 버튼 무관",
                "인원 제한 없음",
                "모든 버튼의 모든 난이도를 말하는 것이다. 정 어렵다면 Urban Night로 하자. 패턴이 총 8개이며 전키 통틀어 8이 가장 높은 난이도이다.",
                "난이도, 버튼 무관",
                "난이도, 버튼 무관\n\n대상: 내게로 와, Color, Creator, Electronics, Flea, Freedom, Love Mode, The Night Stage",
                "대상: First Kiss",
                ""]

clsq = []
for i in range(len(load_images(clsq_dir))):
    clsq.append({"image": load_images(clsq_dir)[i], 
                "keyword": "CLQI", 
                "name": clsq_name[i], 
                "description": clsq_description[i],
                "checked": False,
                "caption": clsq_caption[i]})



##########################################################################################



blsq_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/5. BLACK SQUARE")
blsq_name = ["정말 BLACK SQUARE 곡으로 할거야?",
             "BLACK SQUARE에 도전하시겠습니까?",
             "Get Down의 그녀",
             "Fermion으로 하겠어요",
             "REDESIGN?!",
             "BS Style",
             "페일 위주로 갑니다",
             "빨리 틀어요",
             "DJMAX 시리즈 중에서 최강 난이도"]
blsq_description = ["오픈 매치에서 BLACK SQUARE 곡을 모두가 같은 패턴으로 선택하여 MAX COMBO로 클리어했다.⭐",
                    "BLACK SQUARE 곡의 100가지 패턴을 MAX COMBO로 클리어했다.⭐",
                    "First Kiss 기어를 사용하여 다나를 10번 확인했다.⭐",
                    "Fermion을 체력 게이지 20% 이하만 남겨두고 클리어했다.⭐",
                    "RD Colosseum 미션을 클리어했다.",
                    "Lover(BS Style), Y(BS Style)을 MAX COMBO로 클리어했다.⭐",
                    "BLACK SQUARE 곡을 모두 S랭크로 클리어했다.⭐",
                    "BLACK SQUARE 수록곡 중 한 곡을 연속으로 10회 클리어했다.⭐",
                    "BLACK SQUARE의 SC 패턴을 플레이했다.⭐"]

blsq_caption = ["인원 제한 없음\n\n단 Metro Project와는 다르게 버튼 수와 난이도가 모두 같아야 한다.",
                "중복 불가\n\n내용과는 다르게 클리어만 해도 인정된다.",
                "First Kiss의 기어를 사용하면 등장인물 4명이 랜덤으로 출현한다. 좌우에서 같은 캐릭터가 두 번 출현하기에 실질적으로는 5번만 확인하면 된다. 확인하는 동안에는 곡을 완주할 필요 없지만, 확인하고 나면 곡을 한 번 완주해야 한다.",
                "연속으로 13개를 틀려야 폭사하므로, 마지막에 11~12개 정도를 놓치면 된다. 패치 이후로 노멀, 하드난이도는 노트를 하나도 치지 않아도 클리어가 되기 때문에 프리스타일에서 선곡한 후 그냥 끝날때까지 놔둬도 된다.",
                "",
                "난이도, 버튼 무관",
                "난이도, 버튼 무관",
                "한 패턴만 붙잡고 있을 필요는 없다. 어느 한 곡을 폭사하지 않고 10회 플레이하면 달성할 수 있다.",
                "클리어 여부 무관\n\nBGA를 켜고 플레이해야 한다.\n\n원래는 난이도가 15인 SC 패턴을 플레이하는 것이 조건이었으나 시즌 6 SC 난이도 체계가 개편된 이후 조건도 같이 수정되었다."]

blsq = []
for i in range(len(load_images(blsq_dir))):
    blsq.append({"image": load_images(blsq_dir)[i], 
                "keyword": "BLSQ", 
                "name": blsq_name[i], 
                "description": blsq_description[i],
                "checked": False,
                "caption": blsq_caption[i]})



##########################################################################################



tech_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/6. TECHNIKA")
tech_name = ["플래티넘 크루",
             "ONLY FOR ARCADE",
             "First Step Set 졸업",
             "Stylish eSper Shooting Sports",
             "완벽주의",
             "인성 문제있어?",
             "Rolling On the Screen",
             "이제 팀웍이 보이네",
             "댓글댓글단다 댓글댓글단다",
             "암튼 레어 카드"]
tech_description = ["TECHNIKA 곡을 모두 S랭크로 클리어했다.⭐",
                    "숨겨진 패턴을 MAX COMBO로 클리어했다.⭐",
                    "First step 미션에서 플레이 할 수 있는 모든 곡을 클리어했다.⭐",
                    "COLLECTION 모드에서 SuperSonic의 뮤직 비디오를 감상했다.",
                    "Mr.Perfect 미션을 클리어했다.⭐",
                    "5가지의 TECHNIKA 플레이트를 획득했다.",
                    "Technical Mixing에서 할 수 있는 모든 패턴을 플레이했다.⭐",
                    "오픈 매치에서 TECHNIKA 곡으로 7명 모두 MAX COMBO를 달성했다.⭐",
                    "추장의 장비를 갖추고 SON OF SUN을 MAX COMBO로 클리어했다.⭐",
                    "TECHNIKA 곡 중 숨겨진 BGA를 발견했다.⭐"]

tech_caption = ["난이도, 버튼 무관",
                "Technical Mixing에서 마지막 곡으로 나오는 TB패턴을 MAX COMBO로 클리어 하면 된다. 미션 6개 중 아래로 갈수록 더 어려운 곡이 나오니 1번 미션인 First step으로 도전하는 것을 권장한다.",
                "2번째 곡을 클리어 한 시점에서 누적 콤보 수에 따라 나오는 곡이 달라진다. 홀수일 경우 Only for you, 짝수일 경우 I want You가 등장한다.\n\n3번째 스테이지의 곡은 반드시 같은 기기에서 둘 다 플레이해야 한다. 예컨대 한 컴퓨터에서 Only for you를 플레이하고 다른 컴퓨터에서 I want You를 플레이하면 도전과제가 달성되지 않는다.",
                "",
                "PS4판과는 달리 클리어를 해야 달성할 수 있다.",
                "",
                "클리어 여부 무관",
                "6인 이하 방에서는 달성할 수 없다.\n\n난이도, 버튼 무관",
                "추장의 장비 = SON OF SUN 기어와 노트.",
                "대상: Thor"]

tech = []
for i in range(len(load_images(tech_dir))):
    tech.append({"image": load_images(tech_dir)[i], 
                "keyword": "TECH", 
                "name": tech_name[i], 
                "description": tech_description[i],
                "checked": False,
                "caption": tech_caption[i]})



##########################################################################################



tech2_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/7. TECHNIKA 2")
tech2_name = ["팝 마스터가 될거야",
              "선생님도 결국 재능이었군요",
              "CREW RACE",
              "혼자밖에 생각하지 않아",
              "죽음의 무도",
              "테크니카 붐은 온다",
              "RAINBOW MAX",
              "언제까지 피버를 안 쓰실 겁니까"]
tech2_description = ["TECHNIKA 2 곡을 모두 S랭크로 클리어했다.⭐",
                     "STAR MIXING 미션을 전부 클리어했다.",
                     "TECHNIKA 2 UI 스킨을 적용했다.",
                     "오픈 매치에서 TECHNIKA 2 곡으로 TOP SCORE, RATE, COMBO를 동시에 기록했다.⭐",
                     "D2 기어와 노트를 장착한 상태로 D2를 2번 클리어했다.⭐",
                     "TECHNIKA 2 홍보 영상을 감상했다.⭐",
                     "새로운 TB 패턴을 MAX COMBO로 클리어했다.",
                     "새로운 TB 패턴에서 피버를 3회 발동 후 클리어했다."]

tech2_caption = ["난이도, 버튼 무관",
                 "", "",
                 "인원 제한 없음",
                 "난이도, 버튼 무관",
                 "테크니카 2 미션 1-6 ""Signiture Collection""을 클리어할 시 볼 수 있다.",
                 "", ""]

tech2 = []
for i in range(len(load_images(tech2_dir))):
    tech2.append({"image": load_images(tech2_dir)[i], 
                "keyword": "TECH2", 
                "name": tech2_name[i], 
                "description": tech2_description[i],
                "checked": False,
                "caption": tech2_caption[i]})



##########################################################################################



tech3_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/8. TECHNIKA 3")
tech3_name = ["CREW CHALLENGE",
             "1일 1맥",
             "와! 신곡!",
             "PRETTY PIC BESIDE PRETTY PIC",
             "절대 미션해",
             "싹쓰리",
             "펀하고 쿨하고 섹시하게",
             "맛집 탐험"]
tech3_description = ["TECHNIKA 3 곡을 모두 S랭크로 클리어했다.⭐",
                    "TECHNIKA 3 곡에서 10개의 패턴을 MAX COMBO로 클리어했다.⭐",
                    "ALiCE를 MAX COMBO로 클리어했다.⭐",
                    "10장의 TECHNIKA 3 이미지를 획득했다.",
                    "POP MIXING 미션을 전부 플레이했다.⭐",
                    "오픈 매치에서 TECHNIKA 3 곡으로 TOP SCORE, RATE, COMBO를 동시에 기록했다.⭐",
                    "5가지의 TECHNIKA 3 플레이트를 획득했다.⭐",
                    "TECHNIKA 3 곡에서 SC 패턴을 MAX COMBO로 클리어했다."]

tech3_caption = ["난이도, 버튼 무관",
                 "중복 허용",
                 "난이도, 버튼 무관",
                 "",
                 "클리어 여부 무관",
                 "인원 제한 없음",
                 "한 곡에서 여러 플레이트를 얻으면 하나만 인정된다. 한 곡을 10회 플레이하여 첫 플레이트를 얻던가, TECHNIKA 3 팩의 미션을 클리어하여 얻으면 된다.",
                 ""]

tech3 = []
for i in range(len(load_images(tech3_dir))):
    tech3.append({"image": load_images(tech3_dir)[i], 
                "keyword": "TECH3", 
                "name": tech3_name[i], 
                "description": tech3_description[i],
                "checked": False,
                "caption": tech3_caption[i]})



##########################################################################################



link_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/9. LINK DISC")
link_name = ["링크 디스크",
             "디스크 조각",
             "이제 최종 단계에 들어선거야"]
link_description = ["링크 디스크 미션을 개방했다.⭐",
                    "링크 디스크를 통해 획득할 수 있는 모든 곡을 MAX COMBO로 클리어했다.⭐",
                    "The Others 미션을 클리어했다."]

link_caption = ["클래지콰이 에디션, 블랙 스퀘어, 테크니카 1 미션팩의 모든 미션(총 36개)을 클리어하면 된다.",
                "난이도, 버튼 무관\n\n대상: Here in the Moment ~Extended Mix~, SON OF SUN ~Extended Mix~, Airwave ~Extended Mix~\n\nDLC만 소유하고 있다면 곡은 자동으로 해금된다.",
                ""]

link = []
for i in range(len(load_images(link_dir))):
    link.append({"image": load_images(link_dir)[i], 
                "keyword": "LINK", 
                "name": link_name[i], 
                "description": link_description[i],
                "checked": False,
                "caption": link_caption[i]})



##########################################################################################



ptb3_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/10. PORTABLE 3")
ptb3_name = ["MADE BY MUSICIANS",
             "REmixVOLUTION",
             "Now or never",
             "Put Your Hanz Up!",
             "REMIX SYSTEM",
             "역주행 모드",
             "롤린 롤린",
             "안 죄송합니다"]
ptb3_description = ["PORTABLE 3 곡을 모두 S랭크로 클리어했다.⭐",
                    "PORTABLE 3의 모든 REMIX 곡을 클리어 했다.⭐",
                    "PORTABLE 3 기어를 장착하고 PORTABLE 3 곡을 MAX COMBO로 클리어 했다.⭐",
                    "Hanz up! 메이킹 영상을 시청했다.⭐",
                    "새로운 리믹스 모드에서 MAX COMBO를 달성했다.⭐",
                    "Rewind 미션을 클리어했다.",
                    "10장의 PORTABLE 3 이미지를 획득했다.",
                    "오픈 매치에서 PORTABLE 3 곡을 플레이하여 모두의 최대 콤보수 합이 30000콤보 이상을 기록했다."]

ptb3_caption = ["난이도, 버튼 무관",
                "난이도, 버튼 무관",
                "난이도, 버튼 무관\n\n꽤 많은 사람들이 헷갈리는 부분인데, 포3 DLC를 구입하면 얻는 Hanz Up 기어가 아니라 PORTABLE 3 기어다.",
                "DJMAX PORTABLE 3의 미션 2-2 Put yout hands up을 클리어 시 얻을 수 있다. 영상 제목은 Making of Hanz up!이다. H에서 찾지 말고 M까지 가야 한다.",
                "Workstation Set에서 플레이할 미션을 골라 한 곡만 올콤하고 나머지는 올콤하지 않아도 미션 클리어 시 자동으로 달성된다.",
                "", "", ""]

ptb3 = []
for i in range(len(load_images(ptb3_dir))):
    ptb3.append({"image": load_images(ptb3_dir)[i], 
                "keyword": "PTB3", 
                "name": ptb3_name[i], 
                "description": ptb3_description[i],
                "checked": False,
                "caption": ptb3_caption[i]})



##########################################################################################




ex2_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/11. V EXTENSION 2")
ex2_name = ["VVS",
            "겁은 하나도 안나지",
            "NEXT LEVEL",
            "어 느새 부터 디맥은 ATTACK",
            "불 좀 꺼줄래? 내 기어 좀 보게",
            "알로록 달로록",
            "그건 제 잔상입니다만",
            "달의하루",
            "Multi-Verse",
            "인형사"]
ex2_description = ["V EXTENSION 2 곡을 모두 S랭크로 클리어했다.⭐",
                   "VERSUS 미션을 클리어했다.⭐",
                   "V EXTENSION 2 곡을 NORMAL - HARD - MAXIMUM - SC 난이도 순으로 클리어했다.⭐",
                   "Arcade Love의 SC 패턴을 플레이했다.⭐",
                   "FEVER OFF 설정으로 V EX 2 기어를 장착하고 임의의 곡을 클리어했다.⭐",
                   "V EXTENSION 2 플레이트 중 하나를 장착했다.",
                   "V EXTENSION 2 곡 중에서 숨겨진 BGA를 발견했다.⭐",
                   "V LINK를 통해 획득한 곡을 MAX COMBO로 클리어했다.⭐",
                   "V LINK 미션을 개방했다.⭐",
                   "V LINK 미션 DoLLS를 클리어했다.⭐"]

ex2_caption = ["난이도, 버튼 무관",
               "6개 미션 모두 클리어해야 한다.",
               "너로피어오라 ~Original Ver.~ 은 포함되지 않는다. EXTENSION 2 곡 내에서 지정된 순서를 지키기만 한다면 곡이나 버튼의 종류는 무관하다. 예를 들어, Red Eyes 4B NORMAL - Sweet On You 4B HARD - Arcade Love 6B MAXIMUM - Voyage 5B SC여도 도전과제를 클리어할 수 있다.\n\n도전과제 설명 상으로는 V EXTENSION 2 곡이라고 하지만 V EXTENSION 4 곡으로도 가능하며, 이를 이용해 2와 4 DLC를 동시에 구매한 상태에서 V EXTENSION 4 곡으로 조건을 만족해 사황의 힘 도전과제와 동시에 완료 가능했으나 6월 22일 패치로 수정되었다.",
               "어느 패턴 하나만 플레이를 시작해도 달성된다.",
               "난이도, 버튼 무관",
               "",
               "대상: Chrysanthemum",
               "난이도, 버튼 무관",
               "V EXTENSION 곡과 V EXTENSION 2 곡 전부를 MAX COMBO로 클리어하면 개방된다. 난이도, 버튼의 종류는 무관하다.",
               "아이콘 이미지의 캐릭터는 엘페르트 밸런타인이다."]

ex2 = []
for i in range(len(load_images(ex2_dir))):
    ex2.append({"image": load_images(ex2_dir)[i], 
                "keyword": "EX2", 
                "name": ex2_name[i], 
                "description": ex2_description[i],
                "checked": False,
                "caption": ex2_caption[i]})



##########################################################################################




tnq_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/12. TECHNIKA TUNE & Q")
tnq_name = ["GRAND MASTER of TUNE",
            "Q Lover",
            "Owner of TUNE Q Gallery",
            "T to the TUNE to the Q",
            "튠큐 어서오고",
            "FEVER...FEVER...FEVER!!",
            "Never Ending TECHNIKA"]
tnq_description = ["TECHNIKA TUNE 곡을 모두 MAX COMBO로 클리어했다.⭐",
                   "TECHNIKA Q 곡을 모두 S랭크로 클리어했다.⭐",
                   "모든 TECHNIKA TUNE Q DLC 이미지를 획득했다.⭐",
                   "TECHNIKA TUNE Q 플레이트를 장착했다.",
                   "래더 매치에서 TECHNIKA TUNE Q 곡을 플레이했다.⭐",
                   "TECHNIKA TUNE Q TB 패턴에서 피버를 3회 발동 후 클리어했다.",
                   "Never Ending TECHNIKA의 TB 패턴을 클리어했다.⭐"]

tnq_caption = ["난이도, 버튼 무관",
               "난이도, 버튼 무관",
               "Love☆panic, Mukilteo Beach, Retention, Silent Clarity, VORTEX, Shining My Boy 각 3개씩(각 5회 클리어 시 전부 획득), Never Ending TECHNIKA 6개(9회 클리어 시 전부 획득)",
               "",
               "난이도, 버튼 무관",
               "",
               "미션 성공 여부와 무관하게 클리어만 하면 된다."]

tnq = []
for i in range(len(load_images(tnq_dir))):
    tnq.append({"image": load_images(tnq_dir)[i], 
                "keyword": "T&Q", 
                "name": tnq_name[i], 
                "description": tnq_description[i],
                "checked": False,
                "caption": tnq_caption[i]})



##########################################################################################



ex3_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/13. V EXTENSION 3")
ex3_name = ["DO 3XTENSION", 
            "Tic! Tac! Toe!",
            "디맥의 홀더",
            "엔비 타이탄 더 브로큰 하트",
            "자고로 맥콤이란",
            "운명, 흥망돌, 빡빡이",
            "가보자고",
            "ONE & ONLY"]
ex3_description = ["V EXTENSION 3 곡을 모두 MAX COMBO로 클리어했다.⭐",
                   "Tic! Tac! Toe!의 각각 다른 패턴을 S랭크 이상으로 9회 클리어했다.",
                   "V EXTENSION 3 UI 스킨을 적용했다.",
                   "COLLECTION 모드에서 NB RANGER - Virgin Force, NB RANGER 운명의 Destiny 뮤직 비디오를 연속해서 감상했다.⭐",
                   "V EXTENSION 3 곡을 BREAK 1개로 클리어했다.⭐",
                   "V EXTENSION 3 곡 중에서 숨겨진 BGA를 모두 발견했다.⭐",
                   "V EXTENSION 3 곡을 8500콤보 이상으로 클리어했다.⭐",
                   "오픈 팀 매치에서 V EXTENSION 3 곡으로 승리했다.⭐"]

ex3_caption = ["난이도, 버튼 무관",
               "", "",
               "이전에 Virgin Force 뮤직 비디오를 끝까지 감상한 적이 있다면, Virgin Force 뮤직 비디오를 재생하고서 바로 끈 다음, 곧바로 운명의 Destiny 뮤직 비디오만 끝까지 감상해도 도전과제가 달성된다. 히든 BGA로는 달성되지 않는다.\n\n도전과제가 얻어지지 않는 버그가 있다. [%userprofile%\\AppData\\LocalLow\\NEOWIZ\\DJMAX RESPECT V] 해당 경로의 폴더를 통째로 지우고 뮤직비디오를 다시 보면 된다. 다만 개인이 했던 설정이나 곡 즐겨찾기 등이 모두 날아가기 때문에 백업을 하고 진행하는 것을 추천.".replace('%', '%%'),
               "난이도, 버튼 무관",
               "본래 히든 BGA 발견 도전과제는 미션 모드에서 발견하는 것도 카운트되지만, V EXTENSION 3 미션 1-3 Hidden Catch로는 이 도전과제를 달성할 수 없다.(V EXTENSION 3 곡 중 히든 BGA가 수록된 3곡을 대상으로 하고, 미션 플레이시 반드시 히든 BGA만 재생되는 미션이다.) 해당곡 NB RANGER 운명의 Destiny 운명, Tic! Tac! Toe! 흥망돌, Fundamental 빡빡이",
               "추천곡 : Set me free 4B SC. 맥스 콤보시 약 8690콤보가 나온다.",
               "모두가 옵저버로 플레이하면 전원 승리 처리된다."]

ex3 = []
for i in range(len(load_images(ex3_dir))):
    ex3.append({"image": load_images(ex3_dir)[i], 
                "keyword": "EX3", 
                "name": ex3_name[i], 
                "description": ex3_description[i],
                "checked": False,
                "caption": ex3_caption[i]})



##########################################################################################




ex4_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/14. V EXTENSION 4")
ex4_name = ["BEYOND THE EXTENSIO""IV""", 
            "Lies of Nightmare",
            "사황의 힘",
            "REUNION",
            "Ignition Control",
            "악몽은 끝나지 않아",
            "그게 무슨 말이니",
            "불친절한 행복과 다정한 상처를 노래해요",
            "FINALIST",
            "OVER THE EXTENSIO""IV"""]
ex4_description = ["V EXTENSION 4 곡을 모두 S랭크로 클리어했다.⭐",
                   "LUV, Vertical Eclipse, DIE IN 3곡을 각각 다른 패턴으로 4회씩 클리어했다.",
                   "V EXTENSION 4 곡을 NORMAL - HARD - MAXIMUM - SC 순으로 클리어했다.⭐",
                   "Deadly Bomber, Vertical Eclipse를 차례대로 S 랭크로 클리어했다.⭐",
                   "COLLECTION 모드에서 LUV, Vertical Eclipse, DIE IN 뮤직 비디오를 연속해서 감상했다.⭐",
                   "모든 V EXTENSION 4 DLC 이미지를 획득했다.⭐",
                   "오픈 매치에서 V EXTENSION 4 곡을 플레이하여 MAX COMBO를 달성했다.⭐",
                   "V LINK 2를 통해 획득한 곡을 MAX COMBO로 클리어했다.⭐",
                   "V LINK 2 미션을 개방했다.⭐",
                   "V LINK 2 미션 conveyor belt를 클리어했다."]

ex4_caption = ["난이도, 버튼 무관",
               "",
               "도전과제 설명 상으로는 V EXTENSION 4 곡이라고 하지만 V EXTENSION 2 곡으로도 가능하며, 이를 이용해 2와 4 DLC를 동시에 구매한 상태에서 V EXTENSION 2 곡으로 조건을 만족해 NEXT LEVEL 도전과제와 동시에 완료 가능했으나 6월 22일 패치로 수정되었다.",
               "난이도, 버튼 무관",
               "각 뮤직 비디오를 따로 들으면 인정되지 않으며, COLLECTION 모드에서 해당되는 3개의 뮤직 비디오로 리스트를 따로 만들어야 한다.",
               "총 32장이다. (DIE IN 13장 / Hell'o 6장 / Deadly Bomber, Vertical Eclipse 각 3장 / Gloxinia, Weaponize 각 2장 / 너에게로 갈래, Love.Game.Money, LUV 각 1장)",
               "난이도, 버튼 무관",
               "난이도, 버튼 무관",
               "V EXTENSION 3와 V EXTENSION 4의 모든 곡을 MAX COMBO로 클리어하면 된다.",
               ""]

ex4 = []
for i in range(len(load_images(ex4_dir))):
    ex4.append({"image": load_images(ex4_dir)[i], 
                "keyword": "EX4", 
                "name": ex4_name[i], 
                "description": ex4_description[i],
                "checked": False,
                "caption": ex4_caption[i]})



##########################################################################################



ex5_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/15. V EXTENSION 5")
ex5_name = ["하하하! 유저야, 또 해냈구나!", 
            "필요한 만큼은 보여 줬다.",
            "인벤토리 안에 놓고 가 주세요.",
            "그대들 어떻게 시작할 것인가",
            "다인 시대의 끝이 도래했다.",
            "스킨의 멋짐을 모르는 당신은 불쌍해요.",
            "해냈다! 해냈어!"]
ex5_description = ["V EXTENSION 5 모든 곡을 S랭크로 클리어했다.⭐",
                   "25개의 V EXTENSION 5 이미지를 획득했다.⭐",
                   "20개의 V EXTENSION 5 플레이트를 획득했다.",
                   "'V EXTENSION 5 UI' 스킨을 적용했다.",
                   "COLLECTION 모드에서 'Peace Comes At a Price'의 BGA를 감상했다.",
                   "V EX 5 기어와 노트를 장착하고 'glory MAX'를 클리어했다.⭐",
                   "B O n u S 미션을 클리어했다."]

ex5_caption = ["난이도, 버튼 무관",
               "ECiLA 6개 / S.A.V.E 5개 / Rhapsody for The VEndentta, 별빛너머 각 3개 / Accelerate, Carrot Carrot, Shining Light 각 2개 / Critical Point, Inside the Light 각 1개",
               "", "", "",
               "난이도, 버튼 무관",
               ""]

ex5 = []
for i in range(len(load_images(ex5_dir))):
    ex5.append({"image": load_images(ex5_dir)[i], 
                "keyword": "EX5", 
                "name": ex5_name[i], 
                "description": ex5_description[i],
                "checked": False,
                "caption": ex5_caption[i]})



##########################################################################################



groov_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/1. GROOVE COASTER")
groov_name = ["AD-LIB",
              "Got more plate?",
              "미안하다 이거 시켜보려고 안보이게 해놨다"]
groov_description = ["Groove Coaster 곡을 모두 S랭크로 클리어했다.⭐",
                     "DJMAX 캐릭터가 픽셀로 표현된 플레이트를 모두 획득했다.⭐",
                     "Groove Prayer 5B HD 패턴을 BLIND로 클리어했다.⭐"]

groov_caption = ["난이도, 버튼 무관",
                 "대상: Good Night, Bad Luck., Marry me, Nightmare, ouroboros -twin stroke of the end- 각각 10회씩 클리어",
                 "Groove Coaster 채보를 그대로 집어넣었다. HIT, HOLD, SLIDE, SLIDE HOLD 노트는 3번 라인, CRITICAL, DUAL HOLD 노트는 1번, 5번 라인, SCRATCH 노트는 사이드 트랙에 배정되어 있다. BGA로 노트 타이밍을 추측할 수 있으며 투명도 100%, BGA 최대 밝기로 해놓고 플레이하면 좀 더 수월하게 클리어 가능하다. 오픈 매치에서는 상대방이 설정한 페이더나 카오스 옵션이 대부분 적용되지 않기 때문에 상대방 노트를 보면서 플레이 하면 좀더 쉽게 클리어 할 수 있다. 정 달성이 어렵다면 오픈매치에서 블라인드 설정만 해놓고 폭사가 안되는 걸 이용하여 방치해도 달성된다. 하지만 시즌 패치로 HD 패턴까지는 게이지가 떨어져도 완주가 가능하게 바뀌면서, 이제는 BLIND만 걸어두면 아무것도 하지 않아도 자동으로 클리어된다."]

groov = []
for i in range(len(load_images(groov_dir))):
    groov.append({"image": load_images(groov_dir)[i], 
                "keyword": "GRUV", 
                "name": groov_name[i], 
                "description": groov_description[i],
                "checked": False,
                "caption": groov_caption[i]})




##########################################################################################



Cytus_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/2. Cytus")
Cytus_name = ["Can you hear me?",
              "모든 사건의 흑막",
              "Aesir",
              "Million Master",
              "CAPSO!"]
Cytus_description = ["CYTUS 전용 UI 스킨을 적용했다.",
                     "Entrance를 MAX COMBO로 클리어했다.⭐",
                     "L을 MAX COMBO로 클리어했다.⭐",
                     "CYTUS 곡 중 3개의 패턴을 PERFECT PLAY로 클리어했다.⭐",
                     "5가지의 CYTUS 플레이트를 획득했다.⭐"]

Cytus_caption = ["",
                 "난이도, 버튼 무관",
                 "난이도, 버튼 무관",
                 "난이도, 버튼 무관",
                 "대상: AXION, CODE NAME : ZERO, conflict, Entrance, L, Les Parfums de L'Amour, Mammal, Ververg"]

Cytus = []
for i in range(len(load_images(Cytus_dir))):
    Cytus.append({"image": load_images(Cytus_dir)[i], 
                "keyword": "Cytus", 
                "name": Cytus_name[i], 
                "description": Cytus_description[i],
                "checked": False,
                "caption": Cytus_caption[i]})



##########################################################################################



deemo_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/3. DEEMO")
deemo_name = ["소녀",
              "Deemo",
              "가면을 쓴 여자아이",
              "영혼"]
deemo_description = ["DEEMO 곡에서 처음으로 클리어에 실패했다.",
                     "DEEMO 곡에서 42개의 패턴을 클리어했다.",
                     "10가지의 DEEMO 플레이트를 획득했다.",
                     "DEEMO 기어와 노트를 장착한 상태로 ANiMA를 클리어했다.⭐"]

deemo_caption = ["", "", "", 
                 "난이도, 버튼 무관"]

deemo = []
for i in range(len(load_images(deemo_dir))):
    deemo.append({"image": load_images(deemo_dir)[i], 
                "keyword": "DEEMO", 
                "name": deemo_name[i], 
                "description": deemo_description[i],
                "checked": False,
                "caption": deemo_caption[i]})
    


##########################################################################################



glfr_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/4. 소녀전선")
glfr_name = ["FRONTLINE",
              "404 Not Found",
              "그리폰&크루거",
              "철혈공조공단",
              "기지 귀환"]
glfr_description = ["Frontline을 MAX COMBO로 클리어했다.⭐",
                     "404 Not Found 소대의 플레이트를 모두 획득했다.",
                     "Anti Rain의 플레이트를 획득했다.",
                     "철혈의 모든 전술 인형들과 조우했다.⭐",
                     "두 진영의 모든 전술 인형들과 조우했다.⭐"]

glfr_caption = ["난이도, 버튼 무관",
                "", "",
                "S.F. Girls 기어를 끼고 각 전술인형을 조우한 후 곡을 한 번 완주하면 된다. 총 6쌍이며, 6쌍을 조우하는 동안에는 곡을 클리어하지 않아도 된다.",
                "S.F. Girls 및 G.K. Girls 기어를 끼고 각각의 인형셋을 모두 봐야한다. AIR에서 오토로 돌리든 한번 보고 나가든 카운트는 되는 듯 하나, 모든 인형 조우 후에는 곡을 한번이라도 클리어를 해야 업적이 달성된다. G.K. Girls 기어에서는 같은 인형이라도 일반/중상이 따로 존재하지만, 둘 중 하나라도 보면 해당 인형을 조우한 것으로 친다.\n\nG.K. Girls 기어에서 나오는 총 경우의 수는 10개이다. (SPAS-12 & SAT8), (AK-12 & AN-94), (스프링필드 & WA2000), (M4A1 & M16A1), (M4 SOPMOD II & ST AR-15), (G11 & HK416), (썬더 & M950A), (M4A1 & ST AR-15), (PKP & 네게브), (UMP9 & UMP45)"]

glfr = []
for i in range(len(load_images(glfr_dir))):
    glfr.append({"image": load_images(glfr_dir)[i], 
                "keyword": "GLFR", 
                "name": glfr_name[i], 
                "description": glfr_description[i],
                "checked": False,
                "caption": glfr_caption[i]})



##########################################################################################



chu_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/5. CHUNITHM")
chu_name = ["츄니즘 퀘스트",
             "WORLD`S END",
             "츄니펭귄",
             "Over Power",
             "스킬 발동"]
chu_description = ["CHUNITHM 곡을 모두 MAX COMBO로 클리어했다.⭐",
                    "CHUNITHM 곡 중에서 난이도 15의 패턴을 플레이했다.⭐",
                    "CHUNITHM 플레이트를 장착했다.",
                    "CHUNITHM 곡을 9000콤보 이상으로 클리어했다.⭐",
                    "CHUNITHM 곡 플레이 중에 FEVER를 30회 사용.⭐"]

chu_caption = ["난이도, 버튼 무관",
               "클리어 여부 무관\n\nBGA를 켜고 플레이해야 한다.\n\n대상곡: Trrricksters!! 4B MX, The wheel to the right 4B MX, Cyberozar 4B/6B/8B MX를 제외한 CHUNITHM 콜라보레이션 곡의 모든 MX/SC 패턴.",
               "",
               "대상 패턴: Cyberozar 6B SC / Garakuta Doll Play 8B SC / Ikazuchi 5B MX, 5B SC, 6B MX, 6B SC, 8B MX, 8B SC / Ray Tuning 4B SC, 6B HD, 6B SC, 8B HD / The wheel to the right 6B SC, 8B MX / Trrricksters!! 4B SC, 6B SC, 8B MX, 8B SC\n\n그나마 쉬운 방법이 Ray Tuning 6B HD를 MAX COMBO하는 것인데 6버튼 지력이 딸릴 경우 대안이 SC 영역으로 넘어가는 Ray Tuning 4B SC이기 때문에 6버튼에 익숙해지지 않으면 도전과제 달성이 심히 까다로워진다.",
               "대상곡: 아래 표 참조. 자동피버를 켜고 Over Power 대상곡과 겹치는 곡을 맥스콤보에 근접할 경우 두 과제가 동시에 달성된다.\n\n Cyberozar 5B:SC/8B:MX\nGarakuta Doll Play 6B:SC/8B:SC\nIkazuchi 5B:MX,SC/6B:MX,SC/8B:MX,SC\nRay Tuning 6B:HD/8B:HD\nThe wheel to the right 5B:SC/6B:MX,SC/8B:MX\nTrrricksters!! 4B:SC/6B:MX,SC/8B:MX,SC"]

chu = []
for i in range(len(load_images(chu_dir))):
    chu.append({"image": load_images(chu_dir)[i], 
                "keyword": "CHU", 
                "name": chu_name[i], 
                "description": chu_description[i],
                "checked": False,
                "caption": chu_caption[i]})
    



##########################################################################################



esti_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/6. ESTimate")
esti_name = ["ESTINATION",
             "음유시인",
             "시티팝",
             "꽃에 진심인 편",
             "우주 대스타"]
esti_description = ["OBLIVION, OBLIVION ~Rockin' Night Style~, Obelisque를 차례대로 클리어했다.⭐",
                    "SIN, SIN ~The Last Scene~, HELIX를 차례대로 클리어했다.⭐",
                    "YUKIKA의 곡을 모두 MAX COMBO로 클리어했다.⭐",
                    "ESTiMATE 이미지를 모두 획득했다.⭐",
                    "ESTiMATE 곡 중에서 숨겨진 BGA를 발견했다.⭐"]

esti_caption = ["DLC 발매 이전에 클리어한 기록은 인정되지 않는다.",
                "DLC 발매 이전에 클리어한 기록은 인정되지 않는다.",
                "DLC 발매 이전에 클리어한 기록은 인정되지 않는다.\n\n대상곡: NEON 1989(RESPECT V 기본곡), 안아줘",
                "HELIX 5장, Obelisque 3장, In My Heart ~ESTi Remix~ 1장, 안아줘 5장, U-NIVUS 6장으로 총 20장",
                "대상: U-NIVUS"]

esti = []
for i in range(len(load_images(esti_dir))):
    esti.append({"image": load_images(esti_dir)[i], 
                "keyword": "ESTI", 
                "name": esti_name[i], 
                "description": esti_description[i],
                "checked": False,
                "caption": esti_caption[i]})



##########################################################################################



nexon_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/7. NEXON")
nexon_name = ["DOG FIGHT",
              "몰?루",
              "수련의 숲을 클리어했다!",
              "Reminiscence",
              "루프송의 가호",
              "리얼 판타지 라이프",
              "보물 상자",
              "무지개 장갑",
              "RESPECT YOUR CHILDHOOD",
              "3,2,1 START!"]
nexon_description = ["7인이 참여한 오픈 매치에서 NEXON 기어를 장착하고 카트라이더 곡을 TOP SCORE, TOP RATE, TOP COMBO 중 하나를 달성했다⭐",
                     "블루 아카이브 곡을 10회 클리어했다.⭐",
                     "모든 메이플스토리 곡을 플레이하여 각 패턴의 MAX COMBO 합이 100000을 달성했다.⭐",
                     "FEVER OFF로 설정하고 테일즈위버 곡을 클리어했다.⭐",
                     "테이베르스 던전 테마곡을 S랭크로 클리어했다.⭐",
                     "7인이 참여한 오픈 매치에서 모두가 마비노기 곡을 MAX COMBO로 클리어했다.⭐",
                     "랜덤 선곡으로 NEXON DLC 곡을 플레이했다.⭐",
                     "NEXON DLC 기어를 장착하고 모든 카트라이더 곡을 MAX COMBO로 클리어했다.⭐",
                     "NEXON DLC 플레이트를 장착했다.",
                     "오픈 매치에서 NEXON DLC 기어를 장착하고 카트라이더 곡을 모두 클리어했다.⭐"]

nexon_caption = ["6인 이하 방에서는 달성할 수 없다.",
                 "난이도, 버튼 무관\n\n대상곡 : Constant Moderato",
                 "대상곡 : Lacheln, The City of Dreams(메이플스토리), Start The Adventure ~SOPHI Remix~(메이플스토리), The Raindrop Flower ~jam-jam Remix~(메이플스토리), The Little Adventurer(메이플스토리2)\n\n여기서의 MAX COMBO는 풀콤보를 뜻하는 것이 아닌 각 패턴의 최대 콤보수(Best Combo)를 뜻한다. 모든 대상곡의 8버튼을 제외한 모든 버튼 모든 난이도를 풀콤보로 클리어하면 달성 가능하다.",
                 "난이도, 버튼 무관",
                 "난이도, 버튼 무관",
                 "6인 이하 방에서는 달성할 수 없다.",
                 "BGA를 켜고 플레이해야 한다.\n\nNEXON DLC의 곡 중 두 개만 즐겨찾기에 추가한 다음, 랜덤을 돌리면 100% 확률로 달성 가능하다. 하나만 즐겨찾기에 넣을 경우 즐겨찾기 폴더에 랜덤 선곡이 출연하지 않는다. 또한 끝까지 플레이하지 않고 첫 노트만 쳐도 달성된다.",
                 "난이도는 상관없다. NORMAL 난이도로만 클리어해도 달성한 것으로 처리된다.",
                 "",
                 "난이도, 버튼 무관\n\n인원 제한 없음"]

nexon = []
for i in range(len(load_images(nexon_dir))):
    nexon.append({"image": load_images(nexon_dir)[i], 
                "keyword": "NEXON", 
                "name": nexon_name[i], 
                "description": nexon_description[i],
                "checked": False,
                "caption": nexon_caption[i]})
    


##########################################################################################



muds_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/8. Muse Dash")
muds_name = ["DJMAX Reflect",
              "냥냥 유니버스",
              "마리쟈의 일기장",
              "우리 부로",
              "좋아서 이런 모습 하고있는게 아니라고",
              "내가 널 키워줄게"]
muds_description = ["MUSE DASH 곡을 모두 S랭크로 클리어했다.⭐",
                     "모든 MUSE DASH 이미지를 획득하였다.",
                     "마리쟈가 메인으로 출연하는 곡을 MAX COMBO로 클리어했다.⭐",
                     "MUSE DASH 곡에서 20개의 패턴을 MAX COMBO로 클리어했다.",
                     "MUSE DASH 전용 UI 스킨을 적용했다.",
                     "오픈 매치에서 MUSE DASH 곡을 플레이하여 모두의 최대 콤보수 합이 30000콤보 이상을 기록했다."]

muds_caption = ["난이도, 버튼 무관",
                "",
                "대상곡 : MUSEDASH!!!!, Dysthimia",
                "", "", ""]

muds = []
for i in range(len(load_images(muds_dir))):
    muds.append({"image": load_images(muds_dir)[i], 
                "keyword": "MUDS", 
                "name": muds_name[i], 
                "description": muds_description[i],
                "checked": False,
                "caption": muds_caption[i]})



##########################################################################################



ez2on_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/9. EZ2ON")
ez2on_name = ["1-2-E2-3-4-5",
             "SELF EVOLuTION",
             "THE FIRST NB",
             "Theme of Storm",
             "R U ready 2 go insida DJ Box?",
             "-It rules once again-",
             "ABSOLUTE PITCH",
             "[OVER MIND]",
             "REMEMBER 1ST?",
             "Virtual Battle"]
ez2on_description = ["EZ2ON 곡을 모두 플레이했다.⭐",
                    "각 철자로 시작하는 제목의 곡을 순서에 맞춰 MAX COMBO로 클리어했다.⭐",
                    "Envy Mask - NB POWER를 연속해서 클리어했다.",
                    "Sand Storm - Enemy Storm - Brain Storm을 연속해서 클리어했다.",
                    "EZ2ON 1ST에 해당하는 곡을 모두 PERFECT PLAY로 클리어했다.⭐",
                    "EZ2ON 2ND에 해당하는 곡을 모두 S 랭크로 클리어했다.⭐",
                    "EZ2ON 3RD에 해당하는 곡을 모두 MAX COMBO로 클리어했다.⭐",
                    "EZ2ON 4TH에 해당하는 곡을 모두 S 랭크로 클리어했다.⭐",
                    "EZ2ON 곡 중 숨겨진 BGA를 발견했다.⭐",
                    "OPEN MATCH의 VERSUS MODE로 EZ2ON 곡을 플레이했다.⭐"]

ez2on_caption = ["난이도, 버튼 무관",
                 "MAX COMBO를 달성하기 위해 같은 곡을 재시작하거나 곡 선택 화면에서 다시 곡을 선택해도 곡을 클리어한 순서만 맞다면 달성으로 인정된다. 단, 게임을 종료한 다음 이어서 플레이하는 식으로는 달성할 수 없다.\n\n[최고속 습득 추천 루트]\nShoreline 1분 30초\nEmblem 1분 35초\nLacheln, The City of Dreams 1분 25초\nFunky Chups 1분 31초\nEternal Fantasy ~유니의 꿈~ 1분 41초\nVoid 1분 42초\nOver Your Dream 1분 39초\nLover (버전 상관없음) 1분 26초\nUrban Night - hYo작곡가 1분46초\nThe Clear Blue Sky 1분 35초\nIn my Dream 1분 37초\nOver the Rainbow 1분 51초\nNova ~Mr.Funky Remix~ 1분 48초\n\n도합 시간 26분 6초",
                 "", "",
                 "난이도, 버튼 무관\n\n대상곡 : Envy Mask, Look out ~Here comes my love~, Stay",
                 "난이도, 버튼 무관\n\n대상곡 : Appeal, Back For More, Showdown",
                 "난이도, 버튼 무관\n\n대상곡 : Lie Lie, Sand Storm, Sparrow",
                 "난이도, 버튼 무관\n\n대상곡 : Aquaris, Complex, Metagalactic",
                 "대상곡 : Look out ~Here Comes My Love~",
                 "난이도, 버튼 무관"]

ez2on = []
for i in range(len(load_images(ez2on_dir))):
    ez2on.append({"image": load_images(ez2on_dir)[i], 
                "keyword": "EZ2ON", 
                "name": ez2on_name[i], 
                "description": ez2on_description[i],
                "checked": False,
                "caption": ez2on_caption[i]})



##########################################################################################



maple_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/10. MapleStory")
maple_name = ["제네시스 해방",
              "여제님을 위하여!",
              "드레스 업! 여기가 내 무대라구~",
              "마스터 라벨",
              "모험의 서와 단풍잎"]
maple_description = ["MapleStory 곡을 모두 MAX COMBO로 클리어했다.⭐",
                     "6인 이상이 참여한 오픈 매치에서 MapleStory 곡을 플레이했다.⭐",
                     "MapleStory DLC 기어와 노트 스킨을 장착하고 MapleStory 곡을 클리어했다.⭐",
                     "MapleStory DLC 플레이트를 장착했다.",
                     "MapleStory 전용 UI 스킨을 적용했다."]

maple_caption = ["난이도, 버튼 무관",
                 "난이도, 버튼 무관",
                 "난이도, 버튼 무관",
                 "", ""]

maple = []
for i in range(len(load_images(maple_dir))):
    maple.append({"image": load_images(maple_dir)[i], 
                "keyword": "MAPLE", 
                "name": maple_name[i], 
                "description": maple_description[i],
                "checked": False,
                "caption": maple_caption[i]})




##########################################################################################



flcm_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/16. 콜라보레이션/11. Falcom")
flcm_name = ["기억을 되찾은 소녀",
              "붉은 머리의 모험가",
              "음유시인의 하모니카"]
flcm_description = ["FALCOM 팩 수록곡을 모두 MAX COMBO로 클리어했다.⭐",
                     "FALCOM 플레이트를 장착했다.",
                     "FALCOM UI Skin을 적용했다."]

flcm_caption = ["난이도, 버튼 무관",
                "", ""]

flcm = []
for i in range(len(load_images(flcm_dir))):
    flcm.append({"image": load_images(flcm_dir)[i], 
                "keyword": "FLCM", 
                "name": flcm_name[i], 
                "description": flcm_description[i],
                "checked": False,
                "caption": flcm_caption[i]})





##########################################################################################


liberty_dir = resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/17. V LIBERTY")
liberty_name = ["멋진 신세계",
                "수집가 1",
                "수집가 2",
                "해치웠나!?",
                "세트 상품입니다.",
                "DRIVE 음반도 들어줘요",
                "MAKE DJMAX GREAT AGAIN"]
liberty_description = ["V LIBERTY 모든 곡을 MAX COMBO로 클리어했다.⭐",
                       "20개의 V LIBERTY 플레이트를 획득했다.",
                       "21개의 V LIBERTY 갤러리 아이템을 획득했다.",
                       "미션 모드에서 'BROKEN BROKI' 미션을 클리어했다.",
                       "LIBERTY 기어 스킨과 노트 스킨을 사용했다.",
                       "DRIVE 앨범 수록곡들을 플레이했다.⭐",
                       "'V LIBERTY' UI 스킨을 적용했다."]
liberty_caption = ["난이도, 버튼 무관",
                   "","","","",
                   "난이도, 버튼 무관\n\n대상곡: 평행고백 ~Pan Remix~, Bestie",
                   ""]

liberty = []
for i in range(len(load_images(liberty_dir))):
    liberty.append({"image": load_images(liberty_dir)[i], 
                "keyword": "LBTV", 
                "name": liberty_name[i], 
                "description": liberty_description[i],
                "checked": False,
                "caption": liberty_caption[i]})





##############
## 최종 병합 ##
##############

# 정규 dlc
final_data.extend(rptv)
final_data.extend(ex1)
final_data.extend(ex2)
final_data.extend(ex3)
final_data.extend(ex4)
final_data.extend(ex5)

# 레거시 dlc
final_data.extend(tr)
final_data.extend(tech)
final_data.extend(tech2)
final_data.extend(tech3)
final_data.extend(blsq)
final_data.extend(clsq)
final_data.extend(link)
final_data.extend(ptb3)
final_data.extend(tnq)

# 콜라보 dlc
final_data.extend(groov)
final_data.extend(Cytus)
final_data.extend(deemo)
final_data.extend(glfr)
final_data.extend(chu)
final_data.extend(esti)
final_data.extend(nexon)
final_data.extend(muds)
final_data.extend(ez2on)
final_data.extend(maple)
final_data.extend(flcm)

# 이후 추가된 dlc
final_data.extend(liberty)