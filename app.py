from flask import Flask, render_template

app = Flask(__name__)

# قائمة بكل المشاريع الـ 20
projects = [
    {
        'title': 'موقع Portfolio الشخصي',
        'description': 'موقع ويب متكامل مبني باستخدام Flask لعرض المهارات والمشاريع.',
        'tech_stack': 'Python, Flask, HTML, CSS',
        'github_url': 'https://github.com/ghazalahmad/Flask_Portfolio'
    },
    {
        'title': 'تحليل بقاء ركاب التايتانيك',
        'description': 'تحليل بيانات passengers سفينة التايتانيك واستخراج النتائج والرسوم البيانية.',
        'tech_stack': 'Python, Pandas, Jupyter',
        'github_url': 'https://github.com/ghazalahmad/Titanic-Survival-Analysis'
    },
    {
        'title': 'تطبيق تتبع الأسهم',
        'description': 'تطبيق لتتبع أسعار الأسهم وجلب البيانات المالية.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Stock-Tracker'
    },
    {
        'title': 'أداة كشف الوجوه',
        'description': 'تطبيق يستخدم OpenCV لكشف الوجوه في الصور والفيديو.',
        'tech_stack': 'Python, OpenCV',
        'github_url': 'https://github.com/ghazalahmad/face-detection'
    },
    {
        'title': 'التحكم بالصوت عبر إيماءات اليد',
        'description': 'برنامج يتحكم في مستوى صوت الجهاز باستخدام إيماءات اليد عبر الكاميرا.',
        'tech_stack': 'Python, OpenCV, MediaPipe',
        'github_url': 'https://github.com/ghazalahmad/Hand-Gesture-Volume-Control'
    },
    {
        'title': 'تتبع الأجسام بالألوان',
        'description': 'برنامج لتتبع الأجسام بناءً على لونها باستخدام الكاميرا.',
        'tech_stack': 'Python, OpenCV',
        'github_url': 'https://github.com/ghazalahmad/Color-Based-Object-Tracker'
    },
    {
        'title': 'ملخص المقالات الإخبارية',
        'description': 'أداة تقوم بتلخيص المقالات والأخبار الطويلة تلقائياً.',
        'tech_stack': 'Python, NLP',
        'github_url': 'https://github.com/ghazalahmad/NEWS-ARTICLE-SUMMARIZER'
    },
    {
        'title': 'مترجم لغات احترافي',
        'description': 'أداة لترجمة النصوص بين لغات مختلفة.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Professional-Language-Translator-'
    },
    {
        'title': 'تطبيق التعرف على الصوت',
        'description': 'تطبيق للتعرف على الكلام وتحويل الصوت إلى نص.',
        'tech_stack': 'Python, HTML',
        'github_url': 'https://github.com/ghazalahmad/Speech-Recognition-Application'
    },
    {
        'title': 'تحليل بيانات المبيعات',
        'description': 'تحليل بيانات المبيعات واستخراج الرؤى والإحصائيات.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/sales-data-analysis'
    },
    {
        'title': 'كاشط بيانات الويب (Web Scraping)',
        'description': 'أداة لجمع وتحليل البيانات من صفحات الويب باستخدام BeautifulSoup.',
        'tech_stack': 'Python, BeautifulSoup',
        'github_url': 'https://github.com/ghazalahmad/Web-Scraping-and-Data-Parsing-Using-Beautiful-Soup'
    },
    {
        'title': 'استخراج الصوت من الفيديو',
        'description': 'سكريبت لاستخراج المسار الصوتي من ملفات الفيديو.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Audio-Extractor-from-Video'
    },
    {
        'title': 'محرر الصور الجماعي',
        'description': 'أداة لتعديل مجموعة كبيرة من الصور في وقت واحد.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/BulkImageEditor'
    },
    {
        'title': 'مولد كلمات المرور',
        'description': 'أداة لتوليد كلمات مرور عشوائية وقوية.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Password_Generator'
    },
    {
        'title': 'تحميل الفيديوهات (ytdlp)',
        'description': 'واجهة رسومية لتحميل الفيديوهات من الإنترنت.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/ytdlp-gui'
    },
    {
        'title': 'حساب تكرار الكلمات',
        'description': 'برنامج لحساب عدد مرات تكرار كل كلمة في نص معين.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/word_frequencyn'
    },
    {
        'title': 'تطبيق طقس (1)',
        'description': 'تطبيق يعرض حالة الطقس في مدن مختلفة باستخدام API.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Python-Weather--Info-App'
    },
    {
        'title': 'تطبيق طقس (2)',
        'description': 'نسخة أخرى من تطبيق الطقس لجلب بيانات حالة الجو.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Python-Weather-Info-App'
    },
    {
        'title': 'لعبة تخمين الرقم',
        'description': 'لعبة تفاعلية حيث يحاول المستخدم تخمين رقم عشوائي بين 1 و100.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Number-Guessing-Game'
    },
    {
        'title': 'آلة حاسبة (Tkinter)',
        'description': 'آلة حاسبة رسومية تدعم العمليات الحسابية الأساسية.',
        'tech_stack': 'Python, Tkinter',
        'github_url': 'https://github.com/ghazalahmad/class-TkinterCalculator-'
    },
    {
        'title': 'منظّم الملفات',
        'description': 'برنامج يرتب الملفات تلقائياً في مجلدات حسب النوع.',
        'tech_stack': 'Python, OS',
        'github_url': 'https://github.com/ghazalahmad/dirx-file-organizer-main.'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)