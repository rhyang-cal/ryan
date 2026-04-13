# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# The difference between Git, GitHub, and Git Bash is that Git is a version control system that allows developers to track changes in their code and collaborate with others. GitHub is a web-based platform that hosts Git repositories and provides additional features for collaboration, such as issue tracking and pull requests. Git Bash is a command-line interface that provides a Unix-like environment for using Git on Windows.

# 2) What’s the difference between the terminal and the command line?
# The difference between the terminal and the command line is that the terminal is a program that provides a text-based interface for interacting with the operating system, while the command line is the actual interface where you type commands. The terminal can run various command-line interfaces, such as Git Bash or PowerShell, while the command line is specific to the shell you are using within the terminal.

# 3) How does Windows PowerShell differ from Git Bash?
# Windows PowerShell differs from Git Bash in that PowerShell is a task automation and configuration management framework developed by Microsoft, while Git Bash is a command-line interface that provides a Unix-like environment for using Git on Windows. PowerShell has its own scripting language and is designed for system administration tasks, while Git Bash is primarily focused on providing a familiar environment for developers using Git.   

# 4) What’s the difference between Anaconda, conda, and Python?
# The difference between Anaconda, conda, and Python is that Python is a programming language used for various applications, including data science and web development. Anaconda is a distribution of Python that includes a collection of pre-installed packages and tools for data science and machine learning. Conda is a package manager that comes with Anaconda and allows users to manage their Python environments and install additional packages as needed.

# 5) What is VS Code? 
# VS Code, or Visual Studio Code, is a source code editor developed by Microsoft. It provides a wide range of features for coding, debugging, and version control, making it a popular choice among developers. VS Code supports various programming languages and has a large ecosystem of extensions that enhance its functionality. It is available for Windows, macOS, and Linux.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# Jupyter Notebook is an open-source web application that allows users to create and share documents that contain live code, equations, visualizations, and narrative text. It is commonly used for data analysis, scientific research, and machine learning. Jupyter Lab is an extension of Jupyter Notebook that provides a more flexible and powerful interface for working with notebooks, code, and data. It offers features such as multiple document support, drag-and-drop functionality, and a customizable workspace, making it a more versatile tool for data science and development tasks.

# 7) What does ~/ mean?
# The ~/ symbol is a shorthand for the home directory of the current user. It is used in command-line interfaces to quickly navigate to the user's home directory without having to type the full path. For example, if your username is "ryan", then ~/ would refer to /home/ryan on a Unix-like system or C:\Users\ryan on Windows.

# 8) What’s the difference between an absolute path and a relative path?
# An absolute path is a complete path that specifies the location of a file or directory from the root of the file system. It starts with a slash (/) on Unix-like systems or a drive letter (e.g., C:\) on Windows. A relative path, on the other hand, specifies the location of a file or directory in relation to the current working directory. It does not start with a slash or drive letter and can use special symbols like . (current directory) and .. (parent directory) to navigate through the file system.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Absolute path: /home/ryan/course_assignments/homework2
# Relative path: course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# The command to move from "course_assignments/homework2/" to "course_assignments/" is cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# The command rm ./ would attempt to remove the current directory (./) and all of its contents. However, since rm does not allow you to remove a directory without the -r (recursive) option, it would likely result in an error message indicating that it cannot remove a directory. It is important to be cautious when using the rm command, as it can permanently delete files and directories if used incorrectly.

# 12) What do the following commands do?
# git add
    # The git add command is used to stage changes in your working directory for the next commit. It allows you to specify which files or changes you want to include in the commit. For example, git add file.txt would stage the changes made to file.txt for the next commit.
# git commit
    # The git commit command is used to create a new commit with the staged changes. It allows you to provide a commit message that describes the changes being committed. For example, git commit -m "Added new feature" would create a new commit with the message "Added new feature".
# git push
    # The git push command is used to upload your local commits to a remote repository, such as GitHub. It allows you to share your changes with others and collaborate on a project. For example, git push origin main would push your commits to the main branch of the remote repository named origin.

# 13) What's the difference between "git add ." and "git add <file>"?
# The difference between "git add ." and "git add <file>" is that "git add ." stages all changes in the current directory and its subdirectories, while "git add <file>" stages only the specified file. For example, git add . would stage all modified and new files in the current directory, while git add file.txt would only stage the changes made to file.txt. Using "git add ." can be convenient for quickly staging multiple changes, but it may also include unintended changes if you are not careful.

# 14) What do "git status" and "git log -1" do?
# The git status command is used to display the current state of the working directory and staging area. It shows which files have been modified, which files are staged for the next commit, and which files are untracked. For example, git status would show you a list of modified files and their status (e.g., modified, staged, untracked).

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning a repository creates a local copy of the entire repository on your machine, including all of its history and branches. It is typically done when you want to start working on a project for the first time. Pulling from a repository, on the other hand, is used to update your local copy of the repository with changes that have been made by others. It fetches the latest changes from the remote repository and merges them into your local branch. Cloning is a one-time operation to set up your local environment, while pulling is an ongoing operation to keep your local copy up to date with the remote repository.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# My most frustrating bug in this class so far was when I accidentally deleted a file using the rm command. I realized my mistake immediately and tried to recover the file using various methods, such as checking the trash or using file recovery software, but unfortunately, I was not able to retrieve it. To prevent this from happening again, I made sure to double-check my commands before executing them and started using version control more effectively to keep track of changes and avoid accidental deletions in the future.

# 17) What’s a question you still have? What’s something you’re confused about?
# One question I still have is about the best practices for organizing and structuring a Git repository. I am still a bit confused about how to effectively manage branches, handle merge conflicts, and maintain a clean commit history. I would like to learn more about strategies for branching and merging, as well as tips for writing clear and concise commit messages to improve collaboration and maintainability of the codebase.

# 18) Tell me a fun fact!
# I broke my left ankle 3 times.

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print(2 ** 3)  # This expression calculates 2 raised to the power of 3, which equals 8.
