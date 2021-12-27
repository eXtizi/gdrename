from urllib.parse import unquote
from pydrive2.auth import GoogleAuth
gauth = GoogleAuth()
from pydrive2.drive import GoogleDrive
list_=['mkv','mp4']
drive = GoogleDrive(gauth)


def list_shared_drive(driveid):
 for i in list_:
    heh='fullText contains "{}"'.format(i)
    file_list = drive.ListFile({'q' : heh,
                              "corpora" : 'drive',
                              "driveId" : driveid,
                              "includeItemsFromAllDrives" : "true",
                              "supportsAllDrives" : "true"}).GetList()
    print(i)
    for file1 in file_list:
     if ('_' in file1['title']) :
        file1['title'] = file1['title'].replace('_','.')
        file1.Upload()
        print(file1['title'])


list_shared_drive('0AJr0pB8kNY5nUk9PVA')
