sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
Тогда при решении очередного задания необходимые действия будут сведены к минимуму:

git clone https://github.com/your_account/stepic_web_project.git /home/box/web
bash /home/box/web/init.sh
