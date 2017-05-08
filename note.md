# python manage.py syncdb 變成
```
python manage.py migrate 
python manage.pymake migrations
```
# run
```
python manage.py runserver [[ip:]port]#預設8000
```
# 清空數據庫
```
python manage.py flush
```
# 建立 admin
```
python manage.py createsuperuser
#改密碼
python manage.py changepassword username
```
# 導出入數據
```
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json
```

# shell
```
python manage.py shell
python manage.py dbshell
```
```
python manage.py startapp learn
```
# 抓環境變數
```
os.environ["env"]
```