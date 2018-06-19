# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: test.py
@time: 2018/6/19 6:33
"""
from utils import *
from lxml import etree

html = '''
HTTP/1.1 200 OK
Date: Tue, 19 Jun 2018 21:34:09 GMT
Content-Type: text/html; charset=utf-8
Server: GitHub.com
Status: 200 OK
Cache-Control: no-cache
Vary: X-PJAX
X-PJAX-URL: https://github.com/steinvenic/toupiao/settings
X-PJAX-Version: 97b00481877aec129b0a9cbe2fbe1614
X-HTML-Safe: 035187acfd0760d0fad3603da1e1b254fd1f5f4e
Set-Cookie: user_session=kOawwbMEe1B1MHA6fBQlu6z0xMNJShWpncB1aI5Or6rkoVYg; path=/; expires=Tue, 03 Jul 2018 21:34:09 -0000; secure; HttpOnly
Set-Cookie: __Host-user_session_same_site=kOawwbMEe1B1MHA6fBQlu6z0xMNJShWpncB1aI5Or6rkoVYg; path=/; expires=Tue, 03 Jul 2018 21:34:09 -0000; secure; HttpOnly; SameSite=Strict
Set-Cookie: _gh_sess=Zy9VTHNWQkJGS3VueGw1YlpLOU80SFNEVHFTejRxUGpkVlQwVTNxNkZDSDVlRzd3OG5MVHlpQkVtenkzZG8wZjRpNjBhUkN4NzM1UTY2eDBGQTdTMEtyM2dCamRFdG5JUkhkaVR1Rmx3OEswUFUzSC93bk42UExmeHlSNVVBZlFZVTNzZWt2TTRNTldJRkFrN0xXR1JURkllNHY5K09xdGoyb3BqZzhqaFk3aVpoT1lqQThVVVFuVW44U2laNmlTS01CT3NsaHF5blZobUI5aUxOMW1TZGFtcEJTUzZOZld6YTJPZExLM0owZDNpVTVzMG9kSjUrcHRtVXR2K0NjWC0tRDZrQ1NWU3dvSVhjdFlZWS9QaFJjQT09--9f18c4bfd5e515b8de7aaa638dc6fd9d4d271ee1; path=/; secure; HttpOnly
X-Request-Id: 55312390-eddf-4c98-8be3-63ebdcd4f027
X-Runtime: 0.254727
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Frame-Options: deny
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Expect-CT: max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; connect-src 'self' uploads.github.com status.github.com collector.githubapp.com api.github.com www.google-analytics.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com wss://live.github.com; font-src assets-cdn.github.com; form-action 'self' github.com gist.github.com; frame-ancestors 'none'; frame-src render.githubusercontent.com; img-src 'self' data: assets-cdn.github.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com *.githubusercontent.com; manifest-src 'self'; media-src 'none'; script-src assets-cdn.github.com; style-src 'unsafe-inline' assets-cdn.github.com
X-Runtime-rack: 0.262029
Vary: Accept-Encoding
X-GitHub-Request-Id: DB00:02E1:591C17:85F168:5B2976CF
Content-Length: 46886








  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-autosubmit="true" data-remote="true" class="js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="SHbgEeS+HgIh4g9rtr3lmZjpBkOojyvKpMGkLWVYMRuiUtdI0HrG5H7BD7hTLKRr5WmdW/LOebs8PVLdoWLCGw==" />      <input type="hidden" name="repository_id" id="repository_id" value="129491522" class="form-control" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/steinvenic/toupiao/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:edit_repositories#options">
            <span class="js-select-button">
                <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Unwatch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/steinvenic/toupiao/watchers"
            aria-label="1 user is watching this repository">
            1
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_included" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_subscribed" value="subscribed" checked="checked" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_ignore" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/steinvenic/toupiao/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="gnOTCXTIe9h6we1FsY3rgmKzKnpKO8IhPPECCK/g9qMcxBjy8urxOUyI0FSwGl7+XC48A6Rr+bScWFjMZqGZfw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar steinvenic/toupiao"
        data-ga-click="Repository, click unstar button, action:edit_repositories#options; text:Unstar">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/steinvenic/toupiao/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/steinvenic/toupiao/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="L5ZtU9nwGanOl0mbO+XiltK9MlpdpT1YCuQjmZhLHwROEHxeDFj7tPsxVWcKCSa6IIHhntCkmXsFfVr0y3fXQA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star steinvenic/toupiao"
        data-ga-click="Repository, click star button, action:edit_repositories#options; text:Star">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/steinvenic/toupiao/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/steinvenic/toupiao/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="juPpG4Ywy2ziaPd4OjIxWDU9SfEmf+/j/efHXTzJn5WMuG3XJmtxfpUJr0x6CHMh2rBsxrbwbQ4lF9XhlSI6Qw==" />
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:edit_repositories#options; text:Fork"
                title="Fork your own copy of steinvenic/toupiao to your account"
                aria-label="Fork your own copy of steinvenic/toupiao to your account">
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/steinvenic/toupiao/network" class="social-count"
       aria-label="9 users forked this repository">
      9
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/steinvenic">steinvenic</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/steinvenic/toupiao">toupiao</a></strong>

    <span class="fork-flag">
      <span class="text">forked from <a href="/904356189/toupiao">904356189/toupiao</a></span>
    </span>
</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /steinvenic/toupiao" href="/steinvenic/toupiao">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /steinvenic/toupiao/pulls" href="/steinvenic/toupiao/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /steinvenic/toupiao/projects" href="/steinvenic/toupiao/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /steinvenic/toupiao/wiki" href="/steinvenic/toupiao/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /steinvenic/toupiao/pulse" href="/steinvenic/toupiao/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>
    <a class="js-selected-navigation-item selected reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations repo_keys_settings issue_template_editor /steinvenic/toupiao/settings" href="/steinvenic/toupiao/settings">
      <svg class="octicon octicon-gear" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"/></svg>
      Settings
</a>
</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <div class="columns">
    
<div class="column one-fourth" role="navigation" data-pjax>
  <nav class="menu">
    <a class="js-selected-navigation-item selected menu-item" data-selected-links=" /steinvenic/toupiao/settings" href="/steinvenic/toupiao/settings">Options</a>

      <a class="js-selected-navigation-item menu-item" data-selected-links=" /steinvenic/toupiao/settings/collaboration" href="/steinvenic/toupiao/settings/collaboration">Collaborators</a>

      <a class="js-selected-navigation-item menu-item" data-selected-links="repo_branch_settings /steinvenic/toupiao/settings/branches" href="/steinvenic/toupiao/settings/branches">Branches</a>

      <a class="js-selected-navigation-item menu-item" data-selected-links="hooks /steinvenic/toupiao/settings/hooks" href="/steinvenic/toupiao/settings/hooks">Webhooks</a>
      <a class="js-selected-navigation-item menu-item" data-selected-links="integration_installations /steinvenic/toupiao/settings/installations" href="/steinvenic/toupiao/settings/installations">Integrations &amp; services</a>


    <a class="js-selected-navigation-item menu-item" data-selected-links="repo_keys_settings /steinvenic/toupiao/settings/keys" href="/steinvenic/toupiao/settings/keys">Deploy keys</a>

  </nav>

</div>


    <div class="column three-fourths">
      
  <div id="options_bucket">
    <div class="Subhead">
      <h2 class="Subhead-heading">Settings</h2>
    </div>
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="d-flex js-edit-repo-container" action="/steinvenic/toupiao/settings/rename" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="4OGUWtQkQ7Hbhb8/dh3NuAEJ672LZyqaTBwatCLpmJx5OMtU3xYWoJmOeosFbk/mUnVB0j+KweHLYyIUdwZAeQ==" />
  <auto-check src="/repositories/check-name?current_name=toupiao&amp;owner=steinvenic" csrf="3Uq9zTw83vvtCiYGpI7bpXMEg4QFDe1vQ4BcH5Co+GCJ7gDtNvmhGjy1MRwoT5cRl16UB8QhBSRIDSp49PY5vw==">
    <dl class="form-group d-inline-block">
      <dt class="input-label">
        <label for="rename_field">Repository name</label>
      </dt>
      <dd>
        <input autocapitalize="off" autofocus="autofocus" class="form-control js-repo-name short js-with-permission-fields" id="rename_field" maxlength="100" name="new_name" size="100" type="text" value="toupiao">
      </dd>
    </dl>
  </auto-check>
  <button type="submit" class="btn js-rename-repository-button flex-self-end mb-3" disabled>Rename</button>
</form>

       <div class="Subhead Subhead--spacious border-bottom-0 mb-0">
         <h2 class="Subhead-heading">
           Features
         </h2>
       </div>
       <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-repo-features-form" data-remote="true" data-autosubmit="true" action="/steinvenic/toupiao/settings/update" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="4DvQQ6MCDTEyCaYMSJsiFaBIMKaR6VzA7SZfwRxJknogI3uxDOoACmqRzClFf05DdvF+lpCQpkRq7Wkk38VrfA==" />
  <div class="Box">
    <li class="Box-row py-0">
      <div class="form-checkbox js-repo-option">
        <input type="hidden" name="has_wiki" value="0">
        <input type="checkbox" name="has_wiki" value="1" id="wiki-feature" checked>
        <label for="wiki-feature">Wikis</label>
        <span class="status-indicator ml-1 js-status-indicator">
          <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
          <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </span>
        <p class="note">
          GitHub Wikis is a simple way to let others contribute content.
          Any GitHub user can create and edit pages to use for documentation,
          examples, support, or anything you wish.
        </p>
      </div>
    </li>

    <li class="Box-row py-0">
      <div class="form-checkbox js-repo-option">
        <input type="hidden" name="wiki_access_to_pushers" value="0">
        <input type="checkbox" name="wiki_access_to_pushers" value="1" id="wiki-pusher-access" >
          <label for="wiki-pusher-access">Restrict editing to collaborators only</label>
        <span class="status-indicator ml-1 js-status-indicator">
          <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
          <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </span>
        <p class="note">Public wikis will still be readable by everyone.</p>
      </div>
    </li>

    <li class="Box-row py-0">
      <div class="form-checkbox js-repo-option">
        <input type="hidden" name="has_issues" value="0">
        <input type="checkbox" name="has_issues" value="1" id="issue-feature" >
        <label for="issue-feature">Issues</label>
        <span class="status-indicator ml-1 js-status-indicator">
          <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
          <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </span>
        <p class="note">
          Issues integrate lightweight task tracking into your repository.
          Keep projects on track with issue labels and milestones, and reference them in commit messages.
        </p>

      </div>
    </li>


      <li class="Box-row py-0">
        <div class="form-checkbox js-repo-option">
          <input type="hidden" name="projects_enabled" value="0">
          <input type="checkbox" name="projects_enabled" id="projects-feature" value="1" checked  >
          <label for="projects-feature">Projects</label>
          <span class="status-indicator v-align-top ml-1 js-status-indicator">
            <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </span>
          <p class="note">
            Project boards on GitHub help you organize and prioritize your work.
            You can create project boards for specific feature work,
            comprehensive roadmaps, or even release checklists.
          </p>
        </div>
      </li>
  </div>

    <div class="Subhead Subhead--spacious">
      <h2 class="Subhead-heading">Data services</h2>
    </div>
    <p>Use the data from your repository to power these enhanced features.
    </p>
    <div class="Box js-repo-data-services">
        <div class="Box-row py-0">
          <div class="form-checkbox js-repo-option">
            <input type="hidden" name="vulnerability_alerts_enabled" value="0">
            <input type="checkbox" name="vulnerability_alerts_enabled" class="js-repo-data-option"
              data-octo-click="repo_vuln_alerts"
              data-octo-dimensions="enabled:true,location:settings"
              value="1" id="vulnerability-alerts-feature"
              >
            <label for="vulnerability-alerts-feature">
              Vulnerability alerts
            </label>
            <span class="status-indicator ml-1 js-status-indicator">
              <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </span>
            <p class="note text-gray-light">
              Receive alerts for known security vulnerablities found in dependencies.
            </p>
          </div>
        </div>
    </div>

  <noscript>
    <button class="btn btn-primary" type="submit">Save changes</button>
</noscript></form>

       <div class="Subhead Subhead--spacious">
         <h2 class="Subhead-heading">
           Merge button
         </h2>
       </div>
       <p>
         When merging pull requests, you can allow any combination of
         merge commits, squashing, or rebasing. At least one option must be enabled.
       </p>
       <div class="Box">
         <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="repository-merge-features js-merge-features-form" data-remote="true" data-autosubmit="true" action="/steinvenic/toupiao/settings/update_merge_settings" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="r2k8G6XIWBHyO5SZMgowWmuWQEOwdQwSnyobdwT+zJ13544L0P5+4YpTf75XAT/MOKqHmMsn2FBB89C2cpEozw==" />

    <div class="flash flash-full flash-warn d-none js-select-one-warning">
      You must select at least one option
    </div>

    <ul>
      <li class="Box-row py-0">
        <div class="form-group js-repo-option">
          <div class="form-checkbox">
            <label for="merge_types_merge_commit">Allow merge commits</label>
            <span class="status-indicator js-status-indicator">
              <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
            </span>
            <input type="checkbox"
                   name="merge_types[]"
                   value="merge_commit"
                   id="merge_types_merge_commit"
                   checked>
            <p class="note">Add all commits from the head branch to the base branch with a merge commit.</p>
          </div>
        </div>
      </li>

      <li class="Box-row py-0">
        <div class="form-group js-repo-option">
          <div class="form-checkbox">
            <label for="merge_types_squash">Allow squash merging</label>
            <span class="status-indicator js-status-indicator">
              <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
            </span>
            <input type="checkbox"
                   name="merge_types[]"
                   value="squash_merge"
                   id="merge_types_squash"
                   checked>
            <p class="note">Combine all commits from the head branch into a single commit in the base branch.</p>
          </div>
        </div>
      </li>

      <li class="Box-row py-0">
        <div class="form-group js-repo-option">
          <div class="form-checkbox">
            <label for="merge_types_rebase">Allow rebase merging</label>
            <span class="status-indicator js-status-indicator">
              <svg class="octicon octicon-check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
            </span>
            <input type="checkbox"
                   name="merge_types[]"
                   value="rebase_merge"
                   id="merge_types_rebase"
                   checked>
            <p class="note">Add all commits from the head branch onto the base branch individually.</p>
          </div>
        </div>
      </li>
    </ul>

  <noscript>
    <button class="btn btn-primary" type="submit">Save changes</button>
</noscript></form>
       </div>

        <div class="Subhead Subhead--spacious">
          <h2 class="Subhead-heading">
            Temporary interaction limits
          </h2>
        </div>
        <p>
          Temporarily restrict which users can interact with your repository (comment, open issues, or create pull requests) for a <strong>24-hour</strong> period. This may be used to force a "cool-down" period during heated discussions.
        </p>
        <div class="Box">
          <ul>
  <li class="Box-row">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/steinvenic/toupiao/community" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="11uwkIcDGlu3M/SwuiHXTcrLG/RLrcJ9CtQK3lY+xRX5wUX7Z1PdrsmLmFTTbqngmt1IcNBMRQxvrOy3Kd8z+w==" />
      <div class="d-flex flex-justify-between flex-items-center">
        <div class="pr-2">
          <input type="hidden" name="toggled_interaction_setting" value="interaction_time_limit">
          <input type="hidden" name="ttl" value="one_day">
          <label for="time-limit">Limit to existing users</label>
          <p class="note">Users that have recently created their account will be unable to interact with the repository.</p>
        </div>
          <button id="time-limit" type="submit" class="btn">
            Enable
          </button>
      </div>
</form>  </li>

  <li class="Box-row">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/steinvenic/toupiao/community" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="BhtVr+e4GrP87WkP2Ukr+oI7+ym9mN56ngTysQIU38kogaDEB+jdRoJVBeuwBlVX0i2orSZ5WQv7fBTYffUpJw==" />
      <div class="d-flex flex-justify-between flex-items-center">
        <div class="pr-2">
          <input type="hidden" name="toggled_interaction_setting" value="contributor_interaction_only">
          <input type="hidden" name="ttl" value="one_day">
          <label for="contributor-only">Limit to prior contributors</label>
          <p class="note">Users that have not previously <a href="/steinvenic/toupiao/graphs/contributors">committed</a> to the repository’s master branch will be unable to interact with the repository.</p>
        </div>
          <button id="contributor-only" type="submit" class="btn">
            Enable
          </button>
      </div>
</form>  </li>

  <li class="Box-row">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/steinvenic/toupiao/community" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="TEYz4HpUTG0/Fy6vyxrim6yYakain7EcrTB/zHBKARNi3MaLmgSLmEGvQkuiVZw2/I45wjl+Nm3ISJmlD6v3/Q==" />
      <div class="d-flex flex-justify-between flex-items-center">
        <div class="pr-2">
          <input type="hidden" name="toggled_interaction_setting" value="collaborator_interaction_only">
          <input type="hidden" name="ttl" value="one_day">
          <label for="collaborator-only">Limit to repository collaborators</label>
          <p class="note">Users that have not been granted <a href="/steinvenic/toupiao/settings/collaboration">push access</a> will be unable to interact with the repository.</p>
        </div>
          <button id="collaborator-only" type="submit" class="btn">
            Enable
          </button>
      </div>
</form>  </li>
</ul>

        </div>

        <div class="Subhead Subhead--spacious">
          <h2 class="Subhead-heading">
            GitHub Pages
          </h2>
        </div>
        <p><a href="https://pages.github.com">GitHub Pages</a> is designed to host your personal, organization, or project pages from a GitHub repository.</p>
        <div class="Box">
          


<li class="Box-row">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/steinvenic/toupiao/settings/pages/source" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="rlsGUxhoqjSslMeAhomHg1mwe8d3nYqZrr79zECHcbhTvJ3oIgDIbOJHkIWDPvldG8PpknwfmtY7J0RKiSedbA==" />
    <strong>Source</strong>
    <p>
        GitHub Pages is currently disabled.
          Select a source below to enable GitHub Pages for this repository.
      <a href="https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/">Learn more</a>.
    </p>
    <span class="js-pages-source select-menu js-menu-container js-select-menu">
      <button class="btn mr-1 select-menu-button js-menu-target" type="button"
        aria-haspopup="true" aria-expanded="false" aria-label="GitHub Pages source">
        <span class="js-select-button js-pages-source-btn-text" data-original-text="None">None</span>
      </button>
      <div class="select-menu-modal-holder">
        <div class="select-menu-modal js-menu-content">
          <div class="select-menu-list js-navigation-container" role="menu">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
              <span class="select-menu-title">Select source</span>
            </div>
                <div class="select-menu-item js-navigation-item" role="menuitem">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="source" id="source_master" value="master" />
                    <span class="select-menu-item-heading js-select-button-text">master branch</span>
                    <span class="description">Use the <code>master</code> branch for GitHub Pages.</span>
                  </div>
                </div>
                <div class="select-menu-item disabled" role="menuitem">
                  <svg class="octicon octicon-check select-menu-item-icon" disabled="disabled" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="source" id="source_master__docs" value="master /docs" disabled="disabled" />
                    <span class="select-menu-item-heading js-select-button-text">master branch /docs folder</span>
                    <span class="description">Use only the <code>/docs</code> folder for GitHub Pages.</span>
                  </div>
                </div>
                <div class="select-menu-item js-navigation-item selected" role="menuitem">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="source" id="source_none" value="none" checked="checked" />
                    <span class="select-menu-item-heading js-select-button-text">None</span>
                    <span class="description">Disable GitHub Pages.</span>
                  </div>
                </div>
          </div>
        </div>
      </div>
    </span>
    <button type="submit" class="btn js-pages-source-save-btn" disabled>Save</button>

      <strong class="d-block mt-3">Theme Chooser</strong>
      <p>
        Select a theme to publish your site with a Jekyll theme<span class="js-pages-theme-source-note">
        using the <code class="js-pages-theme-source-note-value" data-original-text="master branch"> master branch</code></span>.
        <a href="https://help.github.com/articles/creating-a-github-pages-site-with-the-jekyll-theme-chooser/">Learn more</a>.
      </p>
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/steinvenic/toupiao/settings/pages/themes" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input type="hidden" class="js-pages-theme-source-value" name="source" data-original-value="master" value="master">
        <button type="submit" class="btn mt-2 tooltipped tooltipped-s js-enable-btn" disabled
                aria-label="Turn JavaScript on to use the theme chooser.">
            Choose a theme
        </button>
</form></form></li>





        </div>

    <div class="Subhead Subhead--spacious border-bottom-0 mb-0">
      <h2 class="Subhead-heading">
        Danger Zone
      </h2>
    </div>
    <div class="Box Box--danger">
      <ul>
        <li class="Box-row">
          
  <button type="button" class="btn btn-danger boxed-action" disabled>Make private</button>
  <strong>Make this repository private</strong>
  <p>
    Public forks can’t be made private.
    Please
    <a href="https://help.github.com/articles/duplicating-a-repository">duplicate the repository</a>.
  </p>

        </li>
        <li class="Box-row">
          
    <details class="details-reset details-expanded details-expanded-dark">
      <summary class="btn btn-danger boxed-action">Transfer</summary>
      <details-dialog class="anim-fade-in fast Box Box--overlay d-flex flex-column">
        <div class="Box-header">
          <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title">Transfer repository</h3>
        </div>
        <div class="flash flash-full flash-warn">
          To understand admin access, teams, issue assignments, and redirects after a repository is
          transferred, see "<strong><a href="https://help.github.com/articles/transferring-a-repository/">Transferring a repository</a></strong>"
          in GitHub Help.
        </div>
        <div class="Box-body overflow-auto">
            <p class="repo-transfer-tip">Transferring may be delayed until the new owner approves the transfer.</p>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/steinvenic/toupiao/settings/transfer" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="gOWoG4xn0z/TBApzIwbQbWBv0DjPDTlYF1h144BAiyUo3eini9mB0bjE7GO/XF9f4zybv2VveqgfWyoJiq3tiQ==" />
            <dl class="form-group">
              <dt><label for="confirm_repository_name">Type the name of the repository to confirm</label></dt>
              <dd>
                <input class="form-control" type="text" id="confirm_repository_name" autofocus required
                        pattern="[tT][oO][uU][pP][iI][aA][oO]|[sS][tT][eE][iI][nN][vV][eE][nN][iI][cC]/[tT][oO][uU][pP][iI][aA][oO]"
                        aria-label="Type in the name of the repository to confirm that you want to transfer this repository.">
              </dd>
            </dl>
            <dl class="form-group">
              <dt><label for="confirm_new_owner">New owner’s GitHub username or organization name</label></dt>
              <dd><input id="confirm_new_owner" class="form-control" type="text" name="new_owner" id="transfer_field" required aria-label="Type in the username of the new owner."></dd>
            </dl>

            <button type="submit" class="btn btn-block btn-danger" data-disable-invalid>I understand, transfer this repository.</button>
</form>        </div>
      </details-dialog>
    </details>

  <strong>Transfer ownership</strong>
    <p>
      Transfer this repository to another user or to an organization where you
      have the ability to create repositories.
    </p>

        </li>
        <li class="Box-row">
          
<details class="details-reset details-expanded details-expanded-dark">
  <summary class="btn btn-danger boxed-action">Archive this repository</summary>
  <details-dialog class="anim-fade-in fast Box Box--overlay d-flex flex-column">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Archive repository</h3>
    </div>
    <div class="flash flash-full flash-warn">
      Unexpected bad things will happen if you don’t read this!
    </div>
    <div class="Box-body overflow-auto">
      <p>
        This will make the <strong>steinvenic/toupiao</strong> repository, issues,
        pull requests, labels, milestones, projects, wiki, releases, commits, tags, branches, reactions and
        comments read-only and disable any future comments. The repository can still be forked.
      </p>

      <p>Ensure you’ve changed any repository settings, considered closing all open issues and pull requests and updated your README before you archive this repository.</p>

      <p>Once archived, you can unarchive the repository at any time.</p>


      <p>Please type in the name of the repository to confirm.</p>

      <form class="js-normalize-submit" action="/steinvenic/toupiao/settings/archive" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Pn6El94ixEicmY0ZRuA5octIuKkD5vWp/5HETNArPjJbsTWbDZr0mn2tK43R0p0iaWYJrrN50Nowxe6SMcwkHA==" />
        <p>
          <input type="text" class="form-control input-block" autofocus required
                 pattern="[tT][oO][uU][pP][iI][aA][oO]|[sS][tT][eE][iI][nN][vV][eE][nN][iI][cC]/[tT][oO][uU][pP][iI][aA][oO]"
                 aria-label="Type in the name of the repository to confirm that you want to archive this repository."
                 name="verify">
        </p>
        <button type="submit" class="btn btn-block btn-danger" data-disable-invalid>I understand the consequences, archive this repository</button>
</form>    </div>
  </details-dialog>
</details>

<strong>Archive this repository</strong>
<p>Mark this repository as archived and read-only.</p>

        </li>
        <li class="Box-row">
          
  <details class="details-reset details-expanded details-expanded-dark">
    <summary class="btn btn-danger boxed-action" aria-haspopup="dialog">
      Delete this repository
    </summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast" aria-label="Delete repository">
      <div class="Box-header">
        <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
          <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
        <div class="Box-title">Are you absolutely sure?</div>
      </div>
      <div class="flash flash-warn flash-full">
        Unexpected bad things will happen if you don’t read this!
      </div>
      <div class="Box-body overflow-auto">
        <p>
          This action <strong>cannot</strong> be undone. This will permanently delete the <strong>steinvenic/toupiao</strong>
          repository, wiki, issues, and comments, and remove all collaborator associations.
        </p>



        <p>Please type in the name of the repository to confirm.</p>

        <form class="js-normalize-submit" action="/steinvenic/toupiao/settings/delete" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="delete" /><input type="hidden" name="authenticity_token" value="VdeGKzd97V1w6oquFN7JmKU4Ylhkeq9CqwVzpQ8uD8yNnHBax9dmvoyaOr0sBIU5qZVpSIIr7cOGSz0A57F7KQ==" />
          <p>
          <input type="text" class="form-control input-block" autofocus required
                 pattern="[tT][oO][uU][pP][iI][aA][oO]|[sS][tT][eE][iI][nN][vV][eE][nN][iI][cC]/[tT][oO][uU][pP][iI][aA][oO]"
                 aria-label="Type in the name of the repository to confirm that you want to delete this repository."
                 name="verify">
          </p>
          <button type="submit" class="btn btn-block btn-danger" data-disable-invalid>I understand the consequences, delete this repository</button>
</form>      </div>
    </details-dialog>
  </details>

<strong>Delete this repository</strong>

  <p>
    Once you delete a repository, there is no going back. Please be certain.
  </p>

        </li>
      </ul>
    </div>
  </div><!-- /#options_bucket -->

    </div>
  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>






<div id="pjax-head">
  <title>Options</title>
  <meta name="selected-link" value="repo_settings">
  
  
  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/edit_repositories/options" data-pjax-transient="true" />
  
  <meta name="request-id" content="DB00:02E1:591C17:85F168:5B2976CF" data-pjax-transient>
  


    <link href="https://github.com/steinvenic/toupiao/commits/master.atom" rel="alternate" title="Recent Commits to toupiao:master" type="application/atom+xml">

</div>

<div id="js-flash-container">
</div>




'''

html = etree.HTML(html)
result = html.xpath('//form[contains(@action,"delete")]//input[@name="authenticity_token"]/@value')
print(result)