#!/usr/bin/env python3

"""
This script prints the list of public repositories from a user.
For each repository the output includes some details like the repository name, the topics, the language ...
It doesnt include the repositories comming from a fork.
"""

import json
import requests

def get_details_about_a_repo(repo):
    name = repo['name']
    description = repo['description']
    if not description:
        description = ''
    topics = str(repo['topics'])
    if not topics:
        topics = ''
    language = str(repo['language'])
    stars = str(repo['stargazers_count'])
    url = repo['html_url']
    details = 'Name: ' + name + '\n' + 'Description: ' + description + '\n' + 'Topics: ' + topics + '\n' + 'Language: ' + language + '\n' + 'Stars: ' + stars + '\n' + 'URL: ' + url + '\n''*******************'
    return (details)

def main():
    page = 1
    user = 'ksator'
    URL = 'https://api.github.com/users/' + user + '/repos?page=' + str(page)
    response = requests.request("GET", URL)
    for repo in response.json():
        if repo['fork'] == False:
            to_print = get_details_about_a_repo(repo)
            print(to_print)

    while 'rel="last"' in response.headers['link']:
        page = page + 1
        URL = 'https://api.github.com/users/' + user + '/repos?page=' + str(page)
        response = requests.request("GET", URL)
        for repo in response.json():
            if repo['fork'] == False:
                to_print = get_details_about_a_repo(repo)
                print(to_print)

if __name__ == '__main__':
    main()
