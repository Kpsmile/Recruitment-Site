# RestShopAPI
we should make sure we have the python3 &  latest version of pip (pip install --upgrade pip)

Steps for Installations :

Step 1: Install virtual Enviroment:

      Windows Command :    pip install virtualenv
                           pip install virtualenv --upgrade 
      Linux Command  :     pip install virtualenv
                           pip install virtualenv --upgrade
      
Step 2: Activate virtual Enviroment:

        Windows Command :    
                          virtualenv restshop 
                          cd restshop
                           .\Scripts\activate
                          
        Linux Command  :     
                        virtualenv restshop 
                        cd restshop
                        source restshop/bin/activate
                        
 Step 3: Install requirements:
 
        Windows Command :   pip install -r requirements.txt
                             
        Linux Command  :     pip install -r requirements.txt
                             
                             
 Step 4:  Clone from git hub  :   
 
      Command:        git clone  git@github.com:Kpsmile/RestShopAPI.git
                               OR
                    git clonehttps://github.com/Kpsmile/RestShopAPI
                    
      Command:              cd RestShopAPI
      Command:                 python manage.py createsuperuser
                            ( Give username & pwd)
      Command:                 python manage.py makemigrations
      Command:                 python manage.py migrate
      Command:                 python manage.py runserver
                              (Start the server)
    
 Step 5:Open Django Admin Interface  login with username & pwd :

          Browser :  http://127.0.0.1:8000/admin/
		  
		  
		  
 Any Suggesstions & Feedbacks on the code are highly appreciated

Thanks & Regards,

Kamakhya Prasad Singh (K.P.Singh)

 Contact No: (+91) 9080144844
