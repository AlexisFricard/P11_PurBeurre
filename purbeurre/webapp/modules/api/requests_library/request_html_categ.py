import requests


def html_categorie_from_product_url(url):

    requete = requests.get(url)
    html = requete.text

    if '<label style="display:inline;font-size:1rem;">' in html:

        text_stage_1 = html.find('<label style="display:inline;font-size:1rem;">')

        # REMOVE BEFORE <label ...
        start_point = html.find('<label style="display:inline;font-size:1rem;">')
        text_1 = html[start_point:]

        # REMOVE AFTER </label> INCLUDE
        end_point = text_1.find('</label>')
        text_2 = text_1[0:end_point]

        # REMOVE LABEL & INPUT THEN CLEAN TEXT
        start_point = text_2.find('<label ')
        end_point = text_2.find('comparison">') + len('comparison">')
        txt_to_replace = text_2[start_point:end_point]
        text = text_2.replace(txt_to_replace, "").strip()

        return(text)