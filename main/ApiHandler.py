import requests
import os
import json

class RequestPuller:
  def __init__(self):
    pass
  
  def test_init(self):
    print("RequestPuller initialized successfully.")
    pass 
  
  def GET(url, filePath):
    response = requests.get(url)
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
    
    def RepoForks(self, Owner, Repo, filePath):
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