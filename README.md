## typemusic


### Github Authentication

```bash
ssh-keygen -t ed25519 -f ~/.ssh/typemusic -C "my@email"
cat  ~/.ssh/typemusic.pub 
```

Add deploy key to github repo.

### Create Python Environment

```bash
sudo apt-get install python3.10 python3.10-venv sox

python -m venv typemusic

source typemusic/bin/activate

pip install -r requirements.txt
```

### Sources

Piano samples: [reddit: SingleInfinity](https://www.reddit.com/r/piano/comments/3u6ke7/heres_some_midi_and_mp3_files_for_individual/)


