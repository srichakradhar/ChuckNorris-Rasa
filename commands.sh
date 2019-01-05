#for training NLU

python3 -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose         

 

#for training core   
python3 -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue --epochs 200
    
#running the action server

python3 -m rasa_core_sdk.endpoint --actions actions

 

#run the bot for live interaction
python3 -m rasa_core.run -d models/current/dialogue -u models/current/nlu --endpoints endpoints.yml     

#To use the Interactive Learning feature of Rasa, run

python3 -m rasa_core_sdk.endpoint &

python3 -m rasa_core.train interactive -o models/dialogue  -d domain.yml -s stories.md --nlu models/current/nlu --endpoints endpoints.yml

# name the files as you have created it.
