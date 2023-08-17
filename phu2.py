from selenium import webdriver
import pyautogui
import time
from undetected_chromedriver import ChromeOptions
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from webdriver_manager.chrome import ChromeDriverManager
# Chuỗi chứa từ khóa bạn muốn tìm kiếm trong tiêu đề cửa sổ
import pygetwindow as gw
time.sleep(10)
def laytoken():
    try:
        chrome_driver_path = r'chromedriver.exe'
        # Đường dẫn đến thư mục profile của Chrome
        chrome_profile_path = r'd2'
        # Khởi tạo trình điều khiển cho trình duyệt Chrome
        chrome_options = ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'--user-data-dir={chrome_profile_path}')       
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disk-cache-size=1")
        driverchrome = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        #driverchrome.minimize_window()
        driverchrome.get('https://1stcaptcha.com/')
        driverchrome.delete_all_cookies()
        wait1 = WebDriverWait(driverchrome, 20)
        trail = wait1.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/div/app-home/div/div[1]/app-home-topcontent/div/div[1]/div[2]')))
        trail.click()
        web = wait1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.recap-sub:nth-child(1) input')))
        web.send_keys('https://cuty.io/Kofr')
        time.sleep(1)
        # Chạy trình duyệt ẩn danh (tùy chọn)
        webkey = wait1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.recap-sub:nth-child(2) input')))
        webkey.send_keys('6LeupnoeAAAAABuQhk4oCY34s4xTJND0U2u77Z2g')
        time.sleep(1)
        resolve = wait1.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/div/app-home/div/div[1]/app-home-topcontent/div/app-home-trial/div/form/div/button')))
        resolve.click()
        time.sleep(7)
        time.sleep(25)
        def checkgiaire(driver,iframe):# Chờ một lúc để trang tải hoàn toàn
            time.sleep(5)
            iframe_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,iframe ))
            )
            # Chuyển qua iframe
            driverchrome.switch_to.frame(iframe_element)
            # Tìm phần tử input có id là "recaptcha-token"
            input_element = driver.find_element(By.XPATH, "/html/body/input")
            # Lấy giá trị của thuộc tính "value" từ phần tử input
            value = input_element.get_attribute("value")
            print(value)
            num_characters = len(value)
            # Kiểm tra nếu num_characters bằng 0
            if num_characters > 1600 :
                print("response_value không có ký tự nào")
                driver.refresh()
                return False
            else:
                print(f"Số lượng ký tự trong response_value:{num_characters}")
                return True
        #driver.save_screenshot('screenshot.png')
        while not checkgiaire(driver=driverchrome, iframe="/html/body/div[2]/div[4]/iframe"):
            pass
        time.sleep(2)
        driverchrome.switch_to.default_content()
        resolve1 = wait1.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.upload > .active')))
        resolve1.click()
        while True:
            textarea_element = wait1.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/div/app-home/div/div[1]/app-home-topcontent/div/app-home-trial/div/div/textarea')))
            text_content = textarea_element.get_attribute('textContent')
            content_length = len(text_content)
            if content_length > 30:
                break # Exit the loop if 'text_content' is not None
        textarea_element =  wait1.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/div/app-home/div/div[1]/app-home-topcontent/div/app-home-trial/div/div/textarea')))
        # Get the text content of the <textarea> element
        text_content = textarea_element.get_attribute('textContent')
        # Find the starting index of the "Token" value
        start_index = text_content.find('"Token": "') + len('"Token": "')
        # Find the ending index of the "Token" value
        end_index = text_content.find('"', start_index)
        # Extract the token using the start and end indexes
        token = text_content[start_index:end_index]
        # Print the extracted token
        t = token
        time.sleep(3)
        return t 
        
    except:
        driverchrome.quit()
def an(x, y):
    # Di chuyển con trỏ chuột đến vị trí có tọa độ (x, y)
    pyautogui.moveTo(x, y, duration=1)  # duration là thời gian di chuyển (giây)
    # Hoặc có thể click chuột tại một vị trí cụ thể
    pyautogui.click(x, y)
    # Để đợi một thời gian trước khi click
    time.sleep(1)  # Đợi 1 giây
    # Để click chuột giữa (middle click)
def anr(x, y):
    # Di chuyển con trỏ chuột đến vị trí có tọa độ (x, y)
    pyautogui.moveTo(x, y, duration=1)  # duration là thời gian di chuyển (giây)
    # Click chuột tại vị trí hiện tại
    pyautogui.click()
    # Hoặc có thể click chuột tại một vị trí cụ thể
    pyautogui.click(x, y)
    # Để đợi một thời gian trước khi click
    time.sleep(1)  # Đợi 1 giây
    # Để click chuột giữa (middle click)
    pyautogui.rightClick()
for i in range(1,100):
    try:
        target_title = "About Tor — Tor Browser"
    # Lấy danh sách các cửa sổ có tiêu đề tương tự
        windows = gw.getWindowsWithTitle(target_title)
    # Kiểm tra xem có cửa sổ nào thỏa mãn không
        if windows:
            target_window = windows[0]  # Lấy cửa sổ đầu tiên trong danh sách
            new_left = 908  # Vị trí theo chiều ngang
            new_top = 0  # Vị trí theo chiều dọc
            new_width = 1012 # Kích thước rộng
            new_height = 991  # Kích thước cao
            target_window.moveTo(new_left, new_top)  # Di chuyển cửa sổ
            target_window.resizeTo(new_width, new_height)  #
            # Kích hoạt cửa sổ sử dụng pyautogu
            target_window.activate()
    except:
        pass
    time.sleep(12)
    # Chuỗi chứa từ khóa bạn muốn tìm kiếm trong tiêu đề cửa sổ
    an(1287,64)
    pyautogui.write('https://cuty.io/Kofr',interval=0.002)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(30)
    pyautogui.hotkey('F12')
    try:
        value = laytoken()
    except:
        value = laytoken()

    time.sleep(3)
    print(value)
    an(1074,971)
    time.sleep(2)
        
    js_code = f"""
    var element = document.querySelector('#g-recaptcha-response');
    var t_with_line_breaks ='{value}';
    element.removeAttribute('style');
    element.innerHTML = t_with_line_breaks;
    """
    pyautogui.write(js_code,interval=0.0002)
    time.sleep(37)
    an(1819,64)
    time.sleep(10)
    