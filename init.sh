sudo pip3 install --upgrade django
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default    
sudo /etc/init.d/nginx start                                                    
gunicorn -c /home/box/web/etc/gunicorn.conf  hello:wsgi_app
                               
