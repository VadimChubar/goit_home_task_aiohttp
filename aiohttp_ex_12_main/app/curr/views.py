import aiohttp_jinja2
from parser import curr_nbu_private


@aiohttp_jinja2.template('index.html')
async def index(request):
    curr = curr_nbu_private()
    return curr


