from django.conf import settings 
import sys 
import os 
import json 

sys.path.append(settings.BASE_DIR)
IGDB_PATH = os.path.join(settings.BASE_DIR,"igdb_python_api")
GAMES_PATH = os.path.join(settings.BASE_DIR,"games")
sys.path.append(IGDB_PATH)

from igdb_python_api import code
 

def createDjangoFixture(model_name,start_pk,filename,json_data,required_fields,field_map): 
    assert model_name != None 
    assert start_pk != None 
    assert json_data != None 

    json_list = []


    current_pk = start_pk 
   
    for obj in json_data: 
        json_dict={}
        json_dict["model"]=model_name 
        json_dict["pk"] = current_pk
        json_sub={}
        for field in obj : 
            #print(field)
            if field=='id' : 
                json_dict["pk"] = obj["id"]
            if field in required_fields : 
                field_alias = field_map[field]
                
                json_sub[field_alias] = obj[field]
        
        json_dict["fields"] = json_sub
        
        json_list.append(json_dict)
        
        current_pk = current_pk + 1 
       
    #print(json_list)
    json_obj = json.dumps(json_list)

    if filename : 
        with open(filename,"w",encoding="utf-8") as json_file : 
            json.dump(json_list,json_file,indent=4)
        
    return json_obj




igdb_handler = code.IGBRequest(media_path="media")



def CreateGameFixture() : 
## Create fixture for Game model 

    FIELDS=[
        "name",
        "summary",    
        "rating",
        "popularity",
        "url",
    ]

    FIELD_MAP={
        "name":"name" , 
        "summary":"summary",
        "rating":"ratings",
        "popularity":"popularity",
        "url":"igdb_url"
    }

    response = igdb_handler.getTopnPopularGames(n=10,fields=FIELDS,cover=True)
    createDjangoFixture(model_name="games.Game",
                        start_pk=1,
                        filename="game_initial_fixture.json",
                        json_data=response,
                        required_fields=FIELDS,
                        field_map=FIELD_MAP
                        )

    pass 

def CreateCoverFixture() : 
    ## Create fixture for Cover model 

    FIELDS=[
        "cover.*"
    ]
    response = igdb_handler.getTopnPopularGames(n=10,fields=FIELDS)
    print(response)
    pass 

