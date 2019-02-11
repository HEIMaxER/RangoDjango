import json
import urllib, urllib2


def read_bing_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')
    return bing_api_key


def run_query(search_terms):
    bing_api_key = read_bing_key()
    if not bing_api_key:
        raise KeyError("Bing Key Not Found")

    root_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
    service = 'Web'

    results_per_page = 10
    offset = 0

    query = "'{0}'".format(search_terms)

    query = urllib.quote(query)

    search_url = "{0}?q={4}".format(
        root_url,
        service,
        results_per_page,
        offset,
        query)

    username = 'Plocharski'

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    password_mgr.add_password(None, search_url, username, bing_api_key)

    results = []

    try:

        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        print('OK')
        opener = urllib2.build_opener(handler)  # Py2.7.x
        print('OK')
        urllib2.install_opener(opener)  # Py2.7.x
        print('OK')
        print(search_url)
        response = urllib2.urlopen(search_url).read()  # Py2.7.x
        print('OK')
        json_response = json.loads(response)
        print('OK')
        print(json_response)
        for result in json_response['d']['results']:
            results.append({'title': result['Title'],
                            'link': result['Url'],
                            'summary': result['Description']})
    except:
        print("Error when querying the Bing API")

    return results

def main():

    def read_bing_key():

        bing_api_key = None
        try:
            with open('bing.key', 'r') as f:
                bing_api_key = f.readline()
        except:
            raise IOError('bing.key file not found')
        return bing_api_key

    def run_query(search_terms):
        bing_api_key = read_bing_key()
        if not bing_api_key:
            raise KeyError("Bing Key Not Found")

        root_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
        service = 'Web'

        results_per_page = 10
        offset = 0

        query = "'{0}'".format(search_terms)

        query = urllib.quote(query)

        search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
            root_url,
            service,
            results_per_page,
            offset,
            query)

        username = ''

        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

        password_mgr.add_password(None, search_url, username, bing_api_key)

        results = []

        try:

            handler = urllib2.HTTPBasicAuthHandler(password_mgr)
            opener = urllib2.build_opener(handler)  # Py2.7.x
            urllib2.install_opener(opener)  # Py2.7.x

            response = urllib2.urlopen(search_url).read()  # Py2.7.x

            json_response = json.loads(response)

            for result in json_response['d']['results']:
                results.append({'title': result['Title'],
                                'link': result['Url'],
                                'summary': result['Description']})
        except:
            print("Error when querying the Bing API")

        return results



if __name__ == '__main__':
    main()
