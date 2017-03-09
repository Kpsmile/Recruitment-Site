# Recruitment-Site
we should make sure we have the python 2.7 &  latest version of pip (pip install --upgrade pip)
Steps for Installations :

Step 1: Install virtual Enviroment
      Windows Command :    pip install virtualenv
                           pip install virtualenv --upgrade 
      Linux Command  :     pip install virtualenv
                           pip install virtualenv --upgrade
      
Step 2: Activate virtual Enviroment:
        Windows Command :    
                          virtualenv myvenv
                          cd myvenv
                           .\Scripts\activate
                          
        Linux Command  :     
                        virtualenv myvenv
                        cd myvenv
                        source myvenv/bin/activate
                        
 Step 3: Install Django 1.9, Pillow & Wheel
        Windows Command :    pip install Django==1.9
                             pip install  Pillow==3.1.0
                             pip install  wheel==0.24.0
                             
        Linux Command  :     pip install Django==1.9
                             pip install  Pillow==3.1.0
                             pip install  wheel==0.24.0
                             
                             
 Step 4:  Clone from git hub  :    
   Command:        git clone  git@github.com:Kpsmile/Recruitment-Site.git
                               OR
                    git clone https://github.com/Kpsmile/Recruitment-Site
                    
    Command:              cd Recruitment-Site/trydjango19/
    Command:                 Python manage.py createsuperuser
                            ( Give username & pwd)
    Command:                 Python manage.py makemigartions
    Command:                 Python manage.py migrate
    Command:                 Python manage.py runserver
                              (Start the server)
    
 Step 5:Open Django Admin Interface  login with username & pwd :
   Browser :  http://127.0.0.1:8000/admin/
 
 
 Step 6: Create  the form 
         http://127.0.0.1:8000/posts/create/
         
  step 7:  View  the form (Pagination Applied for  Multiple forms) 
            http://127.0.0.1:8000/posts/
            
  Step 8: View The details  of the form by  Clicking VIEW icon or  the Hyperlink  it will show the details of  the post created
          Example :      http://127.0.0.1:8000/posts/resume-1-2/
          
   Step 9: Post Can be edited by  adding /edit in the url  
            Example : http://127.0.0.1:8000/posts/resume-1-2/edit/
            
   Step 10: Post Can be deleted by  adding /delete in the url         
            Example :http://127.0.0.1:8000/posts/developer/delete
            
    Step 11: All the Posts added  can be seen in Django admin interface and edit /update/ delete can also be done from admin interface
            http://127.0.0.1:8000/admin/posts/post/
            
            
 
 
 Any Suggesstions & Feedbacks on the code are highly appreciated

Thanks & Regards,

Kamakhya Prasad Singh (K.P.Singh)

 Contact No: (+91) 8553832266
    
    
         
