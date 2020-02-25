from aiohttp import web
import json


async def handle(request):
    response_obj = {
        'name': 'Eyob Tariku',
        'title': 'Python Backend Developer',
        'languages': [
            'Python', 'JavaScript', 'TypeScript',
            'HTML', 'CSS', 'SASS', 'PHP', 'Bash'
        ],
        'frameworks': ['Django', 'Angular'],
        'libraries': ['Bootstrap', 'jQuery', 'Scrapy'],
        'DevOps': ['Docker', 'GCP', 'Travis CI', 'Circle CI'],
        'tools': ['Jira', 'Assana', 'Slack', 'Git', 'Github', 'GitLab'] 
    }
    return web.Response(text=json.dumps(response_obj))

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app, host='0.0.0.0', port='4000')