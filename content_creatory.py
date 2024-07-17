import re
from aqt import mw

def create_mind_map(card_content_html, card_id):
    words = get_content(card_content_html)
    print(words)
    print("german_words:")
    german_words = words[0]
    print(german_words)
    print("chinese_word:")
    chinese_word = words[1]
    print(chinese_word)
    print("pinyin:")
    pinyin = words[2]
    print(pinyin)
    print("serarching in german words:")
    list_of_words = []
    for word in german_words.split(","):
        list_of_words.append(find_same_cards(word.strip(), card_id))
    print("all words found: ", list_of_words)


'''
<style>.card {
 font-family: SimSunl;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
}
</style><span style="font-size: 42px; ">Nenne Lernorte der betrieblichen Ausbildung</span>

<hr id=answer>

<span style="font-family: SimSun; font-size: 70px; ">Betrieb und Berufschule</span>
end total
start get_content
'''
def get_content(card_content_html):
    pattern = r'(?:>)([^<>{}]+)(?:<)'
    cleaned_text = card_content_html.replace("\n", "").replace("\r", "")
    # Use re.findall to find all matches with captured groups
    matches = re.findall(pattern, cleaned_text)
    print(matches)
    return [item for item in matches if item.strip() != ""]


'''
['\n        ',
 '<style>',
 '.card {\n'
 ' font-family: SimSunl;\n'
 ' font-size: 24px;\n'
 ' text-align: center;\n'
 ' color: black;\n'
 ' background-color: white;\n'
 '}\n',
 '</style>',
 '',
 '<span style="font-size: 42px; ">',
 'Nenne Lernorte der betrieblichen Ausbildung',
 '</span>',
 '\n\n',
 '<hr id=answer>',
 '\n\n',
 '<span style="font-family: SimSun; font-size: 70px; ">',
 'Betrieb und Berufschule',
 '</span>',
 '\n        ']
'''

def find_same_cards(word, card_id):
    print("Find same word for :", word)
    col = mw.col  # Das ist die Datenbankverbindung
    results = col.findNotes(f"{word}")
    print("Found following results: ", results)
    notes = []
    for result_id in [result for result in results if result != card_id] :
        note = col.getNote(result_id)
        print("adding note: ", note)
        notes.append(note)
    return notes
