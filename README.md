# **GitLab Merge Requests (menu bar app for Mac)**

[![check](https://github.com/colens-dev/macos-gitlab/actions/workflows/check-action.yml/badge.svg)](https://github.com/colens-dev/macos-gitlab/actions/workflows/check-action.yml)
[![release](https://github.com/colens-dev/macos-gitlab/actions/workflows/release-action.yml/badge.svg)](https://github.com/colens-dev/macos-gitlab/actions/workflows/release-action.yml)

GitLab Merge Requests is a MacOS menu bar app that shows number of opened MRs (owned and assigned as a reviewer) and enables quick navigation to specific MR on GitLab.

<p align="center">
    <img src="./images/banner.png" alt="drawing" width="2000"/>
</p>

### Motivation

- We work daily on multiple projects on GitLab 🦊, since we use merge request (MR) mechanism and we want to iterate quickly sometimes we have multiple opened MRs of our own and a few on which we are assigned as reviewers, when that happens there is some chance we will forget about an active MR which would prolong the task. Since we work on MacOS we thought that making a simple menu bar app would be a good way of solving that issue.

🌟 Look how beautiful it is 😍

<p align="center">
    <img src="./images/gitlab_integration_app_preview.png" alt="drawing" width="400"/>
</p>


### Features

- Present total number of your MRs and MRs on which you are assigned as a reviewer
- List all your MRs and enable navigation
- List all MRs on which you are assigned as a reviewer and enable navigation
- Setup of the app
- Quit the app

## Installing

Currently only manual installation is supported and have in mind that the app is not verified by Apple so some additional steps are required.

Steps:
- Download `release.zip` file from the latest [release](https://github.com/colens-dev/macos-gitlab/releases)
- Extract files from the `.zip` archive
- Move extracted file to your Applications folder
- Hold Control, click on the application file and once the menu popup is shown click on `Open`
- Now alert popup should appear
- If you see the option to open the application go ahead and open it 🎉
- In case you didn't get the option to open the application in the first try click on `Cancel`
    - Hold control and click on the app again, choose `Open` and a new alert should appear with the option to open the application 🎉
- After getting the app to open once, you shouldn't have any more problems in the future. Please refer to [Apple's documentation](https://support.apple.com/en-au/guide/mac-help/mh40616/mac) for further reference

## Setup

So you’ve installed the app, what next hmmm hmmm 🤔 SETUPPPPP YEAH 🥁

### In just few steps

1. If the installation went successfully you should see the new (way to cool) app in top menu bar like presented below, `x` means that the app is not connected so let’s change that

<p align="center">
    <img src="./images/app_not_connected.png" alt="App not connected image"/>
</p>
    
1. By clicking on the icon you will see a drop down menu
2. Notice that there is a preferences section, this is where the setup magic happens 🎩
3. Click on the `GitLab Username` and populate your username
4. Click on the `GitLab URL` and populate URL. In case you are using GitLab Cloud you can leave this one empty
5. Click on the `GitLab Token` and setup your personal token. In case you don’t have one read this [guide](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) on how to set it up
6. Wohoooooo all should be done and ready now 🎈

### **Launch on startup**

If you want to have this app active all the time you should configure your OS to launch this app on startup, if not have in mind that after every system restart you would need start the app manually.

For setting up launch on startup check this [guide](https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/mac)

## Contributing
First make sure you've checked details within the [CONTRIBUTING.md](https://github.com/colens-dev/macos-gitlab/blob/main/CONTRIBUTING.md) file.

### Development
Steps for development setup are presented below:

- Clone the repo
- Navigate to the repo root folder
- run `make setup` to install all dev and prod dependencies (it uses [pip](https://pip.pypa.io/en/stable/))
- You are ready to go 🥳 
    - For example you are using [VSCode](https://code.visualstudio.com/) just start the debug while [main.py](https://github.com/colens-dev/macos-gitlab/blob/main/main.py) file is opened

**How to run tests:**
- From the root folder run `make test`

**How to run lint:**
- From the root folder run `make lint`

You can also run `tests` and `lint` together by running `make check`


#### Roadmap
- Currently these are all the features we need but in case we and some more people find something else useful we can build it up. If this app shows useful to certain amount of people or we find that we need some options which are not available in this super awesome and simple lib ([rumps](https://rumps.readthedocs.io/en/latest/)) we could switch it to [Electron](https://www.electronjs.org/) and make it available for all platforms (Mac, Windows, Linux)

## **License**

- [MIT](LICENSE.md)



