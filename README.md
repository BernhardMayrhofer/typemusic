## typemusic


### Github Authentication

```bash
ssh-keygen -t ed25519 -f ~/.ssh/typemusic -C "my@email"
cat  ~/.ssh/typemusic.pub 
```

Add deploy key to github repo.

### Create Python Environment

```bash
sudo apt-get install python3.10 python3.10-venv

python -m venv typemusic

source typemusic/bin/activate
```



