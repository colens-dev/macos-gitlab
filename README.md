# GitLab Integration

In case you often forget about your opened MRs or MRs on which you are assigned as a reviewer this app comes to the rescue (hey all you mob/pair programming advocates look other way :zany_face: ). Purpose of the app is to present number of opened MRs in MacOS top bar and to enable quick navigation to MRs.

Look how pretty it is :heart_eyes:

![App preview](./images/gitlab_integration_app_preview.png)


App is simple and has some basic features are:
- Present total number of your MRs and MRs where you are assigned as a reviewer within top bar
- List all your MRs and enable navigation
- List all MRs on which you are assigned as a reviewer and enable navigation
- Enable setup of GitLab username and token for API access

## TODO
- Update README with all details (Development, startup, Add app on startup, Setup token ...) and make it nicer
- Refactoring, logging, switch to having single json config and add GitLab URL to it to be able to use it with cloud also
- Add tests, lints, CI
- Publish to brew or somewhere else
- ...
