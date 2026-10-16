from flask import Flask, render_template

app = Flask(__name__)

# قائمة المشاريع
projects = [
    {
        'title': 'آلة حاسبة بلغة Python',
        'description': 'تطبيق Python يحوي عمليات حسابية أساسية (جمع، طرح، ضرب، قسمة) باستخدام Tkinter.',
        'tech_stack': 'Python, Tkinter',
        'github_url': 'https://github.com/ghazalahmad/class-TkinterCalculator-'
    },
    {
        'title': 'لعبة تخمين الرقم',
        'description': 'لعبة تفاعلية حيث يحاول المستخدم تخمين رقم عشوائي بين 1 و100.',
        'tech_stack': 'Python',
        'github_url': 'https://github.com/ghazalahmad/Number-Guessing-Game'
    },
    {
        'title': 'تطبيق الطقس',
        'description': 'تطبيق يعرض حالة الطقس في مدن مختلفة باستخدام API.',
        'tech_stack': 'Python, API',
        'github_url': 'https://github.com/ghazalahmad/Python-Weather--Info-App'
    },
    {
        'title': 'منظّم الملفات',
        'description': 'برنامج يرتب الملفات تلقائياً في مجلدات حسب النوع.',
        'tech_stack': 'Python, OS',
        'github_url': 'https://github.com/ghazalahmad/dirx-file-organizer-main.'
    },
    {
        'title': 'كشف الوجوه',
        'description': 'تطبيق يستخدم OpenCV لكشف الوجوه في الصور والفيديو.',
        'tech_stack': 'Python, OpenCV',
        'github_url': 'https://github.com/ghazalahmad/face-detection'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)