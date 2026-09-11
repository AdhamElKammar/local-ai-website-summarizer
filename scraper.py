import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(
            url=url,
            timeout=10,
            headers=headers
        )
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(
             f'Error while fetching website: {e}'
        )


    soup = BeautifulSoup(
        markup=response.text,
        features='html.parser'
    )

    useless_elements = ['style','script','noscript','svg','form','input','button','nav','footer','header','aside']
    for element in soup(useless_elements):
            element.decompose()
    '''
    main_content = soup.find('main')

    if main_content:
        content_source = main_content
    else:
        article = soup.find('article')

        if article:
            content_source = article
        else:
            content_source = soup.body if soup.body else soup
    '''
    
    useful_tags = soup.find_all(['h1','h2','h3','h4','h5','h6','p','li','a'])

    if not useful_tags:
        return soup.get_text(
            separator=' ',
            strip=True
        )
    
    seen = set()
    clean_lines = []

    for tag in useful_tags:

        if tag.name == 'a':
             if tag.find_parent(['h1','h2','h3','h4','h5','h6','p','li']):
                  continue
             
        text = tag.get_text(
            separator=' ',
            strip= True
        )

        if not text:
            continue

        if text in seen:
            continue

        seen.add(text)
        clean_lines.append(text)


    clean_txt = '\n'.join(clean_lines)

    if not clean_txt:
        raise RuntimeError('No useful content found')

    
    return clean_txt

    

    





    
    


    

    


