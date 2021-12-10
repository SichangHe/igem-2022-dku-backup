***If you see any terms in this document you do not know, please just search for it first and learn it yourself***

## install stuff
- install vs code
- open it
- find yourself a nice theme
- click `Extensions`
- type `markdown`
- install `Markdown All in One` and `Markdown Preview Enhanced`
- go back to the search bar and type `spell`
- install `Code Spell Checker`
- go back to the search bar and type `git`
- install `Git History` and `GitLens`
- go back to the search bar and type `gitlab`
- install `GitLab Workflow`
- go back to the search bar and type `tab`
- install `Tabnine`


## configure stuff
- open vs code setting
- in the search bar, type 'suggest enter'
- switch `Accept Suggestion On Enter` to `off`
- mess with other settings as you like :D

## set up ssh between your computer and GitLab
- open https://gitlab.oit.duke.edu/-/profile/keys, we will use it later
- log in with your net id if asked to
- finish one of the following depending on your situation, and then finish the **… and then** part

### if you already generated a ssh key
- just copy that one
- if you are not sure, generated ssh keys are usually in `.ssh/id_rsa.pub` under your user folder
- if you have no idea, probably you did not do this

### macOS
- open a new terminal (press ⌘` in vs code) and paste in
```zsh
ssh-keygen -t rsa
pbcopy < ~/.ssh/id_rsa.pub
```
### Windows
- go to https://phoenixnap.com/kb/generate-ssh-key-windows-10
- follow the guide to finish `Step 1` and `Step 2`
- copy the ssh key

### … and then
- go back to the browser page and paste it in the biggest box which says `Typically starts with…`
- fill the other boxes as you like
- press the `Add key` button


## grab the project to your local folder
### Windows
you need to install `git bash`
### … and then
- find yourself a nice place on your computer to create the folder for this project
- open this folder with vs code
- open a new terminal in vs code (if you don't know how to do it, just google)
- click the terminal, and right click and paste in `git clone git@gitlab.oit.duke.edu:sh623/igem-2022-dku.git`

## what then?
- you should see a folder named `igem-2022-dku` in vs code. open a new vs code window and open this folder, with this folder you can synchronize files with GitLab
- remember, everyone has a copy of this repository on their computer, so store large files like videos elsewhere and leave a link to refer to them
- actually we have another repository https://gitlab.oit.duke.edu/sh623/igem-2022-dku-big-files
and we use it as a Drive to store big files. just go to the repository and click the "+" to upload files one by one, or navigate to the file or folder you want to download and click the "download" icon to download
