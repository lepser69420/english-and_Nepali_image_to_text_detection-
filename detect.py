import pytesseract
from PIL import Image
from langdetect import detect_langs



def detect_language(word):
    try:
        a = detect_langs(word)
        return a
    except:
        return []

def extract_words_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang="nep+eng")
    word = text.split()
    return word


print(extract_words_from_image('img.png'))
def classify_words(words):
    english = []
    nepali = []

    for word in words:
        lang_list = detect_language(word)
        #print(word, lang_list)
        if lang_list:
            lang = lang_list[0].lang
            if lang == 'en':
                english.append(word)
            elif lang == 'ne':
                nepali.append(word)

    return english, nepali





ocr_result = pytesseract.image_to_string(img)

print(ocr_result)
