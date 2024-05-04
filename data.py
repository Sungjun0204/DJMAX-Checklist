import os

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







rptv_dir = "djmax_app/djmax_assignment/jpg/1. DJMAX RESPECT V"
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

rptv_description = ["모든 곡을 클리어했다.",
                    "BREAK 1개로 클리어했다.",
                    "처음으로 클리어에 실패했다.",
                    "크레딧을 처음으로 감상했다.",
                    "콜렉션에서 NB Ranger 시리즈의 모든 뮤직 비디오를 감상했다.",
                    "10가지의 기어를 획득했다.",
                    "10가지의 노트를 획득했다.",
                    "30가지의 플레이트를 획득했다.",
                    "50가지의 코멘트를 획득했다.",
                    "100장의 이미지를 획득했다.",
                    
                    "난이도 10 이상의 패턴 10개를 MAX COMBO로 클리어했다.",
                    "난이도 10 이상의 패턴 30개를 MAX COMBO로 클리어했다.",
                    "난이도 10 이상의 패턴 50개를 MAX COMBO로 클리어했다.",
                    "100개의 패턴을 MAX COMBO로 클리어했다.",
                    "300개의 패턴을 MAX COMBO로 클리어했다.",
                    "500개의 패턴을 MAX COMBO로 클리어했다.",
                    "PERFECT PLAY로 클리어했다.",
                    "임의의 버튼으로 마스터 스코어의 달성률을 40% 달성했다.",
                    "임의의 버튼으로 마스터 스코어의 달성률을 80% 달성했다.",
                    "AIR를 처음으로 플레이했다.",
                    
                    "OPEN MATCH에서 채팅을 전송했다.",
                    "AIR에서 자신이 가장 좋아하는 곡을 플레이했다.",
                    "AIR에서 10곡에 대한 코멘트를 작성했다.",
                    "AIR에서 스티커를 붙였다.",
                    "미션 10개를 클리어했다.",
                    "미션 30개를 클리어했다.",
                    "미션 50개를 클리어했다.",
                    "래더 매치를 처음으로 플레이했다.",
                    "래더 매치에서 동점을 기록했다.",
                    "래더 매치에서 브론즈 등급으로 승급했다.",
                    
                    "래더 매치에서 실버 등급으로 승급했다.",
                    "래더 매치에서 골드 등급으로 승급했다.",
                    "한 곡에서 5,000 콤보 이상으로 클리어했다.",
                    "100,000 콤보를 달성했다.",
                    "999,999 콤보를 달성했다.",
                    "누적 점수가 100,000,000점을 돌파했다.",
                    "누적 점수가 200,000,000점을 돌파했다.",
                    "누적 점수가 300,000,000점을 돌파했다.",
                    "S랭크로 100회 클리어 했다.",
                    "오픈 매치에서 모두가 MAX COMBO로 클리어했다.",
                    
                    "오픈 매치를 100회 플레이했다.",
                    "오픈 매치에서 스코어 부문 1등을 기록했다.",
                    "오픈 매치에서 호스트 권한을 넘겨주었다.",
                    "레벨 10을 달성했다.",
                    "레벨 50을 달성했다.",
                    "레벨 99를 달성했다.",
                    "정확하게 777 콤보로 클리어했다.",
                    "한 곡에서 10,000 콤보 이상으로 클리어했다.",
                    "처음으로 숨겨진 BGA를 발견했다.",
                    "모든 숨겨진 BGA를 발견했다.",
                    
                    "미션에서 A.I.를 상대로 승리했다.",
                    "DJMAX RESPECT V의 모든 도전과제를 달성했다."]

rptv = []
for i in range(len(load_images(rptv_dir))):
    rptv.append({"image": load_images(rptv_dir)[i], 
                "keyword": "RPTV", 
                "name": rptv_name[i], 
                "description": rptv_description[i],
                "checked": False})



##########################################################################################



ex1_dir = "djmax_app/djmax_assignment/jpg/2. V EXTENSION"
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
                  "AIR에서 V EXTENSION 곡에 대한 코멘트를 작성했다.",
                  "Starlight Guitar 미션을 클리어했다.",
                  "V EXTENSION 곡을 모두 S랭크로 클리어했다.",
                  "V EXTENSION 곡에서 50개의 패턴을 MAX COMBO로 클리어했다.",
                  "Icy Blonde 미션을 클리어했다.",
                  "Dream it 기어와 노트를 장착한 상태로 Dream it을 MAX COMBO로 클리어했다."]

ex1 = []
for i in range(len(load_images(ex1_dir))):
    ex1.append({"image": load_images(ex1_dir)[i], 
                "keyword": "EX1", 
                "name": ex1_name[i], 
                "description": ex1_description[i],
                "checked": False})



##########################################################################################




tr_dir = "djmax_app/djmax_assignment/jpg/3. TRILOGY"
tr_name = ["당신은 대체…",
            "제 여자친구가 확실합니다!",
            "수호천사",
            "뉴 스킨 작렬…!",
            "다음 이벤트도 기대해주세요",
            "대신푸우른USB를드리겠습니다",
            "나올수도 있고 안나올수도 있습니다"]
tr_description = ["TRILOGY 곡을 모두 S랭크로 클리어했다.",
                  "오픈 매치에서 모두가 Someday를 MAX COMBO로 클리어했다.",
                  "오픈 매치에서 My Jealousy를 MAX COMBO로 클리어했다.",
                  "TRILOGY 전용 UI 스킨을 적용했다.",
                  "DJMAX RESPECT U 미션을 클리어했다.",
                  "TRILOGY 곡을 내가 좋아하는 곡 순위권에 등극시켰다.",
                  "TRILOGY 곡 중 숨겨진 BGA를 발견했다."]

tr = []
for i in range(len(load_images(tr_dir))):
    tr.append({"image": load_images(tr_dir)[i], 
                "keyword": "TR", 
                "name": tr_name[i], 
                "description": tr_description[i],
                "checked": False})



##########################################################################################



clsq_dir = "djmax_app/djmax_assignment/jpg/4. CLAZZIQUAI"
clsq_name = ["클럽 투어에 오신것을 환영합니다",
             "CE Style",
             "Metro Project",
             "역시 프로 리듬게이머는 달라",
             "클리어 위주로 갑시다",
             "DJ Clazzi",
             "Go Back From the Top",
             "DJMAX ARTIST TEAM"]
clsq_description = ["Electronic City를 클리어했다.",
                    "Lover(CE Style), Y(CE Style)을 MAX COMBO로 클리어했다.",
                    "오픈 매치에서 Clazziquai Edition 곡을 모두가 다른 패턴으로 선택하여 클리어했다.",
                    "Clazziquai Edition 곡 중 한 곡의 모든 패턴을 MAX COMBO로 클리어했다.",
                    "Clazziquai Edition 곡을 모두 S랭크로 클리어했다.",
                    "Clazziquai의 곡을 모두 MAX COMBO로 클리어했다.",
                    "Clazziquai Edition 곡 중 숨겨진 BGA를 발견했다.",
                    "DJMAX TOURNAMENT LIVE 미션을 클리어했다."]

clsq = []
for i in range(len(load_images(clsq_dir))):
    clsq.append({"image": load_images(clsq_dir)[i], 
                "keyword": "CLQI", 
                "name": clsq_name[i], 
                "description": clsq_description[i],
                "checked": False})



##########################################################################################



blsq_dir = "djmax_app/djmax_assignment/jpg/5. BLACK SQUARE"
blsq_name = ["정말 BLACK SQUARE 곡으로 할거야?",
             "BLACK SQUARE에 도전하시겠습니까?",
             "Get Down의 그녀",
             "Fermion으로 하겠어요",
             "REDESIGN?!",
             "BS Style",
             "페일 위주로 갑니다",
             "빨리 틀어요",
             "DJMAX 시리즈 중에서 최강 난이도"]
blsq_description = ["오픈 매치에서 BLACK SQUARE 곡을 모두가 같은 패턴으로 선택하여 MAX COMBO로 클리어했다.",
                    "BLACK SQUARE 곡의 100가지 패턴을 MAX COMBO로 클리어했다.",
                    "First Kiss 기어를 사용하여 다나를 10번 확인했다.",
                    "Fermion을 체력 게이지 20% 이하만 남겨두고 클리어했다.",
                    "RD Colosseum 미션을 클리어했다.",
                    "Lover(BS Style), Y(BS Style)을 MAX COMBO로 클리어했다.",
                    "BLACK SQUARE 곡을 모두 S랭크로 클리어했다.",
                    "BLACK SQUARE 수록곡 중 한 곡을 연속으로 10회 클리어했다.",
                    "BLACK SQUARE의 SC 패턴을 플레이했다."]

blsq = []
for i in range(len(load_images(blsq_dir))):
    blsq.append({"image": load_images(blsq_dir)[i], 
                "keyword": "BLSQ", 
                "name": blsq_name[i], 
                "description": blsq_description[i],
                "checked": False})



##########################################################################################



tech_dir = "djmax_app/djmax_assignment/jpg/6. TECHNIKA"
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
tech_description = ["TECHNIKA 곡을 모두 S랭크로 클리어했다.",
                    "숨겨진 패턴을 MAX COMBO로 클리어했다.",
                    "First step 미션에서 플레이 할 수 있는 모든 곡을 클리어했다.",
                    "COLLECTION 모드에서 SuperSonic의 뮤직 비디오를 감상했다.",
                    "Mr.Perfect 미션을 클리어했다.",
                    "5가지의 TECHNIKA 플레이트를 획득했다.",
                    "Technical Mixing에서 할 수 있는 모든 패턴을 플레이했다.",
                    "오픈 매치에서 TECHNIKA 곡으로 7명 모두 MAX COMBO를 달성했다.",
                    "추장의 장비를 갖추고 SON OF SUN을 MAX COMBO로 클리어했다.",
                    "TECHNIKA 곡 중 숨겨진 BGA를 발견했다."]

tech = []
for i in range(len(load_images(tech_dir))):
    tech.append({"image": load_images(tech_dir)[i], 
                "keyword": "TECH", 
                "name": tech_name[i], 
                "description": tech_description[i],
                "checked": False})



##########################################################################################



tech2_dir = "djmax_app/djmax_assignment/jpg/7. TECHNIKA 2"
tech2_name = ["팝 마스터가 될거야",
              "선생님도 결국 재능이었군요",
              "CREW RACE",
              "혼자밖에 생각하지 않아",
              "죽음의 무도",
              "테크니카 붐은 온다",
              "RAINBOW MAX",
              "언제까지 피버를 안 쓰실 겁니까"]
tech2_description = ["TECHNIKA 2 곡을 모두 S랭크로 클리어했다.",
                     "STAR MIXING 미션을 전부 클리어했다.",
                     "TECHNIKA 2 UI 스킨을 적용했다.",
                     "오픈 매치에서 TECHNIKA 2 곡으로 TOP SCORE, RATE, COMBO를 동시에 기록했다.",
                     "D2 기어와 노트를 장착한 상태로 D2를 2번 클리어했다.",
                     "TECHNIKA 2 홍보 영상을 감상했다.",
                     "새로운 TB 패턴을 MAX COMBO로 클리어했다.",
                     "새로운 TB 패턴에서 피버를 3회 발동 후 클리어했다."]

tech2 = []
for i in range(len(load_images(tech2_dir))):
    tech2.append({"image": load_images(tech2_dir)[i], 
                "keyword": "TECH2", 
                "name": tech2_name[i], 
                "description": tech2_description[i],
                "checked": False})



##########################################################################################



tech3_dir = "djmax_app/djmax_assignment/jpg/8. TECHNIKA 3"
tech3_name = ["CREW CHALLENGE",
             "1일 1맥",
             "와! 신곡!",
             "PRETTY PIC BESIDE PRETTY PIC",
             "절대 미션해",
             "싹쓰리",
             "펀하고 쿨하고 섹시하게",
             "맛집 탐험"]
tech3_description = ["TECHNIKA 3 곡을 모두 S랭크로 클리어했다.",
                    "TECHNIKA 3 곡에서 10개의 패턴을 MAX COMBO로 클리어했다.",
                    "ALiCE를 MAX COMBO로 클리어했다.",
                    "10장의 TECHNIKA 3 이미지를 획득했다.",
                    "POP MIXING 미션을 전부 플레이했다.",
                    "오픈 매치에서 TECHNIKA 3 곡으로 TOP SCORE, RATE, COMBO를 동시에 기록했다.",
                    "5가지의 TECHNIKA 3 플레이트를 획득했다.",
                    "TECHNIKA 3 곡에서 SC 패턴을 MAX COMBO로 클리어했다."]

tech3 = []
for i in range(len(load_images(tech3_dir))):
    tech3.append({"image": load_images(tech3_dir)[i], 
                "keyword": "TECH3", 
                "name": tech3_name[i], 
                "description": tech3_description[i],
                "checked": False})



##########################################################################################



link_dir = "djmax_app/djmax_assignment/jpg/9. LINK DISC"
link_name = ["링크 디스크",
             "디스크 조각",
             "이제 최종 단계에 들어선거야"]
link_description = ["링크 디스크 미션을 개방했다.",
                    "링크 디스크를 통해 획득할 수 있는 모든 곡을 MAX COMBO로 클리어했다.",
                    "The Others 미션을 클리어했다."]

link = []
for i in range(len(load_images(link_dir))):
    link.append({"image": load_images(link_dir)[i], 
                "keyword": "LINK", 
                "name": link_name[i], 
                "description": link_description[i],
                "checked": False})



##########################################################################################



ptb3_dir = "djmax_app/djmax_assignment/jpg/10. PORTABLE 3"
ptb3_name = ["MADE BY MUSICIANS",
             "REmixVOLUTION",
             "Now or never",
             "Put Your Hanz Up!",
             "REMIX SYSTEM",
             "역주행 모드",
             "롤린 롤린",
             "안 죄송합니다"]
ptb3_description = ["PORTABLE 3 곡을 모두 S랭크로 클리어했다.",
                    "PORTABLE 3의 모든 REMIX 곡을 클리어 했다.",
                    "PORTABLE 3 기어를 장착하고 PORTABLE 3 곡을 MAX COMBO로 클리어 했다.",
                    "Hanz up! 메이킹 영상을 시청했다.",
                    "새로운 리믹스 모드에서 MAX COMBO를 달성했다.",
                    "Rewind 미션을 클리어했다.",
                    "10장의 PORTABLE 3 이미지를 획득했다.",
                    "오픈 매치에서 PORTABLE 3 곡을 플레이하여 모두의 최대 콤보수 합이 30000콤보 이상을 기록했다."]

ptb3 = []
for i in range(len(load_images(ptb3_dir))):
    ptb3.append({"image": load_images(ptb3_dir)[i], 
                "keyword": "PTB3", 
                "name": ptb3_name[i], 
                "description": ptb3_description[i],
                "checked": False})



##########################################################################################




ex2_dir = "djmax_app/djmax_assignment/jpg/11. V EXTENSION 2"
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
ex2_description = ["V EXTENSION 2 곡을 모두 S랭크로 클리어했다.",
                   "VERSUS 미션을 클리어했다.",
                   "V EXTENSION 2 곡을 NORMAL - HARD - MAXIMUM - SC 난이도 순으로 클리어했다.",
                   "Arcade Love의 SC 패턴을 플레이했다.",
                   "FEVER OFF 설정으로 V EX 2 기어를 장착하고 임의의 곡을 클리어했다.",
                   "V EXTENSION 2 플레이트 중 하나를 장착했다.",
                   "V EXTENSION 2 곡 중에서 숨겨진 BGA를 발견했다.",
                   "V LINK를 통해 획득한 곡을 MAX COMBO로 클리어했다.",
                   "V LINK 미션을 개방했다.",
                   "V LINK 미션 DoLLS를 클리어했다."]

ex2 = []
for i in range(len(load_images(ex2_dir))):
    ex2.append({"image": load_images(ex2_dir)[i], 
                "keyword": "EX2", 
                "name": ex2_name[i], 
                "description": ex2_description[i],
                "checked": False})



##########################################################################################




tnq_dir = "djmax_app/djmax_assignment/jpg/12. TECHNIKA TUNE & Q"
tnq_name = ["GRAND MASTER of TUNE",
            "Q Lover",
            "Owner of TUNE Q Gallery",
            "T to the TUNE to the Q",
            "튠큐 어서오고",
            "FEVER...FEVER...FEVER!!",
            "Never Ending TECHNIKA"]
tnq_description = ["TECHNIKA TUNE 곡을 모두 MAX COMBO로 클리어했다.",
                   "TECHNIKA Q 곡을 모두 S랭크로 클리어했다.",
                   "모든 TECHNIKA TUNE Q DLC 이미지를 획득했다.",
                   "TECHNIKA TUNE Q 플레이트를 장착했다.",
                   "래더 매치에서 TECHNIKA TUNE Q 곡을 플레이했다.",
                   "TECHNIKA TUNE Q TB 패턴에서 피버를 3회 발동 후 클리어했다.",
                   "Never Ending TECHNIKA의 TB 패턴을 클리어했다."]

tnq = []
for i in range(len(load_images(tnq_dir))):
    tnq.append({"image": load_images(tnq_dir)[i], 
                "keyword": "T&Q", 
                "name": tnq_name[i], 
                "description": tnq_description[i],
                "checked": False})



##########################################################################################



ex3_dir = "djmax_app/djmax_assignment/jpg/13. V EXTENSION 3"
ex3_name = ["DO 3XTENSION", 
            "Tic! Tac! Toe!",
            "디맥의 홀더",
            "엔비 타이탄 더 브로큰 하트",
            "자고로 맥콤이란",
            "운명, 흥망돌, 빡빡이",
            "가보자고",
            "ONE & ONLY"]
ex3_description = ["V EXTENSION 3 곡을 모두 MAX COMBO로 클리어했다.",
                   "Tic! Tac! Toe!의 각각 다른 패턴을 S랭크 이상으로 9회 클리어했다.",
                   "V EXTENSION 3 UI 스킨을 적용했다.",
                   "COLLECTION 모드에서 NB RANGER - Virgin Force, NB RANGER 운명의 Destiny 뮤직 비디오를 연속해서 감상했다.",
                   "V EXTENSION 3 곡을 BREAK 1개로 클리어했다.",
                   "V EXTENSION 3 곡 중에서 숨겨진 BGA를 모두 발견했다.",
                   "V EXTENSION 3 곡을 8500콤보 이상으로 클리어했다.",
                   "오픈 팀 매치에서 V EXTENSION 3 곡으로 승리했다."]

ex3 = []
for i in range(len(load_images(ex3_dir))):
    ex3.append({"image": load_images(ex3_dir)[i], 
                "keyword": "EX3", 
                "name": ex3_name[i], 
                "description": ex3_description[i],
                "checked": False})



##########################################################################################




ex4_dir = "djmax_app/djmax_assignment/jpg/14. V EXTENSION 4"
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
ex4_description = ["V EXTENSION 4 곡을 모두 S랭크로 클리어했다.",
                   "LUV, Vertical Eclipse, DIE IN 3곡을 각각 다른 패턴으로 4회씩 클리어했다.",
                   "V EXTENSION 4 곡을 NORMAL - HARD - MAXIMUM - SC 순으로 클리어했다.",
                   "Deadly Bomber, Vertical Eclipse를 차례대로 S 랭크로 클리어했다.",
                   "COLLECTION 모드에서 LUV, Vertical Eclipse, DIE IN 뮤직 비디오를 연속해서 감상했다.",
                   "모든 V EXTENSION 4 DLC 이미지를 획득했다.",
                   "오픈 매치에서 V EXTENSION 4 곡을 플레이하여 MAX COMBO를 달성했다.",
                   "V LINK 2를 통해 획득한 곡을 MAX COMBO로 클리어했다.",
                   "V LINK 2 미션을 개방했다.",
                   "V LINK 2 미션 conveyor belt를 클리어했다."]

ex4 = []
for i in range(len(load_images(ex4_dir))):
    ex4.append({"image": load_images(ex4_dir)[i], 
                "keyword": "EX4", 
                "name": ex4_name[i], 
                "description": ex4_description[i],
                "checked": False})



##########################################################################################



ex5_dir = "djmax_app/djmax_assignment/jpg/15. V EXTENSION 5"
ex5_name = ["하하하! 유저야, 또 해냈구나!", 
            "필요한 만큼은 보여 줬다.",
            "인벤토리 안에 놓고 가 주세요.",
            "그대들 어떻게 시작할 것인가",
            "다인 시대의 끝이 도래했다.",
            "스킨의 멋짐을 모르는 당신은 불쌍해요.",
            "해냈다! 해냈어!"]
ex5_description = ["V EXTENSION 5 모든 곡을 S랭크로 클리어했다.",
                   "25개의 V EXTENSION 5 이미지를 획득했다.",
                   "20개의 V EXTENSION 5 플레이트를 획득했다.",
                   "'V EXTENSION 5 UI' 스킨을 적용했다.",
                   "COLLECTION 모드에서 'Peace Comes At a Price'의 BGA를 감상했다.",
                   "V EX 5 기어와 노트를 장착하고 'glory MAX'를 클리어했다.",
                   "B O n u S 미션을 클리어했다."]

ex5 = []
for i in range(len(load_images(ex5_dir))):
    ex5.append({"image": load_images(ex5_dir)[i], 
                "keyword": "EX5", 
                "name": ex5_name[i], 
                "description": ex5_description[i],
                "checked": False})



##########################################################################################



groov_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/1. GROOVE COASTER"
groov_name = ["AD-LIB",
              "Got more plate?",
              "미안하다 이거 시켜보려고 안보이게 해놨다"]
groov_description = ["Groove Coaster 곡을 모두 S랭크로 클리어했다.",
                     "DJMAX 캐릭터가 픽셀로 표현된 플레이트를 모두 획득했다.",
                     "Groove Prayer 5B HD 패턴을 BLIND로 클리어했다."]

groov = []
for i in range(len(load_images(groov_dir))):
    groov.append({"image": load_images(groov_dir)[i], 
                "keyword": "GRUV", 
                "name": groov_name[i], 
                "description": groov_description[i],
                "checked": False})




##########################################################################################



Cytus_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/2. Cytus"
Cytus_name = ["Can you hear me?",
              "모든 사건의 흑막",
              "Aesir",
              "Million Master",
              "CAPSO!"]
Cytus_description = ["CYTUS 전용 UI 스킨을 적용했다.",
                     "Entrance를 MAX COMBO로 클리어했다.",
                     "L을 MAX COMBO로 클리어했다.",
                     "CYTUS 곡 중 3개의 패턴을 PERFECT PLAY로 클리어했다.",
                     "5가지의 CYTUS 플레이트를 획득했다."]

Cytus = []
for i in range(len(load_images(Cytus_dir))):
    Cytus.append({"image": load_images(Cytus_dir)[i], 
                "keyword": "Cytus", 
                "name": Cytus_name[i], 
                "description": Cytus_description[i],
                "checked": False})



##########################################################################################



deemo_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/3. DEEMO"
deemo_name = ["소녀",
              "Deemo",
              "가면을 쓴 여자아이",
              "영혼"]
deemo_description = ["DEEMO 곡에서 처음으로 클리어에 실패했다.",
                     "DEEMO 곡에서 42개의 패턴을 클리어했다.",
                     "10가지의 DEEMO 플레이트를 획득했다.",
                     "DEEMO 기어와 노트를 장착한 상태로 ANiMA를 클리어했다."]

deemo = []
for i in range(len(load_images(deemo_dir))):
    deemo.append({"image": load_images(deemo_dir)[i], 
                "keyword": "DEEMO", 
                "name": deemo_name[i], 
                "description": deemo_description[i],
                "checked": False})
    


##########################################################################################



glfr_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/4. 소녀전선"
glfr_name = ["FRONTLINE",
              "404 Not Found",
              "그리폰&크루거",
              "철혈공조공단",
              "기지 귀환"]
glfr_description = ["Frontline을 MAX COMBO로 클리어했다.",
                     "404 Not Found 소대의 플레이트를 모두 획득했다.",
                     "Anti Rain의 플레이트를 획득했다.",
                     "철혈의 모든 전술 인형들과 조우했다.",
                     "두 진영의 모든 전술 인형들과 조우했다."]

glfr = []
for i in range(len(load_images(glfr_dir))):
    glfr.append({"image": load_images(glfr_dir)[i], 
                "keyword": "GLFR", 
                "name": glfr_name[i], 
                "description": glfr_description[i],
                "checked": False})



##########################################################################################



chu_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/5. CHUNITHM"
chu_name = ["츄니즘 퀘스트",
             "WORLD`S END",
             "츄니펭귄",
             "Over Power",
             "스킬 발동"]
chu_description = ["CHUNITHM 곡을 모두 MAX COMBO로 클리어했다.",
                    "CHUNITHM 곡 중에서 난이도 15의 패턴을 플레이했다.",
                    "CHUNITHM 플레이트를 장착했다.",
                    "CHUNITHM 곡을 9000콤보 이상으로 클리어했다.",
                    "CHUNITHM 곡 플레이 중에 FEVER를 30회 사용."]

chu = []
for i in range(len(load_images(chu_dir))):
    chu.append({"image": load_images(chu_dir)[i], 
                "keyword": "CHU", 
                "name": chu_name[i], 
                "description": chu_description[i],
                "checked": False})
    



##########################################################################################



esti_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/6. ESTimate"
esti_name = ["ESTINATION",
             "음유시인",
             "시티팝",
             "꽃에 진심인 편",
             "우주 대스타"]
esti_description = ["OBLIVION, OBLIVION ~Rockin' Night Style~, Obelisque를 차례대로 클리어했다.",
                    "SIN, SIN ~The Last Scene~, HELIX를 차례대로 클리어했다.",
                    "YUKIKA의 곡을 모두 MAX COMBO로 클리어했다.",
                    "ESTiMATE 이미지를 모두 획득했다.",
                    "ESTiMATE 곡 중에서 숨겨진 BGA를 발견했다."]

esti = []
for i in range(len(load_images(esti_dir))):
    esti.append({"image": load_images(esti_dir)[i], 
                "keyword": "ESTI", 
                "name": esti_name[i], 
                "description": esti_description[i],
                "checked": False})



##########################################################################################



nexon_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/7. NEXON"
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
nexon_description = ["7인이 참여한 오픈 매치에서 NEXON 기어를 장착하고 카트라이더 곡을 TOP SCORE, TOP RATE, TOP COMBO 중 하나를 달성했다",
                     "블루 아카이브 곡을 10회 클리어했다.",
                     "모든 메이플스토리 곡을 플레이하여 각 패턴의 MAX COMBO 합이 100000을 달성했다.",
                     "FEVER OFF로 설정하고 테일즈위버 곡을 클리어했다.",
                     "테이베르스 던전 테마곡을 S랭크로 클리어했다.",
                     "7인이 참여한 오픈 매치에서 모두가 마비노기 곡을 MAX COMBO로 클리어했다.",
                     "랜덤 선곡으로 NEXON DLC 곡을 플레이했다.",
                     "NEXON DLC 기어를 장착하고 모든 카트라이더 곡을 MAX COMBO로 클리어했다.",
                     "NEXON DLC 플레이트를 장착했다.",
                     "오픈 매치에서 NEXON DLC 기어를 장착하고 카트라이더 곡을 모두 클리어했다."]

nexon = []
for i in range(len(load_images(nexon_dir))):
    nexon.append({"image": load_images(nexon_dir)[i], 
                "keyword": "NEXON", 
                "name": nexon_name[i], 
                "description": nexon_description[i],
                "checked": False})
    


##########################################################################################



muds_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/8. Muse Dash"
muds_name = ["DJMAX Reflect",
              "냥냥 유니버스",
              "마리쟈의 일기장",
              "우리 부로",
              "좋아서 이런 모습 하고있는게 아니라고",
              "내가 널 키워줄게"]
muds_description = ["MUSE DASH 곡을 모두 S랭크로 클리어했다.",
                     "모든 MUSE DASH 이미지를 획득하였다.",
                     "마리쟈가 메인으로 출연하는 곡을 MAX COMBO로 클리어했다.",
                     "MUSE DASH 곡에서 20개의 패턴을 MAX COMBO로 클리어했다.",
                     "MUSE DASH 전용 UI 스킨을 적용했다.",
                     "오픈 매치에서 MUSE DASH 곡을 플레이하여 모두의 최대 콤보수 합이 30000콤보 이상을 기록했다."]

muds = []
for i in range(len(load_images(muds_dir))):
    muds.append({"image": load_images(muds_dir)[i], 
                "keyword": "MUDS", 
                "name": muds_name[i], 
                "description": muds_description[i],
                "checked": False})



##########################################################################################



ez2on_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/9. EZ2ON"
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
ez2on_description = ["EZ2ON 곡을 모두 플레이했다.",
                    "각 철자로 시작하는 제목의 곡을 순서에 맞춰 MAX COMBO로 클리어했다.",
                    "Envy Mask - NB POWER를 연속해서 클리어했다.",
                    "Sand Storm - Enemy Storm - Brain Storm을 연속해서 클리어했다.",
                    "EZ2ON 1ST에 해당하는 곡을 모두 PERFECT PLAY로 클리어했다.",
                    "EZ2ON 2ND에 해당하는 곡을 모두 S 랭크로 클리어했다.",
                    "EZ2ON 3RD에 해당하는 곡을 모두 MAX COMBO로 클리어했다.",
                    "EZ2ON 4TH에 해당하는 곡을 모두 S 랭크로 클리어했다.",
                    "EZ2ON 곡 중 숨겨진 BGA를 발견했다.",
                    "OPEN MATCH의 VERSUS MODE로 EZ2ON 곡을 플레이했다."]

ez2on = []
for i in range(len(load_images(ez2on_dir))):
    ez2on.append({"image": load_images(ez2on_dir)[i], 
                "keyword": "EZ2ON", 
                "name": ez2on_name[i], 
                "description": ez2on_description[i],
                "checked": False})



##########################################################################################



maple_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/10. MapleStory"
maple_name = ["제네시스 해방",
              "여제님을 위하여!",
              "드레스 업! 여기가 내 무대라구~",
              "마스터 라벨",
              "모험의 서와 단풍잎"]
maple_description = ["MapleStory 곡을 모두 MAX COMBO로 클리어했다.",
                     "6인 이상이 참여한 오픈 매치에서 MapleStory 곡을 플레이했다.",
                     "MapleStory DLC 기어와 노트 스킨을 장착하고 MapleStory 곡을 클리어했다.",
                     "MapleStory DLC 플레이트를 장착했다.",
                     "MapleStory 전용 UI 스킨을 적용했다."]

maple = []
for i in range(len(load_images(maple_dir))):
    maple.append({"image": load_images(maple_dir)[i], 
                "keyword": "MAPLE", 
                "name": maple_name[i], 
                "description": maple_description[i],
                "checked": False})




##########################################################################################



flcm_dir = "djmax_app/djmax_assignment/jpg/16. 콜라보레이션/11. Falcom"
flcm_name = ["기억을 되찾은 소녀",
              "붉은 머리의 모험가",
              "음유시인의 하모니카"]
flcm_description = ["FALCOM 팩 수록곡을 모두 MAX COMBO로 클리어했다.",
                     "FALCOM 플레이트를 장착했다.",
                     "FALCOM UI Skin을 적용했다."]

flcm = []
for i in range(len(load_images(flcm_dir))):
    flcm.append({"image": load_images(flcm_dir)[i], 
                "keyword": "FLCM", 
                "name": flcm_name[i], 
                "description": flcm_description[i],
                "checked": False})









## 최종 병합 ##
# 정규 dlc
final_data.extend(rptv)
final_data.extend(ex1)
final_data.extend(tr)
final_data.extend(clsq)
final_data.extend(blsq)
final_data.extend(tech)
final_data.extend(tech2)
final_data.extend(tech3)
final_data.extend(link)
final_data.extend(ptb3)
final_data.extend(ex2)
final_data.extend(tnq)
final_data.extend(ex3)
final_data.extend(ex4)
final_data.extend(ex5)

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