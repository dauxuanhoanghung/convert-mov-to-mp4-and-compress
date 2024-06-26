# convert-mov-to-mp4-and-compress

convert-mov-to-mp4-and-compress video

### Cloning project:

```sh
git clone https://github.com/dauxuanhoanghung/convert-mov-to-mp4-and-compress.git
cd convert-mov-to-mp4-and-compress/
```

### Enable virtualenv

```sh
python3 -m venv venv

source venv/bin/activate
```

### Install dependencies

```sh
pip install -r requirements.txt
```

### Extract ffmpeg

```sh
mkdir bin
unzip ffmpeg-7.0.1.zip -d bin/
```

### Run the command to convert

```sh
python main.py
```

### Deactivate venv

```sh
source deactivate
```
