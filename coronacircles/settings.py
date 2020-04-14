import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for CoronaCircles project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'afxw#@!8jun_(0d_@pkoy_b*@(g4igm9v^2fsgsxttrc)ylb1^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'coronacircles.urls'



WSGI_APPLICATION = 'coronacircles.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'coronacircles', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'coronacircles', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'coronacircles',
    'main_app.apps.MainAppConfig',
    'schedule',
    'djcms_custom_menu',
]

TEMPLATE_CONTEXT_PROCESSORS = {
    'django.template.context_processors.request'
}

LANGUAGES = (
    ## Customize this
    ('de', gettext('de')),
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'de',
            'name': gettext('de'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('start.html', 'Start'),
    ('fullcalendar.html', 'Fullcalendar'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'First Slide Headline': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>Why?</h1>',
                },
            },
        ],
    },
    'First Slide Text': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<p>In times of social distancing we meet online to create encounters, where we listen to what touches us deeply.<br />To do this, we combine the powerful tradition of the circle work with the current possibilities of video conferencing.</p><p>Since the beginning of time, people have been coming together in circles to share about themselves and their concerns.<br />Let us use this online tool to get out of our isolation and experience online circles, in which we feel seen and heard.</p>',
                },
            },
        ],
    },
    'Second Slide Headline': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>How do you find one Another?</h1>',
                },
            },
        ],
    },
    'Second Slide Text': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<p>On this platform you can join a CoronaCircle or invite others to one. Up to 7 people come together and talk about what moves them and listen to each other carefully.</p><p>Let us form a network of self-organized circles in order to support each other in these extraordinary times!</p>',
                },
            },
        ],
    },
    'Third Slide Headline': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>Flow of A CoronaCycle</h1>',
                },
            },
        ],
    },
    'Third Slide Text': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<p>The CoronaCircle method is simple and effective. It provides a framework that helps to create a respectful and appreciative communication at eye level.</p><ul><li>Welcome</li><li>A moment of silence</li><li>First round: Who and where am I?</li><li>Second round: How am I doing? What do I need? What touches or inspires me?</li><li>Third round: What do I take with me from this CoronaCircle?</li>',
                },
            },
        ],
    },
    'Fourth Slide Headline': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>What is helpful?</h1>',
                },
            },
        ],
    },
    'Fourth Slide Text': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<ul><li>Rejoicing in meeting people</li><li>Listening benevolently and impartially</li><li>Courage to show myself with my own feelings, worries and experiences</li><li>Making sure that I speak about myself when I talk</li><li>Mindful handling of what is shared</li><li>Silence is also a form of sharing</li>',
                },
            },
        ],
    },
    'Events Headline': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>Participate in a corona circle</h1>',
                },
            },
        ],
    },
    'show more': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h3>Show more Circles:</h3>',
                },
            },
        ],
    },
    'Host': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>Host a Corona Circle</h1><p>Inviting to a CoronaCircle is easy</p><p>You should have good experience with talking circles such as the Corona Circles.<br />As a host your tasts are:</p><ul><li>to welcome everyone and to bring their awareness the suggestions and the procedure as they are formulated for you in the confirmation mail</li><li>mark the beginning of each round</li><li>watch the time (and start the integrated timer as soon as a person starts talking)</li></ul>',
                },
            },
        ],
    },
    'Testimonials Headline': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>Testimonials</h1>',
                },
            },
        ],
    },
    'Testimonial 1 Image': {
        'plugins': ['Bootstrap4PicturePlugin'],
    },
    'Testimonial 2 Image': {
        'plugins': ['Bootstrap4PicturePlugin'],
    },
    'Testimonial 3 Image': {
        'plugins': ['Bootstrap4PicturePlugin'],
    },
    'Testimonial 4 Image': {
        'plugins': ['Bootstrap4PicturePlugin'],
    },
    'Testimonial 5 Image': {
        'plugins': ['Bootstrap4PicturePlugin'],
    },
    'Testimonial 6 Image': {
        'plugins': ['Bootstrap4PicturePlugin'],
    },
    'Testimonial 1 Text': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 2 Text': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 3 Text': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 4 Text': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 5 Text': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 6 Text': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 1 Author': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 2 Author': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 3 Author': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 4 Author': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 5 Author': {
        'plugins': ['TextPlugin'],
    },
    'Testimonial 6 Author': {
        'plugins': ['TextPlugin'],
    },
    'Contact': {
        'plugins': ['TextPlugin'],
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body':'<h1>Contact</h1><p><a href="mailto:contact@coronacircles.net">Contact</a> the CoronaCircle Team</br>Share your experiences, questions, and ideas with us!</p>',
                },
            },
        ],
    },
    'twitter link': {
        'plugins': ['Bootstrap4LinkPlugin'],
    },
    'facebook link': {
        'plugins': ['Bootstrap4LinkPlugin'],
    },
    'instagram link': {
        'plugins': ['Bootstrap4LinkPlugin'],
    },
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
