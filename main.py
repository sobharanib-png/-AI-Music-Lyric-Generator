from transformers import pipeline

# Step 2: Load the GPT-2 text generation model
generator = pipeline("text-generation", model="gpt2")

# Step 3: Ask for user input
theme = input("🎶 Enter the song theme (e.g., love, friendship, motivation): ")

# Step 4: Generate the lyrics
lyrics = generator(
    f"Write a beautiful song about {theme}",
    max_length=100,
    num_return_sequences=1,
    temperature=0.9
)

# Step 5: Display the lyrics
print("\n🎵 Generated Lyrics 🎵\n")
print(lyrics[0]['generated_text'])
