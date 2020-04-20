from django.conf import settings 
import sys 
import os 
import json 

sys.path.append(settings.BASE_DIR)
IGDB_PATH = os.path.join(settings.BASE_DIR,"igdb_python_api")
GAMES_PATH = os.path.join(settings.BASE_DIR,"games")
sys.path.append(IGDB_PATH)

from igdb_python_api import code
 

def createDjangoFixture(model_name,start_pk,filename,json_data): 
    assert model_name != None 
    assert start_pk != None 
    assert json_data != None 

    json_list = []
    json_dict = {}
    json_sub = {}
    current_pk = start_pk 

    for obj in json_data: 
        json_dict["model"]=model_name 
        json_dict["pk"] = current_pk
        
        for field in obj : 
            json_sub[field] = obj[field]
        
        json_dict["fields"] = json_sub
        
        json_list.append(json_dict)
        current_pk=current_pk + 1 
       

    json_obj = json.dumps(json_list)

    if filename : 
        with open(filename,"w",encoding="utf-8") as json_file : 
            json.dump(json_list,json_file,indent=4)
        
    return json_obj




igdb_handler = code.IGBRequest(media_path="media")
response = igdb_handler.getTopnGames(n=10,fields=["name"])
createDjangoFixture(model_name="SAMPLE_MODEL",start_pk=1,filename="my_fixture.json",json_data=response)







