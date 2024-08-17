from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv, dotenv_values
import os
from groq import Groq

load_dotenv()

# Create your views here.

# Define the system message
system_message = {
    "role": "system",
    "content": "You are a summarization speacilization AI"
}

# Define the user messages
user_messages = {
    "role": "user",
    "content": '''I will provide you with reviews and its summary. Create a short summary 
    just as given in the example. Summary should just point out the product good and bad aspects, make it short paragraph of no more than 4 sentence.

    Reviews: One of my favorite features of this watch is the LARGE display. 
    Even with my less-than-perfect vision, the display is bright and easy to read, 
    whether I’m just checking time or date, checking messages, or looking at my 
    health statistics, (like my heart rate), I have no difficulty reading the screen. 
    The display is always bright, crisp and sharp.

    I was very surprised to find that the sound quality of the watch is equally as 
    impressive as the great display. Going up to 60dB, the speakers on the watch 
    make it possible for me to make phone calls, listen to messages, or even listen to music! 
    The microphone is equally as proficient so people have no problem hearing and understanding 
    what I’m saying when on a call.

    Pairing this fine smartwatch to Bluetooth is a cinch! It interfaced with my iPhone seamlessly. 
    The app works great, is easy to navigate, and makes using all the functions of the smartwatch 
    quite simple.

    My favorite features of the watch are the useful health and fitness offerings. The watch provides 
    constant checks on pulse rate, oxygen saturation, and even a stress-level check. The fitness 
    tracker verifies my pace and the amount of terrain I’ve covered (if I’m running or on a treadmill 
    for example), and also monitors the number of calories I’ve burned, my heart rate, and even notifies 
    me if any stat seems unusual or out of sync.

    The battery life of the watch is quite excellent as well. It only takes a max of 2-1/2 hours to 
    fully charge the watch, and the charge can last up to 14 days. A single charge typically keeps the 
    watch running for at least 10 days and sometimes more.

    I did a lot of research before making this purchase, and although I spent a lot less money than I could have, 
    I don’t believe I sacrificed any functionality. This watch has every feature I need or want.

    Summary should be like this and make it short: Customers like the quality, battery life, health monitoring, appearance and value of the wearable computer. They mention that it works great, has a great battery life and that it accurately monitors workouts and provides detailed information. They appreciate the design and the crisp display. Customers also mention that the watch is affordable and great for the price.


    Now for this review write the summary: I chose this dress for our family photos. This dress is very flattering and comfortable. It’s stretchy around the waste and arms. You don’t have to wear it off the shoulders. I was worried about this due to my job and the way that I work my arms are raised all day. I wear my sleeves on top of my shoulders. The skirt is very flowy a long with the fact that it’s long enough to cover everything so you do not feel concerned when bending over.

    The cost isn’t so bad for what you are getting. It has some sheerness to it but it’s still thick enough that if you didn’t want to wear a bra under neath you don’t have to.

    I definitely think this has versatility. You can wear this to work, or special events.Loved this dress!! I used it for my senior pictures and it was perfect!! It was true to size and held together well. It wasn’t super shear that you would need extra undergarments (like a slip or an under shirt or something). Overall a good dress!!This dress is light weight, great quality for the price, and is not see through at all. I purchased this dress in three colors (apricot, brown, and khaki) as I wanted the perfect neutral shade for our family photos. The colors in the photos online compared to what came were a bit off, which is why I knocked this review down to 4 stars. I ended up keeping the apricot color which was off-white and a bit less yellow than the photo. The brown was much more reddish than I had anticipated (I was hoping for a true, deep brown) and the khaki felt a bit lighter than the color in the image. Overall, the dress is great and worked perfectly, I was just a little thrown off with the colors that arrived.The material of this dress is perfect. It is perfect for a summer day, the material is nice and lightweight. My daughter chose this for graduation and she loved it! The back is super cute. Would buy from this seller again.This is a cute dress, but I felt that it was a little too short for me. For curvy women, in general, the chest (regardless of which way you wear this) is not flattering, nor does it offer support for large chests.Above the knee length but not too short, I love this dress

'''}


# Create a list to store the conversation
conversation = [user_messages]

conversation.append(system_message)


def llm_view(request):

    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=conversation,
        # temperature=1,
        # max_tokens=1024,
        # top_p=1,
        # stream=False,
        # response_format={"type": "json_object"},
        # stop=None,
    )

    summary = completion.choices[0].message.content
    print(completion.choices[0].message.content)

    return HttpResponse(f"<p>{summary}</p>")
    # return render(request, 'dashboard.html')
