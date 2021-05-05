
# Command line instructions

You can also upload existing files from your computer using the instructions below.
## Git global setup
```bash
git config --global user.name "Nguyễn Bình Minh"
git config --global user.email "nguyenbinhminh07101997@gmail.com"
```

## Create a new repository
```bash
git clone git@gitlab.com:vnpt-voice-and-speech/speech-to-text-full/stt_inverse_text_normalization.git
cd stt_inverse_text_normalization
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

## Push an existing folder
```bash
cd existing_folder
git init
git remote add origin git@gitlab.com:vnpt-voice-and-speech/speech-to-text-full/stt_inverse_text_normalization.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

## Push an existing Git repository
```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin git@gitlab.com:vnpt-voice-and-speech/speech-to-text-full/stt_inverse_text_normalization.git
git push -u origin --all
git push -u origin --tags
```

