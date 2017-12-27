#!/bin/bash

DIRNAME="projects"
mkdir -p ~/$DIRNAME
cd ~/$DIRNAME

git clone https://github.com/timss/vimconf.git
#git clone https://github.com/vim-scripts/colorsupport.vim.git

cd

rm -f ~/.vimrc

ln -s ~/$DIRNAME/vimconf/.vimrc ~/.vimrc

vim

### Install shortcuts
echo -e '" Show current time ' >> ~/.vimrc.last
echo -e "map <F2> :echo 'Current time is  ' . strftime('%c')<CR>" >> ~/.vimrc.last

echo -e ":map <C-e> :tabnew <CR>\n" >> ~/.vimrc.last
echo -e ":map <C-h> :tabprevious <CR>\n" >> ~/.vimrc.last
echo -e ":map <C-h> :tabnext <CR>\n" >> ~/.vimrc.last

### Add plugins
echo -e "Plug 'davidhalter/jedi-vim'" >> ~/.vimrc.plugins
echo -e "Plug 'scrooloose/nerdtree'" >> ~/.vimrc.plugins
echo -e "Plug 'vim-scripts/colorsupport.vim'" >> ~/.vimrc.plugins

echo "Installation complete. Don't forget to alias tmux='tmux -2'"
echo "Also, the first time you launch vim, input command"
echo ":PlugInstall"
