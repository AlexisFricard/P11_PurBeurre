import requests
from textblob import TextBlob

from webapp.modules.tools.clean_sentence import clean_accents, clean_space


def html_categorie_from_product_url(url):

    requete = requests.get(url)
    html = requete.text

    if '<label style="display:inline;font-size:1rem;">' in html:

        # REMOVE BEFORE <label ...
        start_point = html.find(
            '<label style="display:inline;font-size:1rem;">'
        )
        text_1 = html[start_point:]

        # REMOVE AFTER </label> INCLUDE
        end_point = text_1.find('</label>')
        text_2 = text_1[0:end_point]

        # REMOVE LABEL & INPUT THEN CLEAN TEXT
        start_point = text_2.find('<label ')
        end_point = text_2.find('comparison">') + len('comparison">')
        txt_to_replace = text_2[start_point:end_point]
        text = text_2.replace(txt_to_replace, "").strip()

        # TRANSLATE IN FRENCH
        blob = TextBlob(f'{text}')
        text = blob.translate(to='fr')
        if " " in text:
            text = clean_space(text, "-").lower()
            text = clean_accents(text)

        return text
