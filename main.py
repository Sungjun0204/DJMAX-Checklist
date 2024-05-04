import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageColor
import json
import data as dlc

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 900
TOP_FRAME_HEIGHT = 100
FILTER_FRAME_HEIGHT = 50
FILTER_FRAME_HEIGHT2 = 50
FILTER_FRAME_HEIGHT3 = 50
FILTER_KEYWORDS = ["RPTV", "EX1", "EX2", "EX3", "EX4", "EX5"]
FILTER_KEYWORDS2 = ["TR", "TECH", "TECH2", "TECH3", "BLSQ", 
                   "CLQI", "LINK", "PTB3", "T&Q"]
FILTER_KEYWORDS3 = ["GRUV", "Cytus", "DEEMO", "GLFR", "CHU", "ESTI",
                    "NEXON", "MUDS", "EZ2ON", "MAPLE", "FLCM"]
STATE_FILE = 'checkboxstates5.json'

# Define button size
BTN_WIDTH = 40  # Example width
BTN_HEIGHT = 20  # Example height




# Initialize Tkinter
root = tk.Tk()
root.title("DJMAX RESPECT V 도전과제 체크리스트")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Top Frame
top_frame = tk.Frame(root, height=TOP_FRAME_HEIGHT, bg='grey')
top_frame.pack(fill='x', side='top')

# Label to display checked item count
checked_count_label = tk.Label(top_frame, text="Checked Items: 0")
checked_count_label.pack(pady=20)

# Filter Frame
filter_frame = tk.Frame(root, height=FILTER_FRAME_HEIGHT)
filter_frame.pack(fill='x', pady=(0, 5))
filter_frame2 = tk.Frame(root, height=FILTER_FRAME_HEIGHT2)
filter_frame2.pack(fill='x', pady=(0, 5))
filter_frame3 = tk.Frame(root, height=FILTER_FRAME_HEIGHT3)
filter_frame3.pack(fill='x', pady=(0, 5))

# Scrollable Frame
canvas = tk.Canvas(root)
scrollable_frame = tk.Frame(canvas)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Mouse Wheel Scrolling Function
def on_mouse_wheel(event):
    if root.tk.call('tk', 'windowingsystem') == 'aqua':
        canvas.yview_scroll(-1*(event.delta), "units")
    else:
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Bind the mouse wheel event to the on_mouse_wheel function
canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # For Windows and macOS
canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # For Linux, scroll up
canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))  # For Linux, scroll down



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
B = "black"; W = "white"; G = "light green"    
fg_set1 = [B, B, B, W, W, W]
fg_set2 = [W, B, B, W, W, B, W, W, G]
fg_set3 = [W, B, W, W, B, B, W, W, W, B, B]

# 1행 버튼 배경객체 저장
gradient_set1[0] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#f0b405", "#f86873", None)       # Respect V
gradient_set1[1] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#ff6f1b", "#3b89b6", None)       # EX1
gradient_set1[2] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#E18254", "#BA3955", "#FFFFFF")  # EX2
gradient_set1[3] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#7527EC", "#7527EC", "#9237FF")  # EX3
gradient_set1[4] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#be1207", "#270300", None)       # EX4
gradient_set1[5] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#ffa100", "#014e96", "split")    # EX5

gradient_set2[0] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#3940af", "#26a7b7", None)       # Trilogy
gradient_set2[1] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#6d71f6", "#DC48A1", None)       # Technica
gradient_set2[2] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#FFD3B6", "#ACE1FF", "#FFFDBB")  # Technica2
gradient_set2[3] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#030074", "#2066ff", None)       # Technica3
gradient_set2[4] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#291010", "#BD234B", None)       # Black Square
gradient_set2[5] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#FFFFFF", "#dcaf13", None)       # ClassiQai
gradient_set2[6] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#232323", "#979797", None)       # Link Disc
gradient_set2[7] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#000", "#24190e", "#f0ab1e")     # Portable3
gradient_set2[8] = create_gradient(BTN_WIDTH, BTN_HEIGHT, "#727b79", "#141714", None)       # Technica Q&Tune

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




# 데이터셋 초기화
data = dlc.final_data

# Functions
def update_checked_count():
    checked_count = sum(1 for item in data if item["checked"])
    checked_count_label.config(text=f"Checked Items: {checked_count}")

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
        


def update_items(filter_keyword):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    item_labels.clear()
    item_frames.clear()  # Ensure you initialize this dictionary at the start
    
    for idx, item in enumerate(data):
        if filter_keyword == "All" or item["keyword"] == filter_keyword:
            frame = tk.Frame(scrollable_frame)
            frame.grid(row=idx, column=0, sticky="ew")
            item_frames[idx] = frame  # Store the frame

            img = Image.open(item["image"])
            img = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=img, bg="SystemButtonFace")
            label.image = img  # Keep a reference!
            label.grid(row=0, column=0, padx=5, pady=0, sticky="w")
            item_labels[idx] = label

            keyword_label = tk.Label(frame, text=item["keyword"], width=5, bg="SystemButtonFace")
            keyword_label.grid(row=0, column=1, padx=5, pady=0, sticky="w")

            # Apply wraplength to the name label
            name_label = tk.Label(frame, text=item["name"], width=15, bg="SystemButtonFace", wraplength=100)  # Adjust wraplength as needed
            name_label.grid(row=0, column=2, padx=5, pady=0, sticky="w")

            description_label = tk.Label(frame, text=item["description"], width=40, bg="SystemButtonFace", wraplength=250)
            description_label.grid(row=0, column=3, padx=5, pady=0, sticky="w")

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

def filter_items(filter_keyword):
    update_items(filter_keyword)
    canvas.yview_moveto(0)  # Move the scrollbar to the top

def save_state():
    with open(STATE_FILE, 'w') as file:
        states = [item["checked"] for item in data]
        json.dump(states, file)
    # print("Saved states:", states)  # Debugging output

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
load_state()
update_items("All")


### 필터 버튼 생성 ###

## All 버튼
all_btn = tk.Button(filter_frame, 
                    text="All", 
                    command=lambda: filter_items("All"))
all_btn.pack(side="left", padx=10)

## 1행 버튼
i = 0
for keyword in FILTER_KEYWORDS:
    btn = tk.Button(filter_frame, 
                    text=keyword, 
                    command=lambda keyword=keyword: filter_items(keyword), 
                    image=gradient_set1[i],
                    compound="center",
                    fg=fg_set1[i], 
                    font=("Helvetica", 8, "bold"))
    btn.image = gradient_set1[i]
    btn.pack(side="left", padx=0)
    i += 1

## 2행 버튼
i = 0
for keyword in FILTER_KEYWORDS2:
    btn = tk.Button(filter_frame2, 
                    text=keyword, 
                    command=lambda keyword=keyword: filter_items(keyword),
                    image=gradient_set2[i],
                    compound="center",
                    fg=fg_set2[i], 
                    font=("Helvetica", 8, "bold"))
    btn.pack(side="left", padx=0)
    i += 1

## 3행 버튼
i = 0
for keyword in FILTER_KEYWORDS3:
    btn = tk.Button(filter_frame3, 
                    text=keyword, 
                    command=lambda keyword=keyword: filter_items(keyword),
                    image=gradient_set3[i],
                    compound="center",
                    fg=fg_set3[i], 
                    font=("Helvetica", 8, "bold"))
    btn.pack(side="left", padx=0)
    i += 1

root.mainloop()
