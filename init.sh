sudo apt update                                                                 
sudo apt install python3.5                                                      
virtualenv --python=/usr/bin/python3.5 venv                                     
source venv/bin/activate                                                        
pip3 install django
pip install gunicorn   
sudo apt install htop

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default    
sudo /etc/init.d/nginx start                                                    
#gunicorn -c /home/box/web/etc/gunicorn.conf  hello:wsgi_app
gunicorn -c /home/box/web/etc/gunicorn_dj.conf --pythonpath /home/box/web/ask ask.wsgi:application

                               
