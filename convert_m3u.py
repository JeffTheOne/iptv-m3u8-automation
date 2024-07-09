import requests

TXT_URL = 'https://raw.githubusercontent.com/zwc456baby/iptv_alive/master/live.txt'
M3U8_FILE_PATH = 'live.m3u8'

def download_txt(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.text

def convert_to_m3u8(txt_content):
    # Placeholder function to perform any necessary conversion
    # Here, just pass through the content, but you can modify it as needed
    return txt_content

def save_m3u8(content, path):
    with open(path, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    txt_content = download_txt(TXT_URL)
    m3u8_content = convert_to_m3u8(txt_content)
    save_m3u8(m3u8_content, M3U8_FILE_PATH)