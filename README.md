# File Validation

## Security
##### For security purposes we need to validate/check files uploaded to the server. .php and .asm files may pose a great security risk if uploaded to the server via a website. For example, if you create a website that students have to upload their assignments, they need to upload lets only .doc, .docx or .pdf files. You will have to restrict your form to accept only these three extendsion or else they may end up uploading a video.
##### We can achieve this with Django using FileExtensionValidator.

## Steps to follow
#### 1. Create a project and an app in django in your base folder.
#### 2. In your app create a model to handle file storage (in this case I created UserFiles) and specify where the files will be stored using the upload_to='<name of your folder/>' argument.

![models](https://user-images.githubusercontent.com/78599959/181189625-688975a0-1713-4d7d-923a-ebd598d45abd.png)

#### 3. Since we have used the upload_to='' argument, we have to configure MEDIA_ROOT & MEDIA_URL in our settings.py
 
 ![settings](https://user-images.githubusercontent.com/78599959/181189720-acf6dfd3-69a3-4ff6-9657-7cf5b11ac788.png)

 
#### 4. Open urls.py in your project folder and specify media path.
  

#### 5. Create forms.py in your application and create a form to handle file uploads. Import FileExtensionValidator from django.core.validators. Add supported file extensions in the list in FileExtensionValidator() function. In my case I only want .doc, .docx & .pdf to be uploaded.

![forms](https://user-images.githubusercontent.com/78599959/181189767-27852665-347c-4355-a0ea-d4623a1fb38e.png)
  
#### 6. Import your form in your views.py

![views](https://user-images.githubusercontent.com/78599959/181189870-2899a13c-4cd4-4159-b170-53f07d9503ea.png)

#### 7. Don't forget to add {{form|crispy}} in your template.
