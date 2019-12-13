from github import Github 

g = Github("8c0e5202752a9f00b139b7d0f36bd79f75741975") 
 
#for repo in g.get_user().get_repos():
#   print(repo.name)

repo = g.get_repo("datarepresentationstudent/aPrivateOne") 
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt") 
urlOfFile = fileInfo.download_url 
print(urlOfFile)