# file pathing primer
## Absolute Paths
absolute paths always start from the root of the drive
root is denoted in python as an opening slash /
but when you "see" it in file manager it looks like: `Macintosh HD` on Mac, `C:\` on Windows, `/` on Linux
for example this file (in its initial creation on my Mac M4)
is located at `/Users/rudil24/Documents/webdev/pythonCourse/day024/fun_with_paths.py`
> the Macintosh HD is understood as root (the initial /), so we don't need to write it
> 
> also, rule of thumb in most programming language file access, use forward slashes in pathing and it will automatically convert to the local method (e.g. DOS & Windows backslashes)
## Relative Paths
relative paths are relative to the current directory (aka working directory)
so if i'm in folder day024, then it's just "fun_with_paths.py"
- `..` goes "up" one directory
- `./` goes "into" a directory ("look in the current folder for _______")
so if i'm in folder day023, to get to this file i go `../day024/fun_with_paths.md`
if i'm already in day024, to get to this file i go `./fun_with_paths.md`
or i just go `fun_with_paths.py`
## Sidebar: is ./ ever really necessary?
So if `./` always means open working directory, why would we ever need to use it (just name the file you want since you are already in working directory.)
I posed this question to Gemini 3.0 Pro, they gave me a [pretty good answer](https://gemini.google.com/share/d4f2d62192e2). Here's their summary:
### Summary Table: when to use ./ 
| Context | Example | Is `./` Required? |
| :--- | :--- | :--- |
| **File I/O** | `open('file.txt')` | **No** (usually) |
| **Shell Scripts** | `./script.sh` | **Yes** (on Linux/Mac) |
| **Node.js Imports** | `require('./module')` | **Yes** (to avoid `node_modules`) |
| **Python Imports** | `from . import submodule` | **Yes** (for relative imports) |
| **HTML Links** | `<a href="./page.html">` | **No** (browsers imply it) |

***