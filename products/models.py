from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name = _('parent'), blank = True, null = True, on_delete = models.CASCADE)
    title = models.CharField(_('Title'), max_length = 50)
    description = models.TextField(_('description'), blank = True)
    avatar = models.ImageField(_('Avatar'), blank = True, upload_to = 'categories/')
    is_enable = models.BooleanField(_('Is enable'), default = True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add = True)
    updated_time = models.DateTimeField(_('Update Time'), auto_now = True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length = 50)
    description = models.TextField(_('description'), blank = True)
    avatar = models.ImageField(_('Avatar'), blank = True, upload_to = 'products/')
    is_enable = models.BooleanField(_('Is enable'), default = True)
    categories = models.ManyToManyField('Category', verbose_name = _('categories'), blank = True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add = True)
    updated_time = models.DateTimeField(_('Update Time'), auto_now = True)
    
    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
    
   


class File(models.Model):
        FILE_AUDIO = 'audio'
        FILE_VIDEO = 'video'
        FILE_IMAGE = 'image'
        FILE_PDF = 'pdf'
        FILE_TYPE = [
            (FILE_AUDIO, _('Audio')),
            (FILE_VIDEO, _('Video')),
            (FILE_IMAGE, _('Image')),
            (FILE_PDF, _('PDF')),
        ]
        product = models.ForeignKey('Product', verbose_name = _('product'), related_name = 'file', on_delete = models.CASCADE)
        title = models.CharField(_('Title'), max_length = 50)
        File_type = models.CharField(_('File Type'), choices = FILE_TYPE, default = FILE_VIDEO)
        file = models.FileField(_('File'), upload_to = 'files/%Y/%m/%d/')
        is_enable = models.BooleanField(_('Is enable'), default = True)
        created_time = models.DateTimeField(_('Created Time'), auto_now_add = True)
        updated_time = models.DateTimeField(_('Update Time'), auto_now = True)
    
        class Meta:
            db_table = 'file'
            verbose_name = _('file')
            verbose_name_plural = _('files')
