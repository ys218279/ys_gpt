# ys_gpt
This is a personal project using the openai API

How does it work??

In your terminal run the script and parse in the the file path of the script you want to get reviewed.
    - This will read your file and will be use the contents as a prompt to ask a questions. 
    - In the terminal you will see your answer generated.

KEY NOTES:
======================================================
def configure():
    load_dotenv()
    openai.api_key = os.getenv('api_key')
======================================================

1)In order to make the function above work you need to create a ".env" file which you will use to store your API key. 
     - In the file simply put "api_key=......." (no quotes needed)
     - Make sure it is in the same dir as the gpt script. 
     - I have not included my .env file because I dont want anyone to see the API key because this it costs money to use the API
     
