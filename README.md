# download-line-albums
##### description

- download all line group's albums using pyautogui

##### installation

- ```
  pip install -r requirements.txt
  ```

##### run

1. fill the setting in download-line-albums.py

   ```
   SAVE_DIR="C:/your_save_path/"
   ALBUMS_NAME='your album name'
   ALBUM_FROM=1 #download from album index
   ALBUM_DOWNLOAD_NUM=10 #download album num
   ALBUM_POS=[1035,187] #照片標題 position
   ALBUM_FUNC_POS=[2547,51]   #...功能列 position
   ALBUM_FUNC_POS_RENAME=[ALBUM_FUNC_POS[0]-40, ALBUM_FUNC_POS[1]+15]
   ALBUM_SAVE_POS=[2497,52] #儲存全部
   ```

2. open line app, select the ablum and maxmize window

3. run download-line-albums.py

   ```
   python download-line-albums.py
   ```

   

