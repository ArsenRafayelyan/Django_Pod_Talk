from django.db import models

# Create your models here.


class HomeLogo(models.Model):

    logo = models.ImageField('Home logo', upload_to='images')


class HomeBgInfo(models.Model):

    name = models.CharField('HomeBg info', max_length=50)
    text = models.TextField('HomeBg text')
    button_name = models.CharField('HomeBg button name', max_length=60)

    def __str__(self):
        return self.name
    

class HomeSlider(models.Model):

    name = models.CharField('Slider name', max_length=50)
    img = models.ImageField('Slider image', upload_to='images')
    proff1 = models.CharField('Slider proff1', max_length=60, blank=True)
    proff2 = models.CharField('Slider proff2', max_length=60, blank=True)
    logo = models.ImageField('Slider logo', upload_to='images', blank=True)
    link1 = models.URLField('Slider link1', blank=True)
    link2 = models.URLField('Slider link2', blank=True)
    link3 = models.URLField('Slider link3', blank=True)
    link1_name = models.CharField('Slider link1 name', max_length=30, blank=True)
    link2_name = models.CharField('Slider link2 name', max_length=30, blank=True)
    link3_name = models.CharField('Slider link3 name', max_length=30, blank=True)

    def __str__(self):
        return self.name
    

class Lastest_Episode(models.Model):

    after = models.ForeignKey(HomeSlider, on_delete=models.CASCADE, related_name='after_post')
    video_rate = models.CharField('Video rate', max_length=60)
    episode = models.PositiveIntegerField('Episode number')
    name = models.CharField('Episode name', max_length=60)
    text = models.CharField('Episode text', max_length=100)
    button1 = models.PositiveBigIntegerField('Button1', default=0)
    button2 = models.PositiveBigIntegerField('Button2', default=0)
    button3 = models.PositiveBigIntegerField('Button3', default=0)
    button4 = models.PositiveBigIntegerField('Button3', default=0)
    file = models.FileField('file', upload_to='file', blank=True)


    def __str__(self):
        return self.name
    
class Topic(models.Model):

    name = models.CharField('Topic name',max_length=30)
    img = models.ImageField('Topic image',upload_to='images')
    count = models.PositiveIntegerField('Episode count')

    def __str__(self):
        return self.name

class Trending(models.Model):
    after = models.ForeignKey(HomeSlider, on_delete=models.CASCADE, related_name='after')
    text = models.CharField('Trending text', max_length=100)
    img = models.ImageField('Trending images',upload_to='images')
    button1 = models.PositiveBigIntegerField('Button1', default=0)
    button2 = models.PositiveBigIntegerField('Button2', default=0)
    button3 = models.PositiveBigIntegerField('Button3', default=0)
    name = models.CharField(' Trending name',max_length=30,blank=True)

    def __str__(self):
        return self.name
    
class About_page(models.Model):

    name = models.CharField('About_page name info', max_length=50)

class About_boody(models.Model):

    name = models.CharField('About boody name', max_length=50)
    text = models.TextField('About boody text')
    img = models.ImageField('About boody image',upload_to='images')

    def __str__(self):
        return self.name
    

class AboutSlider(models.Model):

    name = models.CharField('Slider name', max_length=50)
    img = models.ImageField('Slider image', upload_to='images')
    proff1 = models.CharField('Slider proff1', max_length=60, blank=True)
    proff2 = models.CharField('Slider proff2', max_length=60, blank=True)
    logo = models.ImageField('Slider logo', upload_to='images', blank=True)
    link1 = models.URLField('Slider link1', blank=True)
    link2 = models.URLField('Slider link2', blank=True)
    link3 = models.URLField('Slider link3', blank=True)
    link1_name = models.CharField('Slider link1 name', max_length=30, blank=True)
    link2_name = models.CharField('Slider link2 name', max_length=30, blank=True)
    link3_name = models.CharField('Slider link3 name', max_length=30, blank=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField('Contact name',max_length=30)
    email = models.EmailField('Contact email')
    company = models.CharField('Company name',max_length=50)
    message = models.TextField('Message')

    def __str__(self):
        return self.name