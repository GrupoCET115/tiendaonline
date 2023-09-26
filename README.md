# tiendaonline

1. Ejecutar: chmod +x wait-for-it.sh
2. sudo docker compose up
3. docker compose exec web python /code/myshop/manage.py migrate
4. docker compose exec web python /code/myshop/manage.py loaddata mysite_data.json
5. Linux: Agregar a /etc/hosts 127.0.0.1 tdnonline.com www.tdnonline.com
6. Windows: Agregar a C:\Windows\System32\drivers\etc 127.0.0.1 tdnonline.com www.tdnonline.com
