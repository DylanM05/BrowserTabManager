import webbrowser

def open_saved_tab_links():
    # Read the URLs from the plain text file
    with open('open_tab_links.txt', 'r') as f:
        tab_links = f.readlines()

    # Open each URL in Firefox
    for link in tab_links:
        webbrowser.open(link.strip())

    print("Tabs opened successfully!")

open_saved_tab_links()
