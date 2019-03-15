import zipfile
from urllib import request as urllib2
import os
import re


def git_clone(git_url, path=os.getcwd(), branch_name='master'):
    username, projectname = re.match(
        'https://github.com/(.+)/(.+)/?', git_url).groups()
    url = 'https://codeload.github.com/{}/{}/zip/{}'.format(
        username, projectname, branch_name)
    filename = path+'/'+projectname
    zipfile_name = filename + '.zip'
    try:
        data = urllib2.urlopen(url)
    except (urllib.error.URLError):
        headers['Host'] = 'github.com'
        request = urllib2.Request(
            'https://github.com/{}/{}'.format(username, projectname), headers=headers)
        response = urllib2.urlopen(request)
        pattern = '/{}/{}/tree/(.*?)/'.format(username, projectname)
        b_name = re.findall(pattern, str(response.read()))[-1]
        git_clone(name, path, b_name)
    with open(zipfile_name, 'wb') as f:
        f.write(data.read())
    with zipfile.ZipFile(zipfile_name, 'r') as f:
        f.extractall(path+'.')

    os.rename(filename+'-master', filename)
    os.remove(zipfile_name)
