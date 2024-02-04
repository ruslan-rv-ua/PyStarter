'''Класи (категорії) попереджень потрібні для гнучкого керування, фільтрації, форматування попереджень.
'''
import warnings
class MyWarning(UserWarning):
    pass
# усі попередження класа MyWarning або дочірніх — піднімається помилка замість попередження
warnings.filterwarnings('error', category=MyWarning)

# а так просто будемо ігнорувати усі попередження MyWarning
# warnings.filterwarnings('ignore', category=MyWarning)

warnings.warn('важливе попередження', MyWarning)
print('виконано.')
```

