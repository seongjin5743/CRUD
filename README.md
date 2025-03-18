## 0. setting

- `.gitignore`
- 가상환경 설정
    - `python -m venv venv`
    - `source venv/Scripts/activate`
- `README.md`

## 1. Django

1. django 설치
```shell
pip install django
```

2. 프로젝트 생성
```shell
django-admin startproject <pjt-name> <path>
```

3. 서버실행 (종료 : `ctrl + c`)
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app-name>
```

5. 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```

## 2. CRUD
- modeling (`models.py`)

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

- migration (`migrations`)

```shell
# 번역본 생성
python manage.py makemigrations

#DB에 반영
python manage.py migrate 
```