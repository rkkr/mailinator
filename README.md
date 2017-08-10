mailinator
==========

# Packages needed: 
sudo apt-get install git apache2 libapache2-mod-wsgi python-django python-pip python-mysqldb mysql-server<br />

# REST framework:
http://www.django-rest-framework.org/#installation<br />
pip install pymysql
pip install djangorestframework<br />
pip install markdown<br />
pip install django-filter<br />

# Get source:
cd /var/www/
git clone git@github.com:rkkr/mailinator.git

# Create database:
mysql -u root -p<br />
CREATE DATABASE dbo;<br />
exit<br />

# Edit mailinator/settings.py and put your DB password there
        'USER': 'root',
        'PASSWORD': 'password',

# Initialize the DB
/var/www/mailinator/manage.py syncdb<br />

# Add site to apache:
(modify to match current server)<br />
sudo cp /var/www/mailinator/configs/apache_default /etc/apache2/sites-available/000-default<br />
sudo service apache2 restart<br />

# Add init script for SMTP server:
sudo cp /var/www/mailinator/configs/pysmtpd /etc/init.d/<br />
sudo update-rc.d pysmtpd defaults 99 1<br />
