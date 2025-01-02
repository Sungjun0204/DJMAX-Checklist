"""
** DJMAX RESPECT V 스팀 도전과제 체크리스트 프로그램 **

- 제작자: Sungjun Kim
- Email: kxt1234.max@gmail.com
- 개발 시작: 2024.05.03

"""

# imports
import tkinter as tk
from tkinter import ttk, Label
from PIL import Image, ImageTk, ImageDraw, ImageColor
import json
import data as dlc
import os, sys
import sv_ttk

# 각종 상수 초기화
WINDOW_WIDTH = 770          # 프로그램 창 폭
WINDOW_HEIGHT =750         # 프로그램 창 높이
TOP_FRAME_HEIGHT = 100      # 상단 배너 고정창 구역 높이
RIGHT_SIDE_WIDTH = 170      # 우측 고정창 구역 폭 
HEAD_FRAME_HEIGHT = 30      # 머릿글 고정창 구역 높이
FILTER_FRAME_HEIGHT = 50    # 필터 버튼 할당 구역 높이
FILTER_FRAME_HEIGHT2 = 50
FILTER_FRAME_HEIGHT3 = 50
FILTER_KEYWORDS = ["RPTV", "EX1", "EX2", "EX3", "EX4", "EX5"]           # 필터버튼 1행
FILTER_KEYWORDS2 = ["TR", "TECH", "TECH2", "TECH3", "BLSQ",             # 필터버튼 2행
                   "CLQI", "LINK", "PTB3", "T&Q"]
FILTER_KEYWORDS3 = ["GRUV", "Cytus", "DEEMO", "GLFR", "CHU", "ESTI",    # 필터버튼 3행
                    "NEXON", "MUDS", "EZ2ON", "MAPLE", "FLCM", "LBTV"]
STATE_FILE = 'checkboxstates5.json'

# 버튼 사이즈
BTN_WIDTH = 40
BTN_HEIGHT = 20


# 데이터셋 초기화
data = dlc.final_data

# 절대경로 설정 함수
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


# 프로그램 창 설정
root = tk.Tk()
root.title("DJMAX RESPECT V 도전과제 체크리스트")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# 아이콘 설정
icon32 = tk.PhotoImage(file=resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/icon32.jpg"))
icon16 = tk.PhotoImage(file=resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/icon16.jpg"))

root.iconphoto(True, icon32, icon16)


# 상단 고정창 설정
# 이미지 로드
image = Image.open(resource_path(r"C:/Users/SungjunKim/AppData/Local/Programs/Python/Python312/Scripts/djmax_app/djmax_assignment/jpg/title.jpg"))
title_image = ImageTk.PhotoImage(image)
# Label을 사용하여 이미지 표시
top_frame = Label(root, image=title_image, width=600)
top_frame.pack(side='top', anchor='nw')     # 이미지를 왼쪽 상단에 고정
# 상단 고정창의 텍스트 띄우기
text_info = tk.Label(top_frame, text=f"전체 도전과제 갯수: {len(data)}")
text_info.place(x=10, y=10)
checked_count_label = tk.Label(top_frame, text="내가 클리어한 도전과제 갯수: 0")
checked_count_label.place(x=10, y=35)

# 머리글 고정창 설정
head_frame = tk.Frame(root, width=600, height=HEAD_FRAME_HEIGHT, bg='light grey')
head_frame.pack(fill='x', side='top')
# 머리글 상세 항목 라벨 설정
# 이미지 머리글
head_image_label = tk.Label(head_frame, text=None, width=9, bg="light gray")
head_image_label.grid(row=0, column=0, padx=5, pady=0, sticky="w")
# DLC 머리글
head_keyword_label = tk.Label(head_frame, text="[DLC]", width=5, bg="light gray", font=("Helvetica", 8, "bold"))
head_keyword_label.grid(row=0, column=1, padx=5, pady=0, sticky="w")
# 이름 머리글
head_name_label = tk.Label(head_frame, text="[Name]", width=15, bg="light gray", font=("Helvetica", 8, "bold"))
head_name_label.grid(row=0, column=2, padx=5, pady=0, sticky="w")
# 설명 머리글
head_descript_label = tk.Label(head_frame, text="[Description]", width=40, bg="light gray", font=("Helvetica", 8, "bold"))
head_descript_label.grid(row=0, column=3, padx=5, pady=0, sticky="w")
# 체크박스 머리글
head_check_label = tk.Label(head_frame, text="✅", width=3, bg="light gray", font=("Helvetica", 8, "bold"))
head_check_label.grid(row=0, column=4, padx=1, pady=0, sticky="w")


# 우측 필터 버튼 고정창 설정
rightside_frame = tk.Frame(root, width=RIGHT_SIDE_WIDTH, height=WINDOW_HEIGHT-100)
rightside_frame.place(x=600, y=100)
# 우측 필터 버튼 고정창 테두리 설정
rightside_frame.config(relief='solid', borderwidth=2)  # 테두리 너비 2픽셀, 검정색 설정 # (상, 좌, 하, 우)
# 자식 위젯의 크기를 부모 위젯이 조절하지 않도록 설정
rightside_frame.pack_propagate(False)

# 구석 고정창 설정
corner_frame = tk.Frame(root, width=RIGHT_SIDE_WIDTH, height=100)
corner_frame.place(x=600, y=0)
corner_frame.config(relief='solid', borderwidth=2)  # 테두리 너비 2픽셀, 검정색 설정
# 자식 위젯의 크기를 부모 위젯이 조절하지 않도록 설정
corner_frame.pack_propagate(False)

# 구석 고정창의 머릿글 설정
corner_head_frame = tk.Frame(corner_frame, height=20, bg='light grey')
corner_head_frame.pack(fill='x', side='top')
corner_head_label = tk.Label(corner_head_frame, text="필터 버튼", width=0, bg="light gray")
corner_head_label.grid(row=0, column=0, padx=0, pady=0, sticky="w")

# 메인 프레임 설정
main_frame = tk.Frame(root, width=600, height=WINDOW_HEIGHT-HEAD_FRAME_HEIGHT-100)
main_frame.place(x=0, y=130)
main_frame.config(relief='solid', borderwidth=2)  # 테두리 너비 2픽셀, 검정색 설정
main_frame.pack_propagate(False)  # 내부 컨텐츠에 맞게 크기 조정하지 않도록 설정



# 체크박스에 체크 안 되어있는 항목만 보여주는 필터 버튼 정의
def filter_unchecked_items():
    for idx, item in enumerate(data):
        if not item["checked"]:
            frame = item_frames.get(idx)
            if frame:
                frame.grid()
        else:
            frame = item_frames.get(idx)
            if frame:
                frame.grid_remove()





#### 스크롤창 설정 코드 ####

def create_scrollable_frame(parent_frame):
    # Canvas and scrollable frame setup
    canvas = tk.Canvas(parent_frame)
    scrollable_frame = ttk.Frame(canvas)
    scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Canvas inside the parent, not the scrollable frame
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a window that will contain the scrollable_frame
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Adjust scroll region on configuration
    def on_frame_configure(event):
        canvas_height = canvas.winfo_height()
        frame_height = scrollable_frame.winfo_reqheight()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Hide or show scrollbar based on content size
        if frame_height <= canvas_height:
            scrollbar.pack_forget()  # Hide scrollbar if content fits within the canvas
        else:
            scrollbar.pack(side="right", fill="y")  # Show scrollbar if content overflows

    scrollable_frame.bind("<Configure>", on_frame_configure)

    # Mouse wheel event handler
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # Bind and unbind scroll with focus
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mouse_wheel))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

    return canvas, scrollable_frame


canvas, scrollable_frame = create_scrollable_frame(main_frame)
r_canvas, r_scrollable_frame = create_scrollable_frame(rightside_frame)




## 각 dlc의 도전과제 진척도를 보여줄 progress bar 설정 함수 ##
def create_styles():
    style = ttk.Style()
    style.theme_use('vista')  # 'xpnative', 'default', 'clam', 'alt', 'classic' 중 선택 가능
    style.configure('Red.Horizontal.TProgressbar', background='red', thickness=10)
    style.configure('Orange.Horizontal.TProgressbar', background='orange', thickness=10)
    style.configure('Green.Horizontal.TProgressbar', background='green', thickness=10)

def create_progress_bar(parent, value):
    create_styles()  # 스타일 초기 설정
    progress_var = tk.DoubleVar(value=value)
    progress_bar = ttk.Progressbar(parent, variable=progress_var, length=50, mode='determinate', style='Horizontal.TProgressbar')
    text_var = tk.StringVar()
    progress_label = tk.Label(parent, textvariable=text_var)
    update_progress_text(progress_var, text_var, progress_label)  # 초기 텍스트 업데이트
    

    # 값 변경 감지
    progress_var.trace_add("write", lambda *_: update_progress_text(progress_var, text_var, progress_label))
    progress_var.trace_add("write", lambda *_: update_progress_color(progress_var, progress_bar))

    return progress_bar, progress_var, progress_label, text_var

def update_progress_color(progress_var, progress_bar):
    value = progress_var.get()
    if value <= 20:
        progress_bar['style'] = 'Red.Horizontal.TProgressbar'
    elif value <= 60:
        progress_bar['style'] = 'Orange.Horizontal.TProgressbar'
    else:
        progress_bar['style'] = 'Green.Horizontal.TProgressbar'

def update_progress_text(progress_var, text_var, label):
    current_value = progress_var.get()
    text_var.set(f"{int(current_value)}%")

    if int(current_value) == 100:
        label.config(fg='blue', font=("Helvetica", 9, 'bold'))  # 파란색과 굵은 폰트로 변경
    else:
        label.config(fg='black', font=("Helvetica", 9, 'normal'))  # 기본 설정으로 복구

def update_progress_for_keyword(keyword):
    """Update progress bar and text for a specific keyword."""
    total_items = keyword_item_count.get(keyword, 0)
    checked_items = keyword_checked_count.get(keyword, 0)
    if total_items > 0:
        progress_percentage = (checked_items / total_items) * 100
    else:
        progress_percentage = 0

    var[keyword].set(progress_percentage)  # Set the progress variable
    update_progress_color(var[keyword], bar[keyword])  # Update the color
    update_progress_text(var[keyword], label_text_var[keyword], label[keyword])  # Pass the correct StringVar for text updates






# 필터 버튼의 그라데이션 효과를 생성하는 함수
def create_gradient(width, height, color1, color2, color3=None):
    """Generate a horizontal gradient between two or three colors."""
    gradient = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(gradient)

    # Convert color strings to RGB tuples
    color1 = ImageColor.getrgb(color1)
    color2 = ImageColor.getrgb(color2)

    if color3 is None:
        # Create a gradient between color1 and color2
        for x in range(width):
            r = int(color1[0] * (1 - x / (width - 1)) + color2[0] * (x / (width - 1)))
            g = int(color1[1] * (1 - x / (width - 1)) + color2[1] * (x / (width - 1)))
            b = int(color1[2] * (1 - x / (width - 1)) + color2[2] * (x / (width - 1)))
            draw.line([(x, 0), (x, height)], fill=(r, g, b))
    
    elif color3.lower() == "split":
        # Fill the gradient with color1 and color3 without gradient effect
        draw.rectangle([(0, 0), (width // 3, height)], fill=color1, outline=None)
        draw.rectangle([(width // 3, 0), (width, height)], fill=color2, outline=None)

    elif color3.lower() == "falcom":
        draw.rectangle([(0, 0), (width, height // 4)], fill="#F4C5DA", outline=None)
        draw.rectangle([(0, height // 4), (width, height // 4 * 2)], fill="#F7F2AB", outline=None)
        draw.rectangle([(0, height // 4 * 2), (width, height // 4 * 3)], fill="#C5E7AB", outline=None)
        draw.rectangle([(0, height // 4 * 3), (width, height)], fill="#AFDDF1", outline=None)

    elif color3.lower() == "v_liberty":
        draw.rectangle([(0, 0), (width, height // 7)], fill="#45eefc", outline=None)
        draw.rectangle([(0, height // 7), (width, height // 7 * 2)], fill="#fff227", outline=None)
        draw.rectangle([(0, height // 7 * 2), (width, height )], fill="#ff51ba", outline=None)
    
    else:
        # Convert color string to RGB tuple
        color3 = ImageColor.getrgb(color3)

        # Calculate the width for each color
        color_width = width // 5

        # Create gradients between all three colors
        for x in range(width):
            if x < color_width:
                # Gradient from color1 to color3
                r = int(color1[0] * (1 - x / (color_width - 1)) + color3[0] * (x / (color_width - 1)))
                g = int(color1[1] * (1 - x / (color_width - 1)) + color3[1] * (x / (color_width - 1)))
                b = int(color1[2] * (1 - x / (color_width - 1)) + color3[2] * (x / (color_width - 1)))
            elif x < color_width * 4:
                # Solid color3
                r, g, b = color3
            else:
                # Gradient from color3 to color2
                r = int(color3[0] * (1 - (x - color_width * 4) / (color_width - 1)) + color2[0] * ((x - color_width * 4) / (color_width - 1)))
                g = int(color3[1] * (1 - (x - color_width * 4) / (color_width - 1)) + color2[1] * ((x - color_width * 4) / (color_width - 1)))
                b = int(color3[2] * (1 - (x - color_width * 4) / (color_width - 1)) + color2[2] * ((x - color_width * 4) / (color_width - 1)))

            draw.line([(x, 0), (x, height)], fill=(r, g, b))

    return ImageTk.PhotoImage(gradient)


# 버튼의 그래디언트 배경색 객체 저장
gradient_set1 = [0] * len(FILTER_KEYWORDS)
gradient_set2 = [0] * len(FILTER_KEYWORDS2)
gradient_set3 = [0] * len(FILTER_KEYWORDS3)

# 각 버튼의 폰트 색상 정보
B = 'black'; W = 'white'; G = 'light green' 
fg_set1 = [B, B, B, W, W, W]
fg_set2 = [W, B, B, W, W, B, W, W, G]
fg_set3 = [W, B, W, W, B, B, W, W, W, B, B, B]

# 1행 버튼 배경객체 저장
gradient_set1[0] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#f0b405", "#f86873", None)       # Respect V
gradient_set1[1] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#ff6f1b", "#3b89b6", None)       # EX1
gradient_set1[2] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#E18254", "#BA3955", "#FFFFFF")  # EX2
gradient_set1[3] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#7527EC", "#7527EC", "#9237FF")  # EX3
gradient_set1[4] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#be1207", "#270300", None)       # EX4
gradient_set1[5] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#ffa100", "#014e96", "split")    # EX5

# 2행 버튼 배경객체 저장
gradient_set2[0] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#3940af", "#26a7b7", None)       # Trilogy
gradient_set2[1] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#6d71f6", "#DC48A1", None)       # Technica
gradient_set2[2] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#FFD3B6", "#ACE1FF", "#FFFDBB")  # Technica2
gradient_set2[3] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#030074", "#2066ff", None)       # Technica3
gradient_set2[4] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#291010", "#BD234B", None)       # Black Square
gradient_set2[5] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#FFFFFF", "#dcaf13", None)       # ClassiQai
gradient_set2[6] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#232323", "#979797", None)       # Link Disc
gradient_set2[7] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#000", "#24190e", "#f0ab1e")     # Portable3
gradient_set2[8] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#727b79", "#141714", None)       # Technica Q&Tune

# 3행 버튼 배경객체 저장
gradient_set3[0] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#51A9BF", "#0A2739", "#3A6891")  # Groove Coaster
gradient_set3[1] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#000", "#73cbc4", "#FFF")        # Cytus
gradient_set3[2] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#3f4247", "#3f4247", "#757360")  # Deemo
gradient_set3[3] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#433C3D", "#433C3D", "#000")     # Girl's Frontier
gradient_set3[4] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#FFA600", "#FFA600", "#ECC021")  # Chunithm
gradient_set3[5] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#4F4B35", "#7A6F50", "#B79D64")  # ESTimate
gradient_set3[6] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#012a4a", "#c2d500", "#009fe0")  # Nexon
gradient_set3[7] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#ffde00", "#e100e9", None)       # Muse Dash
gradient_set3[8] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#37539f", "#0c1f5d", None)       # EZ2ON
gradient_set3[9] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#fc8114", "#b4ed5e", "#ede55f")  # Maple Story
gradient_set3[10] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#000000", "#000000", "falcom")  # Falcom

gradient_set3[11] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#000000", "#000000", "v_liberty")  # V Liberty 


## 설명 칸에 띄울 툴팁 설정 ##
class ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        if self.tip_window or not tip_text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 210
        y = y + cy + self.widget.winfo_rooty()
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        # Set the wraplength for text wrapping and configure colors
        label = tk.Label(tw, text=tip_text, background="#FFFFCC", foreground="black",
                         borderwidth=2, relief="solid", wraplength=300, justify=tk.LEFT)  # wraplength in pixels
        label.pack(ipadx=4, ipady=4)

    def hide_tip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None






# 체크박스에 체크된 항목들 갯수 카운트 후 텍스트 갱신
def update_checked_count():
    checked_count = sum(1 for item in data if item["checked"])
    checked_count_label.config(text=f"내가 클리어한 도전과제 갯수: {checked_count}")


    

def update_item(idx):
    if idx in item_frames:
        frame = item_frames[idx]
        if data[idx]["checked"]:
            frame.config(bg="gray")  # Change the background color of the frame to gray
            for child in frame.winfo_children():
                child.config(bg="gray")
        else:
            frame.config(bg="SystemButtonFace")  # Revert to default background color
            for child in frame.winfo_children():
                child.config(bg="SystemButtonFace")
    # else:
        # print(f"No frame found for index {idx}. Ensure that item frames are initialized before updating.")
        

# 데이터셋 정보 출력 함수
def update_items(filter_keyword):

    # 초기화
    keyword_item_count.clear()
    keyword_checked_count.clear()

    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    item_labels.clear()
    item_frames.clear()  # Ensure you initialize this dictionary at the start
    tool_tips.clear()
    
    for idx, item in enumerate(data):
        if filter_keyword == "All" or item["keyword"] == filter_keyword:
            frame = tk.Frame(scrollable_frame)
            frame.grid(row=idx, column=0, sticky="ew")
            item_frames[idx] = frame  # Store the frame

            # 항목 수 및 체크된 항목 수 업데이트
            keyword = item["keyword"]
            keyword_item_count[keyword] = keyword_item_count.get(keyword, 0) + 1
            if item["checked"]:
                keyword_checked_count[keyword] = keyword_checked_count.get(keyword, 0) + 1

            # 데이터 이미지 출력 설정
            img = Image.open(item["image"])
            img = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=img, bg="SystemButtonFace")
            label.image = img  # Keep a reference!
            label.grid(row=0, column=0, padx=5, pady=0, sticky="w")
            item_labels[idx] = label

            # DLC 정보 (키워드) 출력
            keyword_label = tk.Label(frame, text=item["keyword"], width=5, bg="SystemButtonFace")
            keyword_label.grid(row=0, column=1, padx=5, pady=0, sticky="w")

            # 이름 출력
            name_label = tk.Label(frame, text=item["name"], width=15, bg="SystemButtonFace", wraplength=100)  # Adjust wraplength as needed
            name_label.grid(row=0, column=2, padx=5, pady=0, sticky="w")

            # 설명 출력
            description_label = tk.Label(frame, text=item["description"], width=39, bg="SystemButtonFace", wraplength=250)
            description_label.grid(row=0, column=3, padx=5, pady=0, sticky="w")

            #툴팁 설정
            tool_tip = ToolTip(description_label)
            tool_tips[idx] = tool_tip
            description_label.bind("<Enter>", lambda e, idx=idx, item=item: tool_tips[idx].show_tip(item["caption"]))
            description_label.bind("<Leave>", lambda e, idx=idx: tool_tips[idx].hide_tip())
            
            var = tk.BooleanVar(value=item["checked"])
            var.trace_add("write", lambda *args, idx=idx: on_checkbox_click(idx))
            chk = tk.Checkbutton(frame, variable=var, bg="SystemButtonFace")
            chk.grid(row=0, column=4, padx=5, pady=0, sticky="w")
            checkbox_vars[idx] = var
            update_item(idx)
    
    canvas.yview_moveto(0)






def on_checkbox_click(idx):

    data[idx]["checked"] = not data[idx]["checked"]
    update_item(idx)
    update_checked_count()
    save_state()

    update_keyword_counts(data[idx]["keyword"], data[idx]["checked"])
    update_progress_for_keyword(data[idx]["keyword"])



def update_keyword_counts(keyword, checked):
    if checked:
        keyword_checked_count[keyword] = keyword_checked_count.get(keyword, 0) + 1
    else:
        keyword_checked_count[keyword] = keyword_checked_count.get(keyword, 0) - 1


def update_progress(index, checked):
    # index는 체크박스의 인덱스, checked는 체크 상태
    keyword = list(keyword_item_count.keys())[index]
    if checked:
        keyword_checked_count[keyword] += 1
    else:
        keyword_checked_count[keyword] -= 1

    # 프로그레스 업데이트
    progress = keyword_checked_count[keyword] / keyword_item_count[keyword] * 100
    var[keyword].set(progress)



# 필터 버튼 기능 구현함수
def filter_items(filter_keyword):
    if filter_keyword == "Unchecked Only":     # "Unchecked Only" 필터링 버튼을 클릭했을 때의 동작
        filter_unchecked_items()
    else:                                      # 스크롤 가능한 프레임에 있는 모든 위젯들을 제거
        for widget in scrollable_frame.winfo_children():   
            widget.destroy()                    # item_labels와 item_frames 딕셔너리 초기화
        item_labels.clear()                         
        item_frames.clear()
        tool_tips.clear()

        for idx, item in enumerate(data):       # 데이터를 반복하면서 각 항목에 대한 정보를 보여주는 위젯을 생성
            if filter_keyword == "All" or item["keyword"] == filter_keyword:
                frame = tk.Frame(scrollable_frame)
                frame.grid(row=idx, column=0, sticky="ew")
                item_frames[idx] = frame

                img = Image.open(item["image"])
                img = ImageTk.PhotoImage(img)
                label = tk.Label(frame, image=img, bg="SystemButtonFace")
                label.image = img  
                label.grid(row=0, column=0, padx=5, pady=0, sticky="w")
                item_labels[idx] = label

                keyword_label = tk.Label(frame, text=item["keyword"], width=5, bg="SystemButtonFace")
                keyword_label.grid(row=0, column=1, padx=5, pady=0, sticky="w")

                name_label = tk.Label(frame, text=item["name"], width=15, bg="SystemButtonFace", wraplength=100)
                name_label.grid(row=0, column=2, padx=5, pady=0, sticky="w")

                description_label = tk.Label(frame, text=item["description"], width=40, bg="SystemButtonFace", wraplength=250)
                description_label.grid(row=0, column=3, padx=5, pady=0, sticky="w")

                #툴팁 설정
                tool_tip = ToolTip(description_label)
                tool_tips[idx] = tool_tip
                description_label.bind("<Enter>", lambda e, idx=idx, item=item: tool_tips[idx].show_tip(item["caption"]))
                description_label.bind("<Leave>", lambda e, idx=idx: tool_tips[idx].hide_tip())

                var = tk.BooleanVar(value=item["checked"])
                var.trace_add("write", lambda *args, idx=idx: on_checkbox_click(idx))
                chk = tk.Checkbutton(frame, variable=var, bg="SystemButtonFace")
                chk.grid(row=0, column=4, padx=5, pady=0, sticky="w")
                checkbox_vars[idx] = var
                update_item(idx)
                canvas.yview_moveto(0)
    canvas.yview_moveto(0)

# 상태 저장 함수
def save_state():
    with open(STATE_FILE, 'w') as file:
        states = [item["checked"] for item in data]
        json.dump(states, file)
    # print("Saved states:", states)  # Debugging output

# 상태 불러오기 함수
def load_state():
    try:
        with open(STATE_FILE, 'r') as file:
            checked_states = json.load(file)
            # print("Loaded states:", checked_states)  # Debugging output
        for idx, checked in enumerate(checked_states):
            data[idx]["checked"] = checked
            update_item(idx)
        update_checked_count()
    except FileNotFoundError:
        print("State file not found, initializing with default states.")


# Initialize data
checkbox_vars = {}
item_labels = {}
item_overlays = {}
item_frames = {}
bar = {}
var = {}
label = {}
label_text_var = {}
keyword_item_count = {}  # 딕셔너리 초기화
keyword_checked_count = {}

checkbox_var = {}
checkbox_widgets = {}
tool_tips = {}

load_state()
update_items("All")





### 필터 버튼 생성 ###

## All 버튼
all_btn = tk.Button(corner_frame, 
                    text="All", 
                    command=lambda: filter_items("All"))
all_btn.pack(side="left", padx=5, pady=5, anchor='nw')

# 체크박스 필터 버튼
unchecked_btn = tk.Button(corner_frame, 
                        text="미완료", 
                        command=lambda: filter_items("Unchecked Only"))
unchecked_btn.pack(side="left", padx=5, pady=5, anchor='nw')

## 1행 버튼
all_i = 0
i = 0
for keyword in FILTER_KEYWORDS:
    btn = tk.Button(r_scrollable_frame, 
                    text=keyword, 
                    command=lambda keyword=keyword: filter_items(keyword),
                    image=gradient_set1[i],
                    compound="center",
                    fg=fg_set1[i], 
                    font=("Helvetica", 8, "bold"))
    btn.grid(row=i, column=0, sticky='w')
    i += 1


## 2행 버튼
all_i += i
i = 0
for keyword in FILTER_KEYWORDS2:
    btn = tk.Button(r_scrollable_frame, 
                    text=keyword, 
                    background='white',
                    command=lambda keyword=keyword: filter_items(keyword),
                    image=gradient_set2[i],
                    compound="center",
                    fg=fg_set2[i], 
                    font=("Helvetica", 8, "bold"))
    btn.grid(row=i+all_i, column=0, sticky='w')
    i += 1


## 3행 버튼
all_i += i
i = 0
for keyword in FILTER_KEYWORDS3:
    btn = tk.Button(r_scrollable_frame, 
                    text=keyword, 
                    command=lambda keyword=keyword: filter_items(keyword),
                    image=gradient_set3[i],
                    compound="center",
                    fg=fg_set3[i], 
                    font=("Helvetica", 8, "bold"))
    btn.grid(row=i+all_i, column=0, sticky='w')
    i += 1


# 키워드마다 해당하는 프로그래스 바와 퍼센티지를 출력하는 코드
for i, keyword in enumerate(keyword_item_count.keys()):
    initial_progress = keyword_checked_count.get(keyword, 0) / keyword_item_count[keyword] * 100
    bar[keyword], var[keyword], label[keyword], label_text_var[keyword] = create_progress_bar(r_scrollable_frame, initial_progress)
    bar[keyword].grid(row=i, column=1, sticky='w', padx=2)
    label[keyword].grid(row=i, column=2, padx=2)


    # 체크박스 상태 변경에 따른 이벤트 핸들러 연결
    checkbox = tk.Checkbutton(r_scrollable_frame, command=lambda i=i: update_progress(i, checkbox_var[i].get()))
    # checkbox.grid(row=i, column=0)
    checkbox_var[i] = tk.BooleanVar()
    checkbox['variable'] = checkbox_var[i]



root.mainloop()
