# Spotify Now Playing

A small widget that displays the currently playing song and top tracks on Spotify. The widget is designed to be used in GitHub profiles.

This is a fork of [ntthn0/Spotify-Readme](https://github.com/tthn0/Spotify-Readme). The original `README.md` is kept [here](./README-original.md) on the side, but the instructions and previews are also below.

## Features

- Shows the currently playing song on Spotify.
- If nothing is playing, shows a randomly chosen track from the recently played 10 tracks of the user.
- Multiple customization options, as shown in the previews below.

## Previews

#### Default
```
/api
```
![Preview](https://lentidas-now-playing.vercel.app/api)

#### Spinning CD Effect
```
/api?spin=true
```
![Preview](https://lentidas-now-playing.vercel.app/api?spin=true)

#### Include Scan Code
```
/api?scan=true
```
![Preview](https://lentidas-now-playing.vercel.app/api?scan=true)

#### Rainbow Equalizer
```
/api?rainbow=true
```
![Preview](https://lentidas-now-playing.vercel.app/api?rainbow=true)

#### Dark Theme
```
/api?theme=dark
```
![Preview](https://lentidas-now-playing.vercel.app/api?theme=dark)

## Setup/Deployment

:warning: The instructions below are different from the ones in the original [`README.md`](https://github.com/tthn0/Spotify-Readme/blob/1dd070c3a0e1bc027f230e3653120b5e69dc56f2/README.md).

This will take approximately 5 minutes.

> [!NOTE]  
> This guide was last updated on Aug 30, 2023. The steps might differ slightly in the future if Spotify or Vercel updates their website interfaces.

#### 0. Star This Repo (Mandatory) 🌟

  * Yes, this step is required.

#### 1. Spotify's API 🎶

* Head over to <a href="https://developer.spotify.com/dashboard/">Spotify for Developers</a>.
  * Accept the Terms of Service if necessary.
  * Verify your email address if you haven't done so already.
  * Click on the **Create app** button.
    * In the **App name** & **App description** fields, you may put whatever you want.
    * In the **Redirect URI** field, add `https://localhost:3000/callback`.
    * Agree with Spotify's TOS and click **Save**.
  * Click on the **Settings** button.
  * Take note of the **Client ID** & **Client Secret**.

#### 2. Intermediary Steps 🛠️

```
https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&scope=user-read-currently-playing,user-read-recently-played,user-top-read&redirect_uri=https://localhost:3000/callback
```

* Copy and paste the above link into your browser.
  * Replace `{CLIENT_ID}` with the **Client ID** you got from your Spotify application.
  * Visit the URL.
    * Log in if you're not already signed in.
    * Click **Agree**.
* After you get redirected to a blank page, retrieve the URL from your browser's URL bar. It should be in the following format: `http://localhost:3000/callback?code={CODE}`.
  * Take note of the `{CODE}` portion of the URL.
* Head over to <a href="https://base64.io">base64.io</a> or use the command `echo -n "{CLIENT_ID}:{CLIENT_SECRET}`.
  * Create a string in the form of `{CLIENT_ID}:{CLIENT_SECRET}` and encode it to base 64.
  * Take note of the encoded base 64 string. We'll call this `{BASE_64}`.
* If you're on Windows or don't have the `curl` command, head over to <a href="https://httpie.io/cli/run">httpie.io/cli/run</a>.
  * Press enter.
  * Clear the pre-filled command.
* If you're on Linux or Mac with the `curl` command, open up your preferred terminal.
* Run the following command (replace `{BASE_64}` and `{CODE}` with their respective values):

  ```bash
  curl \
    -X POST \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -H "Authorization: Basic {BASE_64}" \
    -d "grant_type=authorization_code&redirect_uri=https://localhost:3000/callback&code={CODE}" \
    https://accounts.spotify.com/api/token
  ```

* If you did everything correctly, you should get a response in the form of a JSON object.
  * Take note of the `refresh_token`'s value. We'll call this `{REFRESH_TOKEN}`.

#### 3. Host on Vercel 🌀

* Fork this repository.
* Head over to <a href="https://vercel.com">Vercel</a> and create an account if you don't already have one.
  * Add a new project.
    * Link your GitHub account if you haven't done so already.
    * Make sure Vercel has access to the forked respository.
    * Import the forked respository into your project.
      * Give it a meaningful project name.
      * Keep the default options for the other settings.
      * Add the following environment variables along with their appropriate values:
        * `CLIENT_ID` ⇒ `{CLIENT_ID}`.
        * `CLIENT_SECRET` ⇒ `{CLIENT_SECRET}`.
        * `REFRESH_TOKEN` ⇒ `{REFRESH_TOKEN}`.
      * Click **Deploy**.
      * Click **Continue to Dashboard**.
        * Find the **Domains** field and take note of the URL.
          * Example: `{PROJECT_NAME}.vercel.app`.

#### 4. Add to your GitHub 🚀

* In any markdown file, add the following (replace `{PROJECT_NAME}` with the name you gave your Vercel project):

  ```html
  <a href="https://{PROJECT_NAME}.vercel.app/api/play">
    <img src="https://{PROJECT_NAME}.vercel.app/api" alt="Current Spotify Song">
  </a>
  
  <a href="https://github.com/tthn0/Spotify-Readme">Source Repo</a>
  ```

* Please leave the anchor tag hyperlink reference to this GitHub repo to retain creator credit and for other users to find! 

## Customization

<p>
  To customize the widget, add query parameters to the endpoint. There are many possible combinations! See how it pairs with other widgets on <a href="https://github.com/tthn0/tthn0">my own README</a>! (If you're on mobile and have a small screen, use a desktop browser or change the zoom level to zoom out.)
</p>

| Parameter | Default | Values          |
| :-------- | :------ | :-------------- |
| `spin`    | `false` | `false`, `true` |
| `scan`    | `false` | `false`, `true` |
| `theme`   | `light` | `light`, `dark` |
| `rainbow` | `false` | `false`, `true` |
| `top`     | `false` | `false`, `true` |
| `random`  | `false` | `false`, `true` |

## Keep Your Fork Up To Date

You can keep your fork, and thus your private Vercel instance up to date with the upstream using GitHub's <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork">Sync Fork button</a>.
