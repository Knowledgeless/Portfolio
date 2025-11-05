from django.shortcuts import render




def home(request):
    services = ["Web Development", "Django Backend", "Python Automation", "Web Scraping", "Web Design", "Digital Poster Design", "Cover Page Design", "Ad Design", "Print Media Design"]

    career_steps = [
        {
            "year": "2025",
            "title": "Graphics Designer",
            "description": "Bangladesh Open Source Network (BdOSN).",
        },
        {
            "year": "2023",
            "title": "Graphics Designer Intern",
            "description": "Intellic IT LLC.",
        },
        {
            "year": "2022",
            "title": "Design Advisor",
            "description": "Southeast Computer Club, Southeast University",
        },
        {
            "year": "2021",
            "title": "Graphics Design Team Lead",
            "description": "Southeast Computer Club, Southeast University.",
        },
        {
            "year": "2020",
            "title": "Graphics Designer",
            "description": "Southeast Computer Club, Southeast University.",
        },
        {
            "year": "2018",
            "title": "Junior Graphics Designer",
            "description": "Line Work, Panthapath, Dhaka",
        },
    ]

    return render(request, "html/home.html", {"services": services, "career_steps": career_steps})

def graphics(request):
    return render(request, "html/graphics.html")

def projects(request):
    return render(request, "html/projects.html")

def contact(request):
    return render(request, "html/contact.html")
