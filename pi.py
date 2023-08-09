import pyautogui
import subprocess
import time
time.sleep(4)
def dangnhapfalre(url):
    def an(x, y):
    # Di chuyển con trỏ chuột đến vị trí có tọa độ (x, y)
        pyautogui.moveTo(x, y, duration=1)  # duration là thời gian di chuyển (giây)

        # Click chuột tại vị trí hiện tại
        pyautogui.click()

        # Hoặc có thể click chuột tại một vị trí cụ thể
        pyautogui.click(x, y)

        # Để đợi một thời gian trước khi click
        time.sleep(1)  # Đợi 1 giây

        # Để click chuột giữa (middle click)
        pyautogui.middleClick()

        # Để click chuột phải (right click)
        pyautogui.rightClick()

        # Và còn nhiều hàm khác để điều khiển chuột và bàn phím
    

# Đường dẫn đến tệp batch
    batch_file_path = r"C:\Users\NDC\Desktop\trinh\1.bat"

    # Sử dụng subprocess để chạy tệp batch
    subprocess.run([batch_file_path], shell=True)

    time.sleep(4)
    pyautogui.typewrite(url)

# Gõ Enter để kết thúc
    pyautogui.press('enter')
    


    def click_image(image_path, region, timeout=10):
        try:
            start_time = time.time()
            while time.time() - start_time < timeout:
                # Tìm vị trí của hình ảnh trong khu vực cụ thể
                location = pyautogui.locateOnScreen(image_path, region=region)
                
                if location is not None:
                    # Tính toán tọa độ tâm của hình ảnh
                    center_x = location.left + location.width / 2
                    center_y = location.top + location.height / 2
                    
                    # Click vào tâm của hình ảnh
                    pyautogui.click(center_x, center_y)
                    return True
                
                time.sleep(1)  # Đợi 1 giây trước khi tiếp tục tìm kiếm
            else:
                print("Hình ảnh không được tìm thấy trong khoảng thời gian cho phép.")
                return False
        except Exception as e:
            print("Đã xảy ra lỗi:", e)
            return False

    # Đường dẫn đến hình ảnh cần tìm và click

    # Khu vực cụ thể trên màn hình (x, y, width, height)
    region = (1736,38,81,33)

    # Gọi hàm để tìm và click vào hình ảnh trong khu vực cụ thể
    click_image(r"C:\Users\NDC\tapviet\Cap.png", region)
    time.sleep(5)
    # Khu vực cụ thể trên màn hình (x, y, width, height)
    region1 = (1461,192,56,355)
    click_image(r"C:\Users\NDC\tapviet\ookie.png", region1)
    time.sleep(5)
dangnhapfalre('https://earnbitmoon.club/')