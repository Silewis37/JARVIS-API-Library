import requests
import os
import json

class RequestPuller:
  def __init__(self):
    pass
  
  def test_init(self):
    print("RequestPuller initialized successfully.")
    pass 
  
  def GET(url, headers, filePath):
    h = headers
    response = requests.get(url, headers=h)
    with open(filePath, "w+") as f:
      json.dump(response.json(), f, indent=4)


class Github:
  def __init__(self, token):
    self.token = token
    pass

  def test(self):
    print("Github API initialized successfully.")
    pass 
  
  class Repo:
    def RepoForksList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/forks"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoActivityList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/events"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoBranchesList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/branches"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoCommitList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/commits"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoDeploymentsList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/deployments"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoTagsList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/tags"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoIssuesList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/issues/events"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
        
    def RepoCollaboratorsList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/collaborators"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def RepoReleasesList(self, Owner, Repo, filePath):
      url = f"https://api.github.com/repos/{Owner}/{Repo}/releases"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()

  class User:
    def UserStarredList(self, filePath):
      url = f"https://api.github.com/user/starred"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
    
    def UserFollowersList(self, filePath):
      url = f"https://api.github.com/user/followers"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
        
    def UserFollowingList(self, filePath):
      url = f"https://api.github.com/user/following"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
        
    def UserRepositoryList(self, username,filePath):
      url = f"https://api.github.com/users/{username}/repos"
      h = {
      "Accept": "application/vnd.github+json",
      "Authorization": f"Bearer {self.token}",
      "X-GitHub-Api-Version": "2022-11-28"
      }
      response = requests.get(url, headers=h)
      print(response.json())
      with open(filePath, "w+") as f:
        data4 = json.dumps(response.json(), indent=4)
        f.write(data4)
        f.close()
        
class Nutritionix:
  def __init__(self, app_id, app_token):
    self.appId = app_id
    self.appToken = app_token
    pass
  
  