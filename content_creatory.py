from aqt import mw

front_field_name = ""

def create_mind_map(card_id):
    global front_field_name
    # Holen Sie sich die Notiz zur gegebenen Karte
    card = mw.col.getCard(card_id)
    note = card.note()

    print(note)
    print(note.keys())
    print("note.keys()")
    print("note.items()")
    print(note.items())
    front_content = ""
    back_content = ""
    if "Front" in note.keys():
        front_field_name = "Front"
        print(note.__getitem__("Front"))
        front_content = note.__getitem__("Front")
        print(note.__getitem__("Back"))
        back_content = note.__getitem__("Back")
    else:
        front_field_name = "Vorderseite"
        print(note.__getitem__("Vorderseite"))
        front_content = note.__getitem__("Vorderseite")
        print(note.__getitem__("Rückseite"))
        back_content = note.__getitem__("Rückseite")
    # Extrahiere die Inhalte der Felder "Front" und "Back"



    print("Front content:")
    print(front_content)
    print("Back content:")
    print(back_content)

    # Teile den Back-Inhalt in deutsche Wörter, chinesisches Wort und Pinyin
    words = get_content(front_content, back_content)

    # Extrahiere die spezifischen Wortkategorien
    german_words = words[0]
    chinese_word = words[1]
    pinyin = words[2]

    # Ausgabe der extrahierten Wörter
    print("german_words:")
    print(german_words)
    print("chinese_word:")
    print(chinese_word)
    print("pinyin:")
    print(pinyin)

    # Suche nach ähnlichen Karten, die die deutschen Wörter enthalten
    print("Searching in german words:")
    list_of_similar_words = []
    for word in german_words.split(","):
        found_words = find_similar_cards(word.strip(), card_id)
        list_of_similar_words.append(found_words)

    # Ausgabe der gefundenen ähnlichen Wörter
    print("All similar words found: ", list_of_similar_words)


def get_content(front_content, back_content):
    # Angenommen, dass front_content deutsche Wörter und back_content chinesisches Wort und Pinyin enthält
    # Der folgende Code sollte an das spezifische Format der Felder angepasst werden
    german_words = front_content
    chinese_word, pinyin = back_content.split("<div>", 1)
    return [german_words, chinese_word, pinyin]


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def find_similar_cards(word, card_id, threshold=3):
    global front_field_name
    print("Find similar word for:", word)
    col = mw.col  # Verbindung zur Anki-Datenbank
    results = col.findNotes(f"{word}")
    print("Found following results: ", results)
    similar_notes = []



    for result_id in [result for result in results if result != card_id]:
        note = col.getNote(result_id)
        front_content = ""
        back_content = ""
        if "Front" in note.keys():
            front_field_name = "Front"
            print(note.__getitem__("Front"))
            front_content = note.__getitem__("Front")
            print(note.__getitem__("Back"))
            back_content = note.__getitem__("Back")
        else:
            front_field_name = "Vorderseite"
            print(note.__getitem__("Vorderseite"))
            front_content = note.__getitem__("Vorderseite")
            print(note.__getitem__("Rückseite"))
            back_content = note.__getitem__("Rückseite")
        print(front_content)
        print(back_content)

        distance = levenshtein_distance(word, front_content)

        if distance <= threshold:
            print(f"Found similar word: {front_content} (Distance: {distance})")
            similar_notes.append(note)

    return similar_notes

# Beispielaufruf der Funktion
# create_mind_map(card_id)  # card_id sollte durch eine tatsächliche Karten-ID ersetzt werden
