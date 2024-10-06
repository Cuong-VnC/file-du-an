#Khai báo thư viện
import qrcode
import tkinter as tk
#Tạo hàm
def tao_qrcode():
    # Lấy link từ ô nhập
    link = entry.get()

    # Tạo mã QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make()
    anh = qr.make_image(fill_color='blue', back_color='white')

    # Hiển thị mã QR trong label
    #Lưu ảnh
    anh.save("temp_qr.png") 
    photo = tk.PhotoImage(file="temp_qr.png")
    label.config(image=photo)
    #Giữ ảnh
    label.image = photo  

# Tạo cửa sổ
window = tk.Tk()
window.title("Tạo Mã QR")

# Tạo ô nhập link
label_link = tk.Label(window, text="Nhập link:")
label_link.pack()
entry = tk.Entry(window)
entry.pack()

# Tạo nút tạo mã QR
button = tk.Button(window, text="Tạo mã QR", command=tao_qrcode)
button.pack()

# Tạo ô hiển thị mã QR
label = tk.Label(window)
label.pack()

# Khởi chạy cửa sổ
window.mainloop()