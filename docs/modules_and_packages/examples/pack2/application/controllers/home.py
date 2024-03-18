# Приклад відносного імпорта з батьківського пакета
from ..models.article import ArticleModel

class HomeController(object):
    """Тут тіпа контроллер домашньої сторінки"""

    def get(self):
        print('HTTP GET request to /home/')
        ArticleModel.get_objects()
        print('Rendering HTML page')
