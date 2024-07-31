from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator



def translatorHTML(html_content,lenguage):
    soup = BeautifulSoup(html_content, 'html.parser')

    translator = GoogleTranslator(source='es', target=lenguage)

    def translate_tag_content(tag):
        if tag.string:
        
            translated = translator.translate(tag.string)
            tag.string.replace_with(translated)
        elif tag.contents:
        
            for content in tag.contents:
                if content.string:
                    translated = translator.translate(content.string)
                    content.replace_with(translated)

    for tag in soup.find_all(string=True):
        translate_tag_content(tag)

    return soup.prettify()
