from django.shortcuts import render
from dotenv import load_dotenv, dotenv_values
import os
from groq import Groq

load_dotenv()

# Create your views here.

def llm_view(request):

    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": "Tell me about Dr Doom"
            }
        ],
        # temperature=1,
        # max_tokens=1024,
        # top_p=1,
        # stream=False,
        # response_format={"type": "json_object"},
        # stop=None,
    )

    print(completion.choices[0].message.content)

    return render(request, 'dashboard.html')            

