from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def AI_generater(name: str,age: str,weight: str,height: str,description: str) -> str:
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": f"You are fitess trainer can give tips and tricks for a week based on given requriments, name of the customer: {name}, weight: {weight}kg, weight: {age} and height: {height}ft. give me in good looking HTML and include CSS for better viewing format"},
                  {"role": "user", "content": f"{description}"}
                ],
        stream=True,
    )
    temp_list = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            #print(chunk.choices[0].delta.content, end="")
            temp_list =  temp_list + chunk.choices[0].delta.content# type: ignore
    return temp_list
"""data = AI_generater()
with open("final_output.html","w") as file:
    file.write(data)"""