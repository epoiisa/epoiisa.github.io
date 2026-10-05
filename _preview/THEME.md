# Unfettered theme maintenance

This site consumes the public `epoiisa/unfettered@main` remote theme through `jekyll-remote-theme`. Tracking `main` is an intentional owner decision: every fresh build fetches the branch's current contents, so successive builds can change without a site commit. Site content, titles, description, URL, empty baseurl and Markdown navigation remain owned here. Every current content page selects `layout: default` in front matter.

The central theme owns `_layouts/default.html`, `_includes/breadcrumbs.html` and `assets/css/style.css`. Do not restore copies at those paths: local files override the remote theme. This repository has no exporter or generated-site ownership manifest; the JSON manifests under mechanics assets describe content assets and remain untouched.

## Site customisation

`_includes/guild-invite.html`, `assets/js/guild-invite.js` and `assets/css/guild-invite.css` retain the Frostborn Exiles invitation and remembered dismissal. The site-owned `_includes/navigation.html` loads the additional CSS and invitation through the central layout's navigation slot. The banner now appears after the site title and before breadcrumbs.

This include deliberately overrides Unfettered's optional navigation include because the theme has no separate banner hook. As a result, central changes to `navigation.html` do not apply here, and adding `_data/navigation.yml` alone will not render a navigation bar. Current navigation remains the existing content links and central breadcrumbs. To adopt central navigation later, first agree on a central extension hook or explicitly revise this site-owned include. The layout, breadcrumbs and core CSS otherwise come directly from Unfettered.

## Build and verify

Ruby, Bundler and Python 3 are required. From the repository root:

```sh
export BUNDLE_PATH="$PWD/.preview/gems"
export BUNDLE_GEMFILE="$PWD/_preview/Gemfile"
bundle install
bundle exec jekyll build --destination .preview/theme-check
python3 _preview/verify-theme.py .preview/theme-check
bundle exec jekyll build --baseurl /theme-check --destination .preview/theme-baseurl-check
python3 _preview/verify-theme.py .preview/theme-baseurl-check --baseurl /theme-check
```

These builds use the actual public remote theme; no local theme checkout or replacement configuration is used. Verification checks all content pages, branding, descriptions, content navigation, breadcrumbs, central and site stylesheet URLs, banner scripts, local resource resolution and the published file inventory. The site configuration identifies the consumed ref; ordinary build logs identify the remote repository. `preview.command` continues to start the local live preview using the same Gemfile and site configuration. Inspect the rendered pages when changing presentation.

All documentation, dependency files and verification tooling live under excluded `_preview`; generated builds and downloaded inspection files live under ignored and excluded `.preview`. Do not publish these directories.

## Updating the theme

1. In the theme's own authorised workflow, verify its changes, publish `main` and, when making a release, publish and verify the new signed release tag using its public remote-theme verification tooling. This migration does not authorise changes in that repository or resolve its licence choice.
2. This site intentionally keeps `remote_theme: epoiisa/unfettered@main`. Rebuild to consume the updated public branch. Inspect theme changes since the last verified build, especially the navigation slot used by the banner.
3. Run both builds and verification commands above, inspect branding, content links, breadcrumbs, banner behaviour and light/dark styles, then publish this site only with explicit authorisation.

Theme changes alone do not trigger builds of consuming Pages sites. Rebuild this site explicitly after a theme update; cross-repository automation is not configured.

If release pinning is wanted later, publish and verify a new Unfettered release first, explicitly change this site's `remote_theme` to `epoiisa/unfettered@vX.Y.Z`, then rebuild, inspect and publish this site. Further upgrades then require an explicit tag update. Do not use a local theme checkout as evidence that a published ref builds.

## Migration verification — 2026-10-05

Public `main` was observed at `25e2448fd662ede5ad79dbe548d8e9ab353f4900`. Both public remote-theme builds passed: 28 pages and 129 published files, with empty baseurl and `/theme-check`. No private documentation, dependency files, preview tooling or theme repository metadata appeared in the published inventory. The published core stylesheet matched the downloaded public theme stylesheet exactly.

A build of the pre-migration Git snapshot confirmed unchanged rendered titles, content sections (including content navigation) and breadcrumbs on all 28 pages. Browser inspection confirmed branding, stylesheet loading, content navigation and banner dismissal persisting across reload and page navigation. The banner's position moved below the site title, as described above. No commits, pushes, publication, deployment, automation or changes to another project were performed. The theme's licence choice was left unchanged.
