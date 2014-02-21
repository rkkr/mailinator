mailinator
==========

# Packages needed: 
sudo apt-get install git apache2 pyton-django python-mysqldb mysql-server<br />

# REST framework:
http://www.django-rest-framework.org/#installation<br />
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
/var/www/mailinator/manage.py syncdb<br />

# Add site to apache:
(modify to match current server)<br />
sudo cp /var/www/mailinator/configs/default /etc/apache2/sites-enabled/000-default<br />
sudo service apache2 restart<br />

# Add init script for SMTP server:
sudo cp /var/www/mailinator/configs/pysmtpd /etc/init.d/<br />
sudo update-rc.d pysmtpd defaults 99 1<br />
