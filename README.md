#### SHADES mobile app api
## Overview
This project is a Django-based web application that allows users to create, manage, and interact with "Tabs" (posts) and related content such as comments and polls. The application also includes user authentication, registration, and profile management.

## Features
User Registration & Authentication

-Register new users
-Login and obtain JWT tokens
-Token refresh and verification
-User profile retrieval and listing
-Tabs Management

-Create, retrieve, update, and delete Tabs
-Tabs can contain various media types (images/videos)
-Each Tab can have associated comments and polls
-Comments

-Users can comment on Tabs
-Retrieve, update, and delete comments
-Polls

-Create and manage polls associated with Tabs
-Retrieve, update, and delete polls


## Installation
1 Clone the repository:

```sh

git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

## Install dependencies:
```sh

pip install -r requirements.txt
Configure the database: Update your settings.py with the appropriate database settings.
```
## Apply migrations:

```sh

python manage.py migrate
Create a superuser:```


python manage.py createsuperuser
Run the development server:

```

```sh 
python manage.py runserver
```

API Endpoints
User Endpoints
Registration: POST /accounts/
Login: POST /accounts/auth/login/
Token Refresh: POST /accounts/auth/refresh/
Token Verify: POST /accounts/api/token/verify/
User List: GET /accounts/users/
User Details: GET /accounts/user/<str:pk>/
Tab Endpoints
Create Tab: POST /home/tabs/
List Tabs: GET /home/tabs/
Retrieve/Update/Delete Tab: GET/PATCH/PUT/DELETE /home/tabs/<str:pk>/
Comment Endpoints
Create Comment: POST /home/tabs/<str:tab_id>/comments/
List Comments: GET /home/tabs/<str:tab_id>/comments/
Retrieve/Update/Delete Comment: GET/PATCH/DELETE /home/tabs/<str:tab_id>/comments/<str:pk>/
Poll Endpoints
Create Poll: POST /home/tabs/<str:tab_id>/polls/
List Polls: GET /home/tabs/<str:tab_id>/polls/
Retrieve/Update/Delete Poll: GET/PATCH/DELETE /home/tabs/<str:tab_id>/polls/<str:pk>/
Static and Media Files
Ensure that the static and media files are correctly set up in settings.py:


STATIC_URL = '/static/'
MEDIA_URL = '/media_files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
To serve static and media files during development, add the following to your urls.py:


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your existing URL patterns
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Contribution
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue to discuss what you would like to change.