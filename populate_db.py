from django.conf import settings 
import sys 
import os 

sys.path.append(settings.BASE_DIR)
IGDB_PATH = os.path.join(settings.BASE_DIR,"igdb_python_api")
GAMES_PATH = os.path.join(settings.BASE_DIR,"games")
sys.path.append(IGDB_PATH)

from igdb_python_api import code
 



igdb_handler = code.IGBRequest()
response = igdb_handler.getTopnGames(n=2)
print(response)




