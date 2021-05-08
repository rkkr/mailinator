mailinator
==========

# Packages needed: 
`sudo apt-get install git apache2 libapache2-mod-wsgi python-django python-pip python-mysqldb mysql-server`

# REST framework:
`pip install pymysql`
`pip install djangorestframework`
`pip install markdown`
`pip install django-filter==1.1`

# Get source:
`cd /var/www/`
`git clone https://github.com/rkkr/mailinator.git`

# Create database:
`mysql -u root -p`
`CREATE DATABASE dbo;`
`exit`

# Edit mailinator/settings.py and put your DB password there
        'USER': 'root',
        'PASSWORD': 'password',

# Initialize the DB
`manage.py migrate --run-syncdb`

# Add site to apache:
`sudo cp configs/apache_default.conf /etc/apache2/sites-available/000-default.conf`
`sudo service apache2 restart`

# Grant apache access to package resources:
`sudo nano /etc/apache2/apache2.conf`
Add configuration:
```
<Directory /usr/local/lib/python2.7/dist-packages/rest_framework/static/rest_framework/>
        Options Indexes
        AllowOverride None
        Require all granted
</Directory>

<Directory /usr/lib/python2.7/dist-packages/django/contrib/admin/static/admin//>
        Options Indexes
        AllowOverride None
        Require all granted
</Directory>

```
`sudo service apache2 restart`

# Add init script for SMTP server:
`sudo cp configs/pysmtpd.service /etc/systemd/system/pysmtpd.service`
`sudo systemctl daemon-reload`
`sudo systemctl enable pysmtpd`
`sudo service pysmtpd start`

# Add DB cleanup:
`crontab -e`
Add: `@daily /usr/bin/python /var/www/mailinator/manage.py cleaner`
