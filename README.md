# 台中必吃美食推薦網站

## 專案簡介

本網站是一個以 Flask 框架打造的台中美食推薦平台，展示多家台中在地人氣美食，包含圖片、分類、簡介、地點、價格、評分等資訊，並提供詳細頁面。專案支援本地開發與 PythonAnywhere 雲端部署。

---

## 特色功能

- 美食清單首頁展示（含圖片、分類、簡介、評分）
- 點擊美食可進入詳細介紹頁面
- 美觀的 CSS 樣式排版
- 靜態圖片本地管理，支援雲端部署
- 清楚的資料結構與模板分離

---

## 技術棧

- Python 3.x
- Flask 2.x
- Jinja2 模板引擎
- HTML5 + CSS3
- 適用於本地與 PythonAnywhere

---

## 安裝與執行

### 1. 下載專案
```
git clone <你的專案網址>
cd <專案資料夾>
```

### 2. 建立虛擬環境並安裝套件

```
python3 -m venv venvsource venv/bin/activate  
# Windows 用 venv\Scripts\activatepip install -r requirements.txt
> requirements.txt 已包含 Flask 相關依賴。
```

### 3. 專案結構

```
mysite/
├── app.py
├── data/
│   └── foods.py
├── static/
│   ├── food.1.jpg
│   ├── food.2.jpg
│   ├── food.3.jpg
│   ├── food.4.jpg
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   └── detail.html
├── requirements.txt
└── README.md
```

### 4. 放置圖片

- 請將所有美食圖片（如 food.1.jpg, food.2.jpg, ...）放在 `static/` 資料夾下。
- foods.py 的 `image` 欄位只需寫檔名（例如 `'food.1.jpg'`），**不要加 static/ 前綴**。

### 5. 執行本地伺服器

```
python app.py
```
- 預設啟動於 https://stephen950725.pythonanywhere.com/

---

## 主要檔案說明

### app.py

- Flask 主程式，負責路由與渲染模板。

### data/foods.py

- 儲存美食資料的 Python 檔案，格式如下：
```python
TAICHUNG_FOODS = [
    {
        "id": 1,
        "name": "台中肉員",
        "category": "傳統小吃",
        "description": "米其林必比登推薦的人氣老店，主打手工肉圓，外皮Q彈、內餡多汁。",
        "image": "food.1.jpg",
        "location": "台中市中區自由路二段",
        "price": "NT$40",
        "rating": 4.5
    },
    # ... 更多美食資料 ...
]
```

### static/

- 存放所有靜態資源（圖片、CSS）。

### templates/

- 存放所有 HTML 模板（base.html, index.html, detail.html）。

### style.css

- 網站主題樣式，已優化排版與圖片顯示。

---

## 重要注意事項

- **圖片路徑設定**  
  - foods.py 的 `image` 欄位只需填寫檔名（如 `'food.1.jpg'`），不要加 static/ 前綴。
  - 模板請用 `{{ url_for('static', filename=food.image) }}` 引用圖片。

- **圖片檔案必須實際存在於 static/ 目錄下**，否則會 404。

- **每次修改靜態檔案或資料後，請重啟 Flask 伺服器或在 PythonAnywhere reload 網站。**

---

## 部署到 PythonAnywhere

1. 註冊並登入 PythonAnywhere。
2. 上傳整個專案資料夾（含 static/、templates/、data/、app.py）。
3. 確認圖片已上傳到 static/ 目錄下。
4. 在 Web 設定頁設好專案目錄與 WSGI 檔案（詳見 PythonAnywhere 官方教學）。
5. 點擊「Reload」啟動網站。

---

## 常見問題排查

- **圖片無法顯示或 404：**
  - 檢查 static/ 目錄下有無圖片檔案。
  - foods.py 的 image 欄位是否只寫檔名。
  - 模板 img 標籤是否正確使用 `url_for('static', filename=food.image)`。

- **CSS 沒有生效：**
  - 確認 style.css 放在 static/ 下，並用 `{{ url_for('static', filename='style.css') }}` 引用。

- **PythonAnywhere 出現 ModuleNotFoundError: No module named 'app'：**
  - 檢查 app.py 是否在專案資料夾下，WSGI 設定檔路徑大小寫是否正確。

---

## 參考與延伸

- [Flask 官方教學](https://flask.palletsprojects.com/)
- [PythonAnywhere 部署 Flask](https://help.pythonanywhere.com/pages/Flask/)
- [readme-best-practices 範本](https://github.com/jehna/readme-best-practices)

---


**如有任何問題，聯絡作者 陳心璿。**


