import webbrowser
import urllib.parse

def open_site(site: str):
    print(f"🌐 open_site called | site={site}")
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "github": "https://github.com",
    }

    url = urls.get(site.lower())
    if url:
        webbrowser.open(url)

def search_web(engine: str, query: str):
    print(f"🌐 search_web called | engine={engine}, query={query}")
    query = urllib.parse.quote_plus(query)

    if engine == "google":
        url = f"https://www.google.com/search?q={query}"
    elif engine == "youtube":
        url = f"https://www.youtube.com/results?search_query={query}"
    else:
        return

    webbrowser.open(url)
