Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line
echo "# anisble" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sjstanev/anisble.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/sjstanev/anisble.git
git branch -M main
git push -u origin main





Starting with basic configuration and going deeper

** basic**
git clone https://github.com/sjstanev/ansible_tutorial.git
git status

**optional__
git config --global user.name ""
git config --global user.email ""

git diff
git add .
git push origin main
