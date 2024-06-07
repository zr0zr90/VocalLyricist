# VocalLyricist
The "Song Maker" bot is an intelligent application capable of producing personalized songs for the user based on the words provided by the user, and designing them with the voice of their favorite artist. The bot relies on artificial intelligence techniques and natural language processing to generate songs of high quality and in the style preferred by the user.
### الصوت الكاتب
بوت "صانع الأغاني" يعتبر تطبيقًا ذكيًا ينتج أغانيًا مخصصة للمستخدم بناءً على الكلمات التي يدخلها المستخدم، ويصممها بصوت فنانه المفضل. يستخدم البوت تقنيات الذكاء الاصطناعي ومعالجة اللغة الطبيعية لإنتاج الأغاني بجودة عالية وبالأسلوب المفضل للمستخدم. احصل على أغاني شخصية واستمتع بتجربة فريدة مع بوت "صانع الأغاني".


# About

This is an intelligent bot that creates personalized songs for the user based on the words they input, using the voice of their favorite artist. The bot utilizes smart techniques to produce high-quality songs in the user's preferred style.

## Features
- Generate songs with custom lyrics.
- Use the voice of your favorite artist.
- High-quality audio output.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud TTS:**
   - Enable Google Cloud Text-to-Speech API.
   - Download your service account key JSON file.
   - Set the environment variable to point to your JSON file:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
     ```

4. **Run the application:**
   ```bash
   python app.py
   ```

## Usage
- Send a POST request to `/create_song` with JSON payload containing `text` (lyrics) and `artist_voice` (voice model).
- Example payload:
  ```json
  {
    "text": "Your custom lyrics here",
    "artist_voice": "en-US-Wavenet-D"
  }
  ```

## Deployment
You can deploy this bot using Render or any other cloud service provider.

### Using Render:
1. Push your code to GitHub.
2. Create a new service in Render and connect your GitHub repository.
3. Set environment variables in Render for `GOOGLE_APPLICATION_CREDENTIALS`.
4. Deploy the service and access your bot.

## License
This project is licensed under the MIT License.
```

### 4. `.gitignore`
```
*.pyc
__pycache__/
instance/
.webassets-cache
.env
venv/
.env.local
.env.*.local
.DS_Store
/output.mp3
```

### 5. `Procfile` (for deploying with Render)
```
web: gunicorn app:app
```

### 6. خدمة Google Cloud TTS
تأكد من أنك قد فعلت Google Cloud Text-to-Speech API وحصلت على ملف JSON لمفاتيح الخدمة.

### التعليمات لنشر التطبيق على Render:
1. ادخل إلى [Render](https://render.com/) وقم بإنشاء حساب إذا لم يكن لديك حساب بالفعل.
2. أنشئ خدمة جديدة واختر نوع الخدمة "Web Service".
3. اربط حساب GitHub الخاص بك واختر المستودع الذي يحتوي على ملفات البوت.
4. تأكد من إعداد متغير البيئة `GOOGLE_APPLICATION_CREDENTIALS` للإشارة إلى ملف JSON الخاص بمفاتيح الخدمة.
5. اختر الإعدادات المناسبة واضغط على "Create Service".

بعد اتباع هذه الخطوات، يجب أن يكون لديك بوت جاهز لاستقبال طلبات إنشاء الأغاني بصوت الفنان والكلمات التي يرسلها المستخدم.
