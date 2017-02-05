#!/bin/bash

mkdir -p ~/projects
cd ~/projects

git clone https://github.com/timss/vimconf.git
#git clone https://github.com/vim-scripts/colorsupport.vim.git

cd

rm -f ~/.vimrc

ln -s ~/projects/vimconf/.vimrc ~/.vimrc

vim

### Install shortcuts
echo -e '" Show current time ' >> ~/.vimrc.last
echo -e "map <F2> :echo 'Current time is  ' . strftime('%c')<CR>" >> ~/.vimrc.last

echo -e ":map <C-e> :tabnew <CR>\n" >> ~/.vimrc.last
echo -e ":map <C-h> :tabprevious <CR>\n" >> ~/.vimrc.last
echo -e ":map <C-h> :tabnext <CR>\n" >> ~/.vimrc.last

### Add plugins
echo -e "Plugin 'davidhalter/jedi-vim'" >> ~/.vimrc.plugins
echo -e "Plugin 'scrooloose/nerdtree'" >> ~/.vimrc.plugins
echo -e "Plugin 'vim-scripts/colorsupport.vim'" >> ~/.vimrc.plugins

echo "Installation complete. Don't forget to alias tmux='tmux -2'"
echo "Also, the first time you launch vim, input command"
echo ":PluginInstall"
