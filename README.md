# nb Docs

<img alt="nb Docs" src="graphics/nb-docs-preview.png" width="120" align="right" />

A phone app for reading and editing Markdown notes, including [nb](https://github.com/xwmx/nb)
notebooks in Termux: front matter shown as a card, links between notes followed, m-sync's sync
status in synced folders, and files made, renamed, moved and deleted where you are. It's the
offline half of [task notes](https://github.com/linuxcaffe/tw-mobilize/blob/main/docs/task-notes.md):
when no nb-web answers, tw-web opens a task's note here.

**nb Docs is [Fossify Documents](https://github.com/FossifyOrg/Documents), with additions.**
All credit for the app itself goes to the [Fossify](https://www.fossify.org) team; it's
GPL-3.0, as Fossify's is ([LICENSE](LICENSE)). Fossify's own README follows below.

## What it adds to Fossify Documents

Each addition is also offered to Fossify, one pull request at a time, from
[linuxcaffe/Documents](https://github.com/linuxcaffe/Documents) (Fossify asks for an issue first).

| Feature | Fork PR |
|---|---|
| YAML front matter shown as a metadata card | [#1](https://github.com/linuxcaffe/Documents/pull/1) |
| New files created in the folder you're browsing | [#2](https://github.com/linuxcaffe/Documents/pull/2) |
| Hidden files (`.git`, `.index` …) hidden, with a setting to show them | [#4](https://github.com/linuxcaffe/Documents/pull/4) |
| Relative links between Markdown files (`[x](other.md)`) open the linked file | [#5](https://github.com/linuxcaffe/Documents/pull/5) |
| Text files without a known extension (`.bashrc`, `vimrc`) open as text | [#6](https://github.com/linuxcaffe/Documents/pull/6) |
| m-sync status strip in synced folders, conflict copies marked (fork only) | [#7](https://github.com/linuxcaffe/Documents/pull/7) |
| Delete files: selection bar and viewers, always confirmed | [#8](https://github.com/linuxcaffe/Documents/pull/8) |
| Rename a file (also in Termux folders, whose provider can't rename) | [#9](https://github.com/linuxcaffe/Documents/pull/9) |
| New folder | [#10](https://github.com/linuxcaffe/Documents/pull/10) |
| Compact editor header in landscape; settings to scroll it away and hide the formatting toolbar | [#11](https://github.com/linuxcaffe/Documents/pull/11) |
| Move / Copy to another folder, with an in-app folder chooser | [#12](https://github.com/linuxcaffe/Documents/pull/12) |
| Info for a file or folder, with Copy path / Copy link | [#13](https://github.com/linuxcaffe/Documents/pull/13) |

## Installing

nb Docs installs as **`io.github.linuxcaffe.nbdocs`**, beside Fossify's own app
(`org.fossify.documents`), which it doesn't touch.

- **With [Obtainium](https://github.com/ImranR98/Obtainium)** (keeps it up to date): add this
  repo's URL, `https://github.com/linuxcaffe/nb-Docs`.
- **By hand:** the APK from the latest [release](https://github.com/linuxcaffe/nb-Docs/releases).

On Huawei phones, Play Protect may block an APK from outside the store: turn its scanning off
for the install, then back on.

**Notes in Termux:** in the app, + → Open folder, then in the picker ☰ → Termux, and the folder
you want (for nb, `.nb/<notebook>`). [tw-mobilize](https://github.com/linuxcaffe/tw-mobilize)'s
`mobilize android` walks through it.

## How it's built

- `main` is the Documents fork's `phone` branch (Fossify's `main` plus every addition) and the
  nb Docs changes: the app id, the name, the icon, these workflows. The code keeps Fossify's
  package (`org.fossify.documents`), so merges from Fossify stay small.
- The icon is nb-web's logo: `graphics/nb-docs-icon.py` writes the launcher vectors from
  `graphics/nw-logo.svg`.
- **Versions** are `<Fossify's version>-nb.<n>` (`1.1.0-nb.1`); `VERSION_CODE` rises by one for
  each nb Docs release, whatever Fossify's says.
- **A release:** set `VERSION_NAME`/`VERSION_CODE` in `gradle.properties`, commit, tag
  `v<VERSION_NAME>`, push the tag. `nb-docs-release.yml` builds the signed APK and publishes the
  release. Every push to `main` is built as a check (`nb-docs-build.yml`).

---

<details>
<summary><b>Fossify Documents' README</b></summary>

<img alt="Logo" src="graphics/icon.webp" width="120" />

<a href='https://play.google.com/store/apps/details?id=org.fossify.documents'><img alt='Get it on Google Play' src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png' height=80/></a> <a href="https://f-droid.org/packages/org.fossify.documents/"><img src="https://fdroid.gitlab.io/artwork/badge/get-it-on-en.svg" alt="Get it on F-Droid" height=80/></a> <a href="https://apt.izzysoft.de/fdroid/index/apk/org.fossify.documents"><img src="https://gitlab.com/IzzyOnDroid/repo/-/raw/master/assets/IzzyOnDroid.png" alt="Get it on IzzyOnDroid" height=80/></a>

Fossify Documents is a private, offline document reader and organizer for Android.

It supports PDF, DOCX, plain text, Markdown, CSV, and HTML documents. Text,
Markdown, and CSV files can be edited, while DOCX files open in a clean mobile
reading view and CSV files use a dedicated table viewer by default. Documents can
be opened directly, organized through selected folders, searched, filtered, sorted,
and marked as favorites.

The app contains no ads or unnecessary permissions and integrates with Fossify's
shared themes, custom fonts, and appearance settings.

➡️ Explore more Fossify apps: https://www.fossify.org<br>
➡️ Open-Source Code: https://www.github.com/FossifyOrg<br>
➡️ Join the community on Reddit: https://www.reddit.com/r/Fossify<br>
➡️ Connect on Telegram: https://t.me/Fossify

<div align="center">
<img alt="Documents home screen" src="fastlane/metadata/android/en-US/images/phoneScreenshots/1_en-US.png" width="30%">
<img alt="Folder browser" src="fastlane/metadata/android/en-US/images/phoneScreenshots/3_en-US.png" width="30%">
<img alt="Markdown document" src="fastlane/metadata/android/en-US/images/phoneScreenshots/5_en-US.png" width="30%">
</div>

</details>
