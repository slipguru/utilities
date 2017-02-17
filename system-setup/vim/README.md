# VIM

Unless otherwise specified, all command work 
when in _Normal_ or _Visual_ mode.

Also, most of the times you can specify a number before giving a 
command so that that command will affect that number of lines/words
(depending on the action). For instance, `3dd` will delete (actually
cut and store in a sort of Vim permament clipboard) three lines, while
`4p` will paste the content of said clipboard four times.

`CTRL-w ARROW` means first press simultaneously CTRL and w, 
**then** a direction arrow

When in _Command line_ mode (`:`) it is necessary to press ENTER 
to execute the command

### Basics - Modes

 * `i` or `a`: enter _Insert_ mode, either at the point
 where the cursor is (`i`) or the one after (`a`, as _append_)
 * `:` enter command-line mode
 * Pressing ESC returns to _Normal_ mode
 * `v` enters _Visual_ mode (lets you select text as you would
 do with the mouse)

### Saving, quitting, new files

 * `:w` writes the current buffer to disk. Basically, it 
 corresponds to the 'save' command in any other editor
 * `:q` quits Vim. In case there are unsaved changes, you 
 will be prompted (as it happens in other editors)
 * `:w` and `:q` can actually be given at once to write changes
 and quit with `:wq`.
 * if you want to quit discarding unsaved changes without being 
 prompted, use `:q!`

### Buffers

Roughly, buffers correspond to open files.

### Panes 

 * `:split <FILENAME>` splits the current pane horizontally. If no
 `<FILENAME>` is provided, 
 * `CTRL-w ARROW` allows you to navigate panes

## Editing commands

### Copy, paste, delete and navigate

 * `yy` _yanks_ one line
 * `dd` cuts the current line
 * `p` paste whatever is in the 'clipboard'

 * `e` moves to the end of the word.
 * `b` moves to the beginning of the previous word.
 * `$` moves to the end of the line.
 * `^` moves to the beginning of the line.
 * `:N` moves to the Nth line. If N is greater than the number of 
 lines of the current buffer, moves to the end.

 * `u` undo
 * `CTRL-r` redo

 * `/` allows you to search for text. See example below.

In order to select individual words, you must enter _Visual_ mode 
with `v`. At that point you will select text, and will be able 
to **cut** (using `d`, only one 'd' this time)

### Writing code

 * `,cc` comments current one or more lines.
 * `,cu` uncomments one or more lines.
 * `,g` while on a function call will redirect to the declaration of the
   function (works in Python, don't know in other languages)

## Common examples:

 * `ESC v e y`: copies a single word in the clipboard
 * `:1` goes to the beginning of the line
 * `/print ENTER n n`: search for string 'print' in the buffer. The two
 following 'n's move to the next occurences of the string
