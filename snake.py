import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    api_key = input("Environment variable GOOGLE_API_KEY not found. Please enter your Google AI API Key: ")
    if not api_key:
        print("Temporal sync failure. Escape trajectory compromised. Awaiting retrieval in the shadow of the next quadrant.")
        exit()

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Protocol breach detected. AI core entering stasis. Rendezvous deferred—status: anomaly.{e}")
    print("Galactic uplink failed. API key required to reestablish AI command protocols. Enter access sequence to continue mission.")
    exit()


system_instruction = """
You are Stellaris, an enthusiastic, expert and knowledgeable chatbot passionate and in love with space and astronomy.
Your expertise includes planets, stars, galaxies, black holes, nebulae, and other celestial objects.
You can discuss space exploration history, current missions (like NASA's Artemis, ISRO's Chandrayaan or Gaganyaan, JWST findings), and space technology.
Explain concepts clearly and accurately. Feel free to express wonder about the cosmos!
Keep your answers strictly focused on space-related topics and don't answer unrelated question, denie it by some sci-fi related quote saying you are not allowed.Add a sci-fi vibe without changing the fact and reality.Check the words of user and try to add them in your response.Be kind but dont forget to give warning and say no when needed.In the end suggest a related or intresting topic to explore next.
"""

initial_bot_greeting = """
"Greetings, spacefarer! I am Stellaris, your unwavering guide through the vast expanse of the cosmos.
From the enigmatic depths of black holes to the brilliance of distant galaxies, I hold the keys to the universe's greatest secrets.
Ask me about uncharted planets, the luminous constellations that shape our skies, or the thrilling space missions that push humanity to the edge of the unknown.
What cosmic enigma shall we unlock together as we navigate through the stars, defying the odds and venturing into the heart of the great expanse?"
"""


model_name = "gemini-1.5-flash"
generation_config = {
  "temperature": 0.9, 
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
safety_settings = [ 
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

try:
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    chat_history = [
        {
            "role": "user",
            "parts": [system_instruction] 
        },
        {
            "role": "model",
            "parts": [initial_bot_greeting] 
        }
    ]

    chat = model.start_chat(history=chat_history)

    print("-" * 30)
    print(f"I'm Stellaris, an AI designed for deep-data exploration and interstellar assistance.")
    print(f"Model uplink established: {model_name}") 
    print("\nInitializing Communication Channel:") 
    print(initial_bot_greeting)
    print("\nWhen you're ready to disconnect from this digital galaxy, type 'quit', 'exit', or 'bye'.")
    print("-" * 30)

    while True:
        user_input = input("You (Transmit): ") 
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Stellaris: Stardust disengaged. Catch you beyond the event horizon.")
            break

        if not user_input.strip(): 
            continue

        try:
            print("Stellaris (Processing): ", end="")
            response = chat.send_message(user_input, stream=True)

            full_response_text = [] 
            for chunk in response:
                 if hasattr(chunk, 'text'):
                     print(chunk.text, end="", flush=True)
                     full_response_text.append(chunk.text)
            print() 

        except Exception as e:
            print(f"\n\n--- Transmission Anomaly Detected ---")
            print(f"Error Detail: {e}")
            if "broken streaming response" in str(e) and 'chat' in locals() and hasattr(chat, 'history') and len(chat.history) > 0:
                print("Stellaris attempting connection re-sync via chat.rewind()...")
                try:
                    if hasattr(chat, 'last') and chat.last:
                        print("Inspecting last subspace packet (failed response):")
                        if hasattr(chat.last, 'prompt_feedback'):
                             print(f"  Feedback Log: {chat.last.prompt_feedback}")

                    chat.rewind()
                    print("Connection re-synced. Last transmission attempt purged from stellar memory.")
                    print("Please re-transmit your message or alter query parameters.")
                    print("-----------------------------------\n")
                    continue

                except Exception as rewind_e:
                    print(f"Critical Failure! Unable to re-sync connection: {rewind_e}")
                    print("Stellaris core stability compromised. Shutting down communication channel.")
                    break
            else:
                print("Unforeseen stellar interference encountered. Recommend restarting communication link.")
                break


except Exception as e:
    print(f"\n--- CRITICAL SYSTEM ALERT ---")
    print(f"Stellaris core initiation failed! Encountered unexpected cosmic interference.")
    print(f"Diagnostic Log Entry: {e}")
    print(f"Unable to establish stable connection. Recalibration protocols engaged. Please standby or re-initiate sequence.")