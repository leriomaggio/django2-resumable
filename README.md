# Django Resumable (`django-resumable`)

``django-resumable`` provides Django 2.1 backend stuff (e.g. `ModelFields`, `Forms`, `staticfiles`) 
to integrates [`resumable.js`](<https://github.com/23/Resumable.js>) in Django apps and admin.

#### `ICYM`:

(from the [documentation](https://github.com/23/resumable.js/blob/master/README.md))

>Resumable.js is a JavaScript library providing multiple simultaneous, stable and 
>resumable uploads via the [`HTML5 File API`](http://www.w3.org/TR/FileAPI/).
>
>The library is designed to introduce fault-tolerance into the upload of large files through HTTP. 
>This is done by splitting each file into small chunks. 
>Then, whenever the upload of a chunk fails, uploading is retried until the procedure completes. 
>This allows uploads to automatically resume uploading after a network connection 
>is lost either locally or to the server. 
>Additionally, it allows for users to pause, resume and even recover uploads without 
>losing state because only the currently uploading chunks will be aborted, not the entire upload.
>
>Resumable.js does not have any external dependencies other than the `HTML5 File API`. 
>This is relied on for the ability to chunk files into smaller pieces. 
>Currently, this means that support is widely available in to Firefox 4+, Chrome 11+, 
>Safari 6+ and Internet Explorer 10+.


## Installation

* ``pip install django-resumable``
* Add ``django_resumable`` to your ``INSTALLED_APPS``


## How to use

### Views

In order to enable asynchronous files upload files, you must define an endpoint that will deal
with uploaded file chunks:

```Python
from django.urls import path, include

urlpatterns = [
    path('resumable_upload/', include('django_resumable.urls')),
]
```

By default, the `resume-upload` view is provided with no restriction on the accesses
(i.e. no `login_required` nor `staff_member_required`). 

To enable the view only on restricted levels of permissions, the url integration can be
easily modified, accordingly:

```Python

from django.contrib.auth.views import login_required
# To enable view in AdminForm
from django.contrib.admin.views.decorators import staff_member_required

from django_resumable.views import resumable_upload
from django.urls import path, include

urlpatterns = [
    path('resumable-upload', login_required(resumable_upload), 
         name='resumable-upload'),
    path('admin-resumable-upload', staff_member_required(resumable_upload), 
         name='admin-resumable-upload'),
]

```

### Model

`django-resumable` provides a `ResumableFileField` that can be easily integrated in 
your Model class:

```Python

from django.db import models
from django_resumable.fields import ResumableFileField

class MyModel(models.Model):
    file = ResumableFileField(chunks_upload_to='resumable_chunks', **kwargs)
```

The `ResumableFileField` field extends the default `django.core.fields.FielField` by including 
an additional parameter, namely `chunks_upload_to` specifying the path in the `MEDIA_ROOT` in which
temporary chunks will be uploaded. Once the upload is complete, the file will be 
automatically moved to the `upload_to` destination folder (if any).
 

### Form

If you want to handle resumable upload within your forms, 
you can use the `FormResumableFileField`:

```Python
from django.forms import Form
from django_resumable.forms import FormResumableFileField


class ResumableForm(Form):
    file = FormResumableFileField()
        
```

It is as simple as that: 
`FormResumableFileField` simply extends the core `django.forms.FileField` by injecting the
`django_resumable.widgets.ResumableWidget`.
This widget is the default widget mapped by default to `ResumableFileField` instances 
(see `django_resumable.fields.ResumableFileField.formfield` method). 


### Additional Settings

``django-resumable`` comes with some extendable settings allowing for additional setup:

- `RESUMABLE_SUBDIR`: Directory in `MEDIA_ROOT` in which chunks will be uploaded. This settings will be 
                      overriden by any `chunks_upload_to` options specified at the time of definition of 
                      `ResumableFileField` within Django Model.
                    
- `RESUMABLE_STORAGE`: (default `django.core.files.storage.FileSystemStorage`)
                       Django Storage class to be used to handle the uploads.