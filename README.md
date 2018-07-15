# uhack2018
A web app for restaurants owners to list food/meal serves that they would not be able to sell by the end of their day, and can list them using a quick and friendly interface to find potentials consumers. 
They will receive payment from MealPass based on their user rating and how much food they sold through MealPass.

Setup: Run pip install in Terminal:

$pip install -r requirement.txt

For Developmant mode:
In Settings.py change:
+ DEBUG = True
+ Comment out:
    ALLOWED_HOSTS = ['app.herokuapp.com'] 
+ Uncomment Local host:
    ALLOWED_HOSTS = []
    
For Production mode:
In Settings.py change:
+ DEBUG = True
+ Uncomment:
    ALLOWED_HOSTS = ['app.herokuapp.com'] 
+ Comment out Local host:
    ALLOWED_HOSTS = []
    
