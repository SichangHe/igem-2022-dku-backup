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
open https://gitlab.oit.duke.edu/-/profile/keys
log in with your net id if asked to
### if you already generated a ssh key
just copy that one
if you have no idea, probably you did not do this

### macOS
open a new terminal (press ⌘` in vs code) and paste in
```zsh
ssh-keygen -t rsa
pbcopy < ~/.ssh/id_rsa.pub
```
### Windows
go to https://phoenixnap.com/kb/generate-ssh-key-windows-10
follow the guide to finish `Step 1` and `Step 2`
if you want to, continue following the guide, or I suggest you follow mine here
press the "windows key" and type in `cmd`, choose run as administrator
a black command prompt should pop up
type in `cd `
open file explorer
navigate to your `document` folder
drag whatever that says `document` to the black command prompt window
click the command prompt and press `enter`
paste in
```cmd
cd ..
ssh-keygen
```
press a bunch of `enter`s
paste in
```cmd
clip < .ssh\id_rsa.pub
```

### … and then
go back to the browser page and paste it in the biggest box which says `Typically starts with…`
fill the other boxes as you like
press the `Add key` button


## grab the project to your local folder
### Windows
you need to install `git bash`
### … and then
- find yourself a nice place on your computer to create the folder for this project
- open this folder with vs code
- open a new terminal in vs code (if you don't know how to do it, just google)
- click the terminal, and right click and paste in `git clone git@gitlab.oit.duke.edu:sh623/igem-2022-dku.git`

