# igem-2022-dku

This is temporarily where we dump our stuff.\
This project is for the iGEM 2022 competition as the DKU participants

For non-text files (`.docx` `.pdf` `.pptx` movies etc.),
please store in [this official OneDrive folder](https://prodduke-my.sharepoint.com/:f:/g/personal/sh623_duke_edu/EgjNqY1GXsZIusRPRf8mfc0BKV2JE-mSrYtPHVxpGQ6BXw?e=TmMyhU)

## for new members

- Please open [how-to-set-up.md](https://gitlab.oit.duke.edu/sh623/igem-2022-dku/-/blob/main/how-to-set-up.md)
    and follow the guide to set up.
- Please go to your icon at the top-right of GitLab page - `Edit Profile`,
    under `Main Settings`,
    change your `Full name` to your name, scroll down and `Update profile settings`,
    *so we know who you are on GitLab*.
    Go to the `Notifications` in the left panel,
    and change your `Global notification level` to `Watch`,
    *so you receive email notifications when something happens here*.

## view wiki locally

This wiki uses [mdBook](https://rust-lang.github.io/mdBook/index.html)
to build from Markdown.

Please read their documentation to learn how to use it.

To view the wiki locally,
please follow the instructions on their documentation to install mdBook.
After the installation,
open this repository in VSCode and open a new terminal.
Paste in:

```shell
mdbook serve --open
```

You should see the Home page.

If you edit and save any content files in `/src`,
it would live reload with the newest content.
