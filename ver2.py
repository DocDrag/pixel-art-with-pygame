import tkinter as tk
import xy

# ดึงตำแหน่ง x y จากในไฟล์
p = xy.p

# กำหนดขนาดหน้าต่าง
width, height = 375, 500

# สร้างหน้าต่าง Tkinter
root = tk.Tk()
root.title("Display Image Pixel by Pixel")
root.geometry(f"{width}x{height}+{root.winfo_screenwidth() - (width + 50)}+100")

# สร้าง Canvas สำหรับวาดพิกเซล
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

x, y = 0, 0
count = 0

# ฟังก์ชันสำหรับวาดพิกเซลทีละจุด
def draw_pixels():
    global x, y, count
    if x < width and y < height:
        color = "#FFFFFF"  # สีขาว
        canvas.create_rectangle(p[count]["x"], p[count]["y"], p[count]["x"] + 1, p[count]["y"] + 1, fill=color, outline=color)
        
        x += 1
        if x >= width:
            x = 0
            y += 1
        
        if count < len(p) - 1:
            count += 1

        root.after(1, draw_pixels)  # เรียกฟังก์ชันนี้ซ้ำทุกๆ 1 มิลลิวินาที
    else:
        print("Drawing finished.")

# เริ่มวาดพิกเซล
draw_pixels()

# เริ่ม loop ของ Tkinter
root.mainloop()
