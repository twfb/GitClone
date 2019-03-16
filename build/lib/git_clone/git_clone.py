import zipfile
from urllib import request as urllib2
import os
import re
headers = {
    'User-Agent':
    r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'identity',
}


def git_clone(git_url, path=os.getcwd(), branch_name='master'):
    git_url = git_url.replace(' ', '')
    if git_url[-1] == '/':
        git_url = git_url[:-1]
    elif git_url[-4:] == '.git':
        git_url = git_url[:-4]
    username, projectname = re.match('https://github.com/(.+)/(.+)',
                                     git_url).groups()[0:2]
    url = 'https://codeload.github.com/{}/{}/zip/{}'.format(
        username, projectname, branch_name)
    filename = path + '/' + projectname
    zipfile_name = filename + '.zip'
    try:
        data = urllib2.urlopen(url)
    except (urllib.error.URLError):
        headers['Host'] = 'github.com'
        request = urllib2.Request(
            'https://github.com/{}/{}'.format(username, projectname),
            headers=headers)
        response = urllib2.urlopen(request)
        pattern = '/{}/{}/tree/(.*?)/'.format(username, projectname)
        b_name = re.findall(pattern, str(response.read()))[-1]
        git_clone(name, path, b_name)
    with open(zipfile_name, 'wb') as f:
        f.write(data.read())
    with zipfile.ZipFile(zipfile_name, 'r') as f:
        f.extractall(path + '.')

    os.rename(filename + '-master', filename)
    os.remove(zipfile_name)
