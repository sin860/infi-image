import requests
import re
import webbrowser
webbrowser.open('https://t.me/SIN_PHP')
def image_info(image):
    
    url = "https://www.pic2map.com/includes/upload.php"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json",
        'X-Requested-With': "XMLHttpRequest",
    }
    payload = {'private': '1'}
    
    try:
        with open(image, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, data=payload, files=files, headers=headers)

            infores = response.text.strip()  
            _url = f'{infores}'
            api= requests.get(_url).text

            brand = re.search(r'Brand:</span><span class="dvalue">(.*?)</span>', api).group(1)
            model = re.search(r'Model:</span><span class="dvalue">(.*?)</span>', api).group(1)
            shutter_speed = re.search(r'Shutter:</span><span class="dvalue">(.*?)</span>', api).group(1).split(' ')[0]
            f_number = re.search(r'F Number:</span><span class="dvalue">(.*?)</span>', api).group(1)
            iso = re.search(r'ISO Speed:</span><span class="dvalue">(.*?)</span>', api).group(1)
            focal_length = re.search(r'Focal Length:</span><span class="dvaluex">(.*?)</span>', api).group(1)
            image_size = re.search(r'Image Size:</span><span class="dvalue">(.*?)</span>', api).group(1)
            resolution = re.search(r'Resolution:</span><span class="dvalue">(.*?)</span>', api).group(1)
            date = re.search(r'Date:</span><span class="dvalue">(.*?)</span>', api).group(1)
            time = re.search(r'Time:</span><span class="dvalue">(.*?)</span>', api).group(1)
            
            gps_info = "No GPS information was found." if re.search(r'No GPS information was found...', api) else "GPS information available."

            print(f"Brand: {brand}")
            print(f"Model: {model}")
            print(f"Shutter Speed: {shutter_speed}")
            print(f"F Number: {f_number}")
            print(f"ISO: {iso}")
            print(f"Focal Length: {focal_length}")
            print(f"Image Size: {image_size}")
            print(f"Resolution: {resolution}")
            print(f"Date: {date}")
            print(f"Time: {time}")
            print(f"GPS Location: {gps_info}")
            print('DEVLOPER :- @SIN_php')

    except FileNotFoundError:
        print("مسار ملف غير صحيح ")
    except requests.exceptions.RequestException as e:
        print(f"{e}")
    except AttributeError:
        print("هناك خطاء راجع المطور")
    except Exception as e:
        print(f'{e}')    
image_info(input('Put the image path : '))
