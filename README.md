# dotfiles

Linux configuration files. Repo operation follows https://github.com/randy3k/dotfiles

```
git clone --bare git@github.com:jsta/dotfiles.git $HOME/.dotfiles
alias dotfiles='git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
dotfiles config --local status.showUntrackedFiles no
dotfiles config --local alias.github '!git add -u && git commit -m "Update dotfiles at $(date -u)" && git push'
dotfiles config --local pull.rebase true
dotfiles reset --hard

rm ~/README.md
dotfiles update-index --skip-worktree README.md
```
More details at: https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/
