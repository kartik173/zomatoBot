### Data Files

- **data/nlu/nlu.md** : contains training examples for the NLU model  
- **data/core/stories.md** : contains training stories for the Core model  

### Script Files

- **zomatoAPI.py** : contains Zomato API integration code
- **actions.py** : contains custom actions

### Config Files

- **config.yml** : contains model configuration and custom policy
- **domain.yml** : defines chatbot domain like entities, actions, responses, slots  
- **endpoints.yml** : contains the webhook configuration for custom action

## Usages
- **Changes to be done before running the application :**
In console.py of rasa/core/channels package, set ```DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS = 30```
Default setting is 10 seconds which is very less to complete the action of sending email.
For me the the complete path is - C:\Users\kartik.sharma10\AppData\Local\Continuum\anaconda3\Lib\site-packages\rasa\core\channels\

- **To train the model, use below command :**
```rasa train -vv -dump-stories --force```
This command will train both nlu and core

- **To test the model, run below command in different terminals:**
```rasa run actions```
```rasa shell```
