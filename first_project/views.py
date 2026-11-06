
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    <body style="background:#1e293b; color:white; text-align:center; padding:100px 40px 40px; font-family:Arial;">

        <div style="background:#0f172a; padding:20px; border-radius:15px; position:fixed; top:0; left:0; right:0;">
            <a href="/" style="color:#f5deb3; margin:15px; text-decoration:none;">HOME</a>
            <a href="/about/" style="color:#f5deb3; margin:15px; text-decoration:none;">ABOUT</a>
            <a href="/services/" style="color:#f5deb3; margin:15px; text-decoration:none;">SERVICES</a>
            <a href="/portfolio/" style="color:#f5deb3; margin:15px; text-decoration:none;">PORTFOLIO</a>
            <a href="/media/" style="color:#f5deb3; margin:15px; text-decoration:none;">MEDIA</a>
            <a href="/contact/" style="color:#f5deb3; margin:15px; text-decoration:none;">CONTACT</a>
        </div>

        <h1 style="color:#f5deb3;">Welcome to Django 🚀</h1>

        <img src="https://picsum.photos/id/1/500/300"
             style="width:400px; border-radius:20px; box-shadow:0 5px 15px bisque;">

        <h2>My First Project</h2>

        <p style="color:#cbd5e1;">I am learning Python and Django!</p>

        <button style="background:#f5deb3; padding:12px 25px; border:0; border-radius:20px; color:#1e293b; font-weight:bold;">WELCOME</button>

    </body>
    """)


def media(request):
    return HttpResponse("""
    <body style="background:#3e0707; color:white; text-align:center; padding:100px 30px 30px; font-family:Arial;">

        <div style="background:#0f172a; padding:20px; border-radius:15px; position:fixed; top:0; left:0; right:0;">
            <a href="/" style="color:#f5deb3; margin:15px; text-decoration:none;">HOME</a>
            <a href="/about/" style="color:#f5deb3; margin:15px; text-decoration:none;">ABOUT</a>
            <a href="/services/" style="color:#f5deb3; margin:15px; text-decoration:none;">SERVICES</a>
            <a href="/portfolio/" style="color:#f5deb3; margin:15px; text-decoration:none;">PORTFOLIO</a>
            <a href="/media/" style="color:#f5deb3; margin:15px; text-decoration:none;">MEDIA</a>
            <a href="/contact/" style="color:#f5deb3; margin:15px; text-decoration:none;">CONTACT</a>
        </div>

        <h1 style="color:bisque;">🎬 My Video</h1>

        <video controls style="width:50%; height:400px; border-radius:25px; box-shadow:0 4px 15px bisque;">
            <source src="/static/Yurikamome_Line_(Shimbashi_to_Toyosu)_Train_POV.webm" type="video/webm">
        </video>

        <h1 style="color:bisque; margin-top:40px;">🎵 My Audio</h1>

        <audio controls style="width:40%;">
            <source src="/static/arunangshubanerjee-live-football-match-stadium-crowd-cheering-563439.mp3" type="audio/mpeg">
        </audio>

    </body>
    """)


def about(request):
    return HttpResponse("""
    <body style="background:#164e63; color:white; text-align:center; padding:100px 40px 40px; font-family:Arial;">

        <div style="background:#0f172a; padding:20px; border-radius:15px; position:fixed; top:0; left:0; right:0;">
            <a href="/" style="color:#f5deb3; margin:15px; text-decoration:none;">HOME</a>
            <a href="/about/" style="color:#f5deb3; margin:15px; text-decoration:none;">ABOUT</a>
            <a href="/services/" style="color:#f5deb3; margin:15px; text-decoration:none;">SERVICES</a>
            <a href="/portfolio/" style="color:#f5deb3; margin:15px; text-decoration:none;">PORTFOLIO</a>
            <a href="/media/" style="color:#f5deb3; margin:15px; text-decoration:none;">MEDIA</a>
            <a href="/contact/" style="color:#f5deb3; margin:15px; text-decoration:none;">CONTACT</a>
        </div>

        <h1 style="color:#bae6fd;">About Me 👨‍💻</h1>

        <img src="https://images.unsplash.com/photo-1793605300952-49cbebdc3d49?w=600"
             style="height:400px; width:350px; border-radius:25px; box-shadow:0 5px 20px black;">

        <h2>Future Python Developer</h2>

        <p style="color:#cffafe;">My name is Kholiqov Abdujamil</p>
        <p style="color:#cffafe;">I'm 16 years old</p>
        <p style="color:#cffafe;">I love programming and creating websites!</p>

    </body>
    """)


def contact(request):
    return HttpResponse("""
    <body style="background:#3e0707; color:white; text-align:center; padding:100px 40px 40px; font-family:Arial;">

        <div style="background:#0f172a; padding:20px; border-radius:15px; position:fixed; top:0; left:0; right:0;">
            <a href="/" style="color:#f5deb3; margin:15px; text-decoration:none;">HOME</a>
            <a href="/about/" style="color:#f5deb3; margin:15px; text-decoration:none;">ABOUT</a>
            <a href="/services/" style="color:#f5deb3; margin:15px; text-decoration:none;">SERVICES</a>
            <a href="/portfolio/" style="color:#f5deb3; margin:15px; text-decoration:none;">PORTFOLIO</a>
            <a href="/media/" style="color:#f5deb3; margin:15px; text-decoration:none;">MEDIA</a>
            <a href="/contact/" style="color:#f5deb3; margin:15px; text-decoration:none;">CONTACT</a>
        </div>

        <h1 style="color:bisque;">Contact Me 📞</h1>

        <img src="https://picsum.photos/id/180/500/300"
             style="width:400px; border-radius:25px; box-shadow:0 5px 20px black;">

        <h2>Let's Work Together!</h2>

        <p style="color:#f5deb3;">Welcome to my contact page!</p>

        <button style="background:linear-gradient(135deg,#f5deb3,#d2a679); color:#3e0707; padding:15px 35px; border:none; border-radius:30px; font-size:16px; font-weight:bold; cursor:pointer; box-shadow:0 5px 15px rgba(245,222,179,0.4);">CONTACT ME ✉</button>

    </body>
    """)


def services(request):
    return HttpResponse("""
    <body style="background:#14532d; color:white; text-align:center; padding:100px 40px 40px; font-family:Arial;">

        <div style="background:#0f172a; padding:20px; border-radius:15px; position:fixed; top:0; left:0; right:0;">
            <a href="/" style="color:#f5deb3; margin:15px; text-decoration:none;">HOME</a>
            <a href="/about/" style="color:#f5deb3; margin:15px; text-decoration:none;">ABOUT</a>
            <a href="/services/" style="color:#f5deb3; margin:15px; text-decoration:none;">SERVICES</a>
            <a href="/portfolio/" style="color:#f5deb3; margin:15px; text-decoration:none;">PORTFOLIO</a>
            <a href="/media/" style="color:#f5deb3; margin:15px; text-decoration:none;">MEDIA</a>
            <a href="/contact/" style="color:#f5deb3; margin:15px; text-decoration:none;">CONTACT</a>
        </div>

        <h1 style="color:#bbf7d0;">My Services 💻</h1>

        <img src="https://picsum.photos/id/0/500/300"
             style="width:400px; border-radius:25px; box-shadow:0 4px 15px bisque;">

        <h2>What I Can Do</h2>

        <p style="color:#dcfce7; font-size:18px;">
            Python | Django | Web Development
        </p>

        <p style="color:#dcfce7; font-size:18px;">
            HTML & CSS | SQL | Telegram Bot
        </p>

    </body>
    """)


def portfolio(request):
    return HttpResponse("""
    <body style="background:#7c2d12; color:white; text-align:center; padding:100px 40px 40px; font-family:Arial;">

        <div style="background:#0f172a; padding:20px; border-radius:15px; position:fixed; top:0; left:0; right:0;">
            <a href="/" style="color:#f5deb3; margin:15px; text-decoration:none;">HOME</a>
            <a href="/about/" style="color:#f5deb3; margin:15px; text-decoration:none;">ABOUT</a>
            <a href="/services/" style="color:#f5deb3; margin:15px; text-decoration:none;">SERVICES</a>
            <a href="/portfolio/" style="color:#f5deb3; margin:15px; text-decoration:none;">PORTFOLIO</a>
            <a href="/media/" style="color:#f5deb3; margin:15px; text-decoration:none;">MEDIA</a>
            <a href="/contact/" style="color:#f5deb3; margin:15px; text-decoration:none;">CONTACT</a>
        </div>

        <h1 style="color:#fed7aa;">My Portfolio ⭐</h1>

        <img src="https://picsum.photos/id/20/500/300"
             style="width:400px; border-radius:25px; box-shadow:0 5px 20px black;">

        <h2>My First Django Project</h2>

        <p style="color:#ffedd5;">Every expert was once a beginner!</p>

        <button style="background:#fed7aa; color:#7c2d12; padding:12px 30px; border:0; border-radius:20px; font-weight:bold;">MY PROJECTS ⭐</button>

    </body>
    """)