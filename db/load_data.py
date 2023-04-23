import pandas as pd
import sqlite3

def url_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('CREATE TABLE urls (url TEXT PRIMARY KEY)')
    # c.execute('ALTER TABLE phishing ADD COLUMN Index INTEGER PRIMARY KEY AUTOINCREMENT;')

    conn.commit()
    conn.close()

def db_connect():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('../phishing.csv')
    df.columns = ['Index', 'UsingIP', 'LongURL', 'ShortURL', 'Symbol', 'Redirecting', 'PrefixSuffix', 'SubDomains',
                'HTTPS', 'DomainRegLen', 'Favicon', 'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
                'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL', 'WebsiteForwarding',
                'StatusBarCust', 'DisableRightClick', 'UsingPopupWindow', 'IframeRedirection', 'AgeofDomain',
                'DNSRecording', 'WebsiteTraffic', 'PageRank', 'GoogleIndex', 'LinksPointingToPage', 'StatsReport',
                'class']
    # Save the DataFrame to the SQLite database
    df.to_sql('phishing', conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()

db_connect()
# url_db()