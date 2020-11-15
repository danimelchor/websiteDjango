from django.shortcuts import render

def home(request):
    context = {
        'socials': [{
                'icon': 'fas fa-envelope',
                'a': '#',
                'color': '#EA4335'
            },{
                'icon': 'fab fa-github',
                'a': 'https://github.com/danimelchor',
                'color': '#333'
            },{
                'icon': 'fab fa-twitter',
                'a': 'https://twitter.com/danii672',
                'color': '#1DA1F2'
            },{
                'icon': 'fab fa-linkedin-in',
                'a': 'https://www.linkedin.com/in/dannymelchor/',
                'color': '#0077b5'
            },{
                'icon': 'fab fa-instagram',
                'a': 'https://www.instagram.com/dmelchor_/',
                'color': 'linear-gradient(45deg, rgba(64,93,230,1) 0%, rgba(253,29,29,1) 50%, rgba(255,220,128,1) 100%)'
            }],
        'path':'/'
    }
    return render(request, 'index.html', context)
