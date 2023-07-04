import pyautogui as ag
import pyperclip
import os
import time
import re

def filter_filename(filename):
    # 定義不合法字元的正則表達式
    illegal_chars = r'[\\/]'
    # 將不合法字元替換為底線
    filtered_filename = re.sub(illegal_chars, '_', filename)
    return filtered_filename

def window_max(delaysec=0.01):
    ag.hotkey('alt', ' ', 'x')
    time.sleep(delaysec)

def window_close(delaysec=0.01):
    ag.hotkey('alt', 'F4')
    time.sleep(delaysec)

def copy_clipboard():
    ag.hotkey('ctrl', 'a')
    time.sleep(.01)
    ag.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def clip_write(str):
    pyperclip.copy(str)
    #pyperclip.paste()
    ag.hotkey('ctrl', 'v')

def clickpos(ary, delaysec=0.01):
    #print("click {}, {}".format(ary[0], ary[1]))
    ag.moveTo(ary[0], ary[1])
    ag.click(ary[0], ary[1])
    time.sleep(delaysec)

def press(key, delaysec=0.01):
    ag.press(key)
    time.sleep(delaysec)

SAVE_DIR="C:/your_save_path/"
ALBUMS_NAME='your album name'
ALBUM_FROM=1 #download from album index
ALBUM_DOWNLOAD_NUM=10 #download album num
ALBUM_POS=[1035,187] #照片標題 position
ALBUM_FUNC_POS=[2547,51]   #...功能列 position
ALBUM_FUNC_POS_RENAME=[ALBUM_FUNC_POS[0]-40, ALBUM_FUNC_POS[1]+15]
ALBUM_SAVE_POS=[2497,52] #儲存全部

def make_album_dir(album_name):
    # 組合目錄路徑
    directory = os.path.join(SAVE_DIR, album_name)
    directory = directory.replace("/", "\\")
    # 檢查目錄是否存在，若不存在則創建目錄
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("目錄已成功創建：", directory)
    else:
        print("目錄已存在：", directory)
    return directory

def get_album_name():
    clickpos(ALBUM_FUNC_POS,3)
    clickpos(ALBUM_FUNC_POS_RENAME,2)
    pyperclip.copy('ERROR_ALBUM')
    album_name = copy_clipboard()
    album_name = filter_filename(album_name)
    print(album_name)
    if album_name=='ERROR_ALBUM':
        print('something error.')
        quit()
    window_close()
    return album_name

def wait_pic(picfile):
    print("wait " + picfile)
    while True:
        pos = ag.locateCenterOnScreen(picfile)
        if pos != None:
            return [pos.x, pos.y]
    return None

def wait_download():
    while True:
        pos = ag.locateCenterOnScreen('download_completed.png')
        if pos != None:
            return [pos.x, pos.y]
    return None

def save_album(album_dir):
    clickpos(ALBUM_SAVE_POS)
    #ag.typewrite(album_dir)
    clip_write(album_dir)
    press('enter', 0.1) #輸入路徑, 開啟到該目錄
    press('enter') #關閉save file dialog
    print('wait_download...')
    pos = wait_download()
    print('wait_download completed...')
    clickpos(pos)
    window_close() #關閉popup msgbox
    #clickpos(pos)
    time.sleep(1)
    window_close() #關閉album window

def find_window(title):
    # 取得所有正在運行的視窗
    windows = ag.getAllWindows()
	for window in windows:
		#print(window)
		if window.title == title:
			return window
	return None
	
def save_albums():
	window = find_window(ALBUMS_NAME)
	if window == None:
		print("window {} not found!".format(ALBUMS_NAME))
		quit()
		
	print(window)
    window.activate()
	press('home')
	press('pagedown')

	# locate to album #ALBUM_FROM
	for i in range(1, ALBUM_FROM):
		press('down')
	
	for i in range(0, ALBUM_DOWNLOAD_NUM):
		clickpos(ALBUM_POS)
		window_max()
		album_name = get_album_name()
		album_dir = make_album_dir(album_name)
		save_album(album_dir)
		#window.activate()
		time.sleep(3)
		#wait_pic('album_list.png')
		press('down')

#main
save_albums()
ag.alert('save albums completed!')

