# TwitterFollowing
Pulling information from those whose presence brings you joy. It now screenshots and saves in the directory it runs in.

## Warning: Make sure the script is in a new directory.

- Screenshots will be flooding in as it runs and it will probably take half an hour or longer depending on how many users you follow.

### How to Use

1. Download your Twitter data: https://twitter.com/settings/download_your_data

2. Go into the "data" folder and open "following.js"

3. Copy contents into [CyberChef](https://cyberchef.org/) and use the recipe in "CyberChefRecipe.txt" to clean it up. Save that as "following.txt" (Select the folder icon in cyberchef and 'load recipe')

4. Run FollowingCheck.py and wait while it copies the name, bio, and website of everyone you follow into "Contacts.csv"

### Requires

Selenium, I had to force update requests and then urllib to get the right versions

`python -m pip install selenium`
