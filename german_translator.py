import pandas as pd
from translate import Translator

# Print the introduction message
intro_message = """
Prekladám...
"""

print(intro_message)

# Load your CSV file with UTF-8 encoding
df = pd.read_csv('german.csv', encoding='utf-8')

# Initialize the translator with MyMemory service
translator = Translator(to_lang="sk", from_lang="de")

# Function to translate English to Slovak
def translate_to_slovak(text):
   translation = translator.translate(text)
   return translation

#Takto adaptuj excel
#'Column_A' - 'German', 'Column_B' - 'Slovak'

df['Slovak'] = df['German'].apply(translate_to_slovak)

# Decapitalize all words in column B (Slovak translations)
df['Slovak'] = df['Slovak'].str.lower()

# Save the translated DataFrame to a new CSV file with UTF-8 encoding and BOM
df.to_csv('translated_file.csv', index=False, encoding='utf-8-sig')

# Print a message indicating that the file has been uploaded
upload_message = "Slovíčka máš preložené! :-)"
print(upload_message)
input("Stlač nejakú klávesu na zavretie aplikácie ")