from django.db import models

############################ FEEDBUZZ PROJECT ##########################################################

class admin(models.Model):  
    username            = models.CharField(max_length=50,unique=True) 
    contactno           = models.BigIntegerField(default=0,unique=True) 
    email               = models.CharField(max_length=100,null=True,unique=True)
    password            = models.CharField(max_length=100,null=True)
    active              = models.CharField(max_length=100,null=True)
    lastlogin          = models.CharField(max_length=100,null=True)
    auth_key             = models.CharField(max_length=100,null=True)

    



class shop(models.Model):
    admin_id        = models.ForeignKey(admin, on_delete=models.CASCADE)
    shopname        = models.CharField(max_length=100,null=True)
    address         = models.CharField(max_length=200,null=True)
    contactno       = models.CharField(max_length=100,null=True)
    description     = models.CharField(max_length=200,null=True)
    modeofreview    = models.CharField(max_length=20,null=True)

class googleshop(models.Model):
    shop_id        = models.OneToOneField(shop,on_delete=models.CASCADE)
    credential     = models.CharField(max_length=100,null=True)
    mapurl           = models.CharField(max_length=500,null=True)
    last_fetchid     = models.CharField(max_length=100,null=True)

class fbshop(models.Model):
    shop_id              = models.OneToOneField(shop,on_delete=models.CASCADE)
    credential           = models.CharField(max_length=100,null=True)
    fb_page_url          = models.CharField(max_length=500,null=True)
    total_review_count   = models.IntegerField(default=0,null=False)
    


class yelpshop(models.Model):
    shop_id        = models.ForeignKey(shop, on_delete=models.CASCADE)
    credential     = models.CharField(max_length=100,null=True)
    mapurl           = models.CharField(max_length=500,null=True)
    last_fetchid         = models.CharField(max_length=100,null=True)


class category(models.Model):
    shop_id             = models.ForeignKey(shop, on_delete=models.CASCADE)
    categoryname        = models.CharField(max_length=100,null=True)
    total_aspect        = models.IntegerField(null=True)

class reviewdata(models.Model):
    shop_id             = models.ForeignKey(shop, on_delete=models.CASCADE) 
    modeofreview        = models.CharField(max_length=20,null=True)
    review              = models.CharField(max_length=2000,null=True)
    sentiment           = models.FloatField(null=True)
    isaspectdone        = models.IntegerField(default=0)
    date_created        = models.DateTimeField(auto_now=True)
    username            = models.CharField(max_length=100,default="noname")
    rating              = models.IntegerField(default=0)
    reviewid            = models.CharField(max_length=40,null=True)
    timestamp           = models.CharField(max_length=40,null=True)


class aspectdata(models.Model):
    reviewdata_id       = models.ForeignKey(reviewdata, on_delete=models.CASCADE) 
    category_id         = models.ForeignKey(category, on_delete=models.CASCADE,null=True) 
    aspect              = models.CharField(max_length=500,null=True)
    sentiment           = models.FloatField(null=True)


class pricing(models.Model):
    shop_id                     = models.OneToOneField(shop,on_delete=models.CASCADE)
    aspectrequest               = models.IntegerField(default=0)
    sentimentrequest            = models.IntegerField(default=0)
    googlerequest               = models.IntegerField(default=0)
    yelprequest                 = models.IntegerField(default=0)
    date_created                = models.DateTimeField(auto_now=True,null=True)

class shopaspectarchive(models.Model):
    admin_id                    = models.ForeignKey(admin,on_delete=models.CASCADE)
    aspectname                  = models.CharField(max_length=30)
    count                       = models.IntegerField(default=0)
    

############################ FEEDBUZZ PROJECT ##########################################################
