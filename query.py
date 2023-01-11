import requests

# Write successful words to a subset dictionary
with open("words.txt", "r") as infile, open("words_subset.txt", "w") as outfile:
    for word in infile:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)

        # Check for a 200 response
        if response.status_code == 200:
            outfile.write(word + "\n")
            print(f"{word} was successful.")
        else:
            print(f"{word} was not successful.")


